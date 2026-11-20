#!/usr/bin/env python3
import argparse
import re

import pandas as pd


def label_text(text: str) -> str:
    text = str(text).lower()
    reaction_words = (
        "can't believe", "cannot believe", "crying", "cried", "shaking",
        "got me", "immediately regret", "wow", "holy shit", "bruh",
        "just got", "just realised", "just watched", "made me",
    )
    support_markers = (
        "chapter", "scene", "episode", "timing", "seconds", "minutes",
        "compared", "comparison", "data", "results", "because", "since",
        "before", "after", "first verse", "shot", "ending", "adaptation",
    )
    if any(marker in text for marker in reaction_words):
        return "reaction"
    if any(marker in text for marker in support_markers):
        return "analysis"
    return "hot_take"


def build(source: str, output: str) -> int:
    df = pd.read_csv(source)
    if "text" not in df.columns:
        raise ValueError(f"{source} must contain a text column")
    df = df[["text"]].copy()
    df["label"] = df["text"].map(label_text)
    df["note"] = "deterministic local rule; human review required"
    df.to_csv(output, index=False)
    return len(df)


def main():
    parser = argparse.ArgumentParser(description="Build labels.csv from a text-only post snapshot")
    parser.add_argument("--source", default="data/public_posts.csv")
    parser.add_argument("--output", default="labels.csv")
    args = parser.parse_args()
    print(f"Wrote {build(args.source, args.output)} rows to {args.output}")


if __name__ == "__main__":
    main()
