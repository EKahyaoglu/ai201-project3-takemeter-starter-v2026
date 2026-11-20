#!/usr/bin/env python3
import argparse
import random
from collections import Counter

import pandas as pd

VALID_LABELS = {"analysis", "hot_take", "reaction"}


def validate(path: str, sample_size: int = 20, seed: int = 2024) -> dict:
    df = pd.read_csv(path)
    if "text" not in df.columns or "label" not in df.columns:
        raise ValueError(f"{path} must contain text and label columns")

    bad_labels = sorted(set(df["label"].dropna().astype(str).str.strip()) - VALID_LABELS)
    missing_labels = int(df["label"].isna().sum())
    duplicate_text = int(df["text"].duplicated().sum())
    counts = Counter(df["label"].astype(str).str.strip())

    errors = []
    if bad_labels:
        errors.append("invalid labels: " + ", ".join(bad_labels))
    if missing_labels:
        errors.append(f"missing labels: {missing_labels}")
    if duplicate_text:
        errors.append(f"duplicate texts: {duplicate_text}")

    sample = df[["text", "label"]].sample(n=min(sample_size, len(df)), random_state=seed)
    sample.to_csv("label_validation_sample.csv", index=False)

    report = {
        "rows": len(df),
        "counts": dict(sorted(counts.items())),
        "invalid_labels": bad_labels,
        "missing_labels": missing_labels,
        "duplicate_texts": duplicate_text,
        "sample_size": len(sample),
        "errors": errors,
    }
    return report


def main():
    parser = argparse.ArgumentParser(description="Validate the labelled dataset before training")
    parser.add_argument("--data", default="labels.csv")
    parser.add_argument("--sample", type=int, default=20)
    parser.add_argument("--seed", type=int, default=2024)
    args = parser.parse_args()

    report = validate(args.data, args.sample, args.seed)
    print(f"Validated {report['rows']} rows")
    print("Counts:", report["counts"])
    print("Duplicate texts:", report["duplicate_texts"])
    print("Missing labels:", report["missing_labels"])
    print("Invalid labels:", report["invalid_labels"])
    print("Random sample: label_validation_sample.csv")
    if report["errors"]:
        raise SystemExit("\n".join(report["errors"]))


if __name__ == "__main__":
    main()
