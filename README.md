# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->

I am collecting public text posts from Reddit's r/SteelBallRun community. I
read recent posts through the community's public RSS feed and sampled roughly
35 posts before choosing labels; the community has discussion, questions,
fan-art and adaptation reactions, so it has real variation in post type. The
classifier sorts posts by what the text is doing: evidence-backed
interpretation, unsupported confident judgment, or immediate emotional
response. I will collect at least 200 public posts from the same community.

### Candidate distinctions observed while reading

- Some posts cite a specific chapter, scene, timing, quote, or comparison;
     others make a judgment without giving a checkable reason.
- Some posts mainly express an immediate feeling about a newly released
     episode, image, song, or chapter rather than making an argument.
- Some posts ask for information or invite opinions, while others assert a
     conclusion; a question is labelled by the substance of its text only when
     it also contains one of the three target behaviors.
- Posts vary sharply in length: a paragraph that explains a connection is
     different from a one-line reaction, even when both use strong emotion.



---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

### `label_one`

**Definition:** `analysis` makes an interpretation or argument and supports it
with a specific, checkable detail from the manga, anime, or adaptation.

**Example 1:**
> "Holy shit The Chain works perfectly for the ending, the drum beats are the
> same timing as the light flashing at the beginning, and the end credits go
> until the end of the first verse (90 seconds)."

**Example 2:**
> "Someone asks a normal question or makes a casual post then gets called a
> larper or edit watcher ... Knowing the exact stage of A Man's World does not
> make you superior ... Some people just like the story."

### `label_two`

**Definition:** `hot_take` makes a confident evaluation or prediction without
offering a specific detail that would let a reader check the reasoning.

**Example 1:**
> "Oyecomova with red, white and blue facepaint. Alt Title: Oyecomova if David
> Pro weren't Shueisha glazers."

**Example 2:**
> "Who Shot Johnny? must be changed for the anime."

### `label_three`

**Definition:** `reaction` is primarily an immediate feeling or short response
to something just seen, read, or heard, without an argument to establish.

**Example 1:**
> "This manga got me crying bruh im at the later end of it like chapter 87"

**Example 2:**
> "Bro's fr even hittin the same pose."

### The hardest boundary

**Which two labels:** `analysis` and `hot_take`

**The decision rule I used every time:** If the post names a specific scene,
chapter, quote, timing, adaptation choice, or comparison and uses it as
support for its conclusion, it is `analysis`, even if the tone is heated. If
the conclusion has no such checkable support, it is `hot_take`. A question is
not automatically a `reaction`; classify its text by this same evidence rule.

### Boundary stress test

These are eight deliberately borderline examples generated for the taxonomy
check. The rule above gives each one a single label.

| Example | Label | Why |
|---|---|---|
| "The ending is perfect." | `hot_take` | Strong judgment, no support. |
| "The ending is perfect because the final shot repeats the opening panel." | `analysis` | Specific checkable comparison. |
| "I cannot believe that ending happened." | `reaction` | Immediate feeling, no argument. |
| "Why is everyone saying the ending is perfect?" | `hot_take` | A judgment is asserted without evidence; the question form does not change that. |
| "The ending song works: its first verse lasts about 90 seconds, matching the credits." | `analysis` | Timing is offered as support. |
| "That episode made me cry." | `reaction` | Emotional response to something just watched. |
| "The new colors are awful; the manga palette made Gyro's green eyes readable." | `analysis` | Specific adaptation detail supports the evaluation. |
| "The anime ruined the colors." | `hot_take` | Confident evaluation without a supporting detail. |



---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:**

I collected 200 whole public submissions from Reddit's r/SteelBallRun using a
public historical Reddit archive. I deduplicated by normalized post text and
kept the title and body together in `labels.csv`.

**How I labelled them:** I applied the written taxonomy to the full text in a
deterministic pre-labeling pass. The first 20 rows are reserved as the cold
sample and are marked `cold - provisional label; manually verify unaided`; they
still need my unaided check before the agreement comparison. The remaining rows
are marked as pre-labelled from the public archive. This is disclosed because
the rows still need a human review and correction pass before the dataset is
treated as final.

**Counts per label:**

| Label | Count | Share |
|---|---|---|
| `analysis` | 64 | 32.0% |
| `hot_take` | 71 | 35.5% |
| `reaction` | 65 | 32.5% |
| **Total** |  | 100% |

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:* "Since they're showing the Oyecomova fight before Gyro's
> backstory, the dialogue during the fight won't make any sense."
>
> *Could have been:* `analysis` or `hot_take`
>
> *I chose, because:* It makes a confident prediction but gives no specific
> checkable scene detail to support it, so I chose `hot_take`.

**2.**
> *The post:* "Holy shit The Chain works perfectly for the ending, the drum
> beats are the same timing as the light flashing at the beginning, and the end
> credits go until the end of the first verse (90 seconds)."
>
> *Could have been:* `analysis` or `reaction`
>
> *I chose, because:* Although the tone is excited, it gives a specific timing
> and visual comparison, so I chose `analysis`.

**3.**
> *The post:* "Cannot wait to see this scene animated"
>
> *Could have been:* `reaction` or `hot_take`
>
> *I chose, because:* It is an immediate feeling about a future adaptation
> with no argument, so I chose `reaction`.

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:** `distilbert-base-uncased`

**Settings:** 3 epochs, learning rate `2e-5`, batch size `16`, maximum length
`128`, seed `42`

**Anything I changed from the defaults, and why:** Nothing. I ran the default
settings on the project's `.venv` kernel using Apple Silicon MPS (`torch 2.14.1`).

**Split sizes:** train `139` / validation `31` / test `30`. Test counts were
`analysis 9`, `hot_take 11`, and `reaction 10`; no label had fewer than about 8
test examples.



---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:* Help me turn the observed r/SteelBallRun distinctions
     into boundaries that another person could apply.
- *What came back:* The evidence-versus-unsupported-judgment rule and the
     `analysis`, `hot_take`, and `reaction` definitions.
- *What I changed:* I recorded the checkable-detail rule and added boundary
     stress tests to the taxonomy.

**Moment 2**

- *What I asked for:* Help collect and structure public posts for the dataset.
- *What came back:* A deduplicated CSV with whole post text and provisional
     labels using the written taxonomy.
- *What I changed:* I checked the schema, counts, duplicates, label balance,
     and provenance notes; the 20 cold rows remain explicitly provisional for my
     manual verification.

**Pre-labelling disclosure:** The 200 rows were provisionally labelled by a
local deterministic rule informed by the written definitions. I have not yet
manually corrected every row, so the cold sample and the rest of the corpus
need that human review before a final training run.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
