# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1.

<!-- Your criterion. It must name a number. -->

On the held-out test set, overall accuracy is at least **0.68** across all
three random seeds.

**Why this target:** With three labels, chance performance is about 0.33. A
0.68 accuracy target requires the classifier to identify the post's function
well enough to be useful for triage, while allowing for the overlap between
heated analysis and unsupported hot takes.



---

## 2.

<!-- Your criterion. -->

Every label has an F1 score of at least **0.55** on the held-out test set in
each seed, and the macro-F1 is at least **0.60**.

**Why this target:** The three labels are not equally easy: short reactions
are easy to spot, while `analysis` and `hot_take` share confident language.
The 0.55 per-label floor prevents the model from hiding a weak label inside a
good overall score, and the 0.60 macro-F1 keeps performance balanced.



---

## 3.

<!-- Your criterion. -->

After collecting 200 posts, each label represents at least **15%** and at
most **50%** of the dataset.

**Why this target:** The corpus should include enough examples of reactions,
unsupported judgments, and evidence-backed discussion for every label to be
learnable. A 15% minimum gives the smallest label roughly 30 examples, while
the 50% maximum stops the majority class from becoming a default answer.



---

## 4.

<!-- Your criterion. -->

On a blind double-label sample of **30** posts, a second human labeler and I
agree on at least **80%** of labels, with Cohen's kappa of at least **0.60**.

**Why this target:** The hardest distinction is whether a specific detail is
actual support or merely a confident assertion. Requiring both 80% raw
agreement and a 0.60 chance-adjusted agreement checks that the decision rule
is usable by another reader, not just by me.



---

## 5.

<!-- Your criterion. -->

Among predictions whose highest class probability is at least **0.80**, at
least **85%** are correct on the held-out test set.

**Why this target:** A high-confidence prediction should be safer to use for
initial sorting than an uncertain one. The 0.80 confidence cutoff leaves the
model free to abstain on ambiguous `analysis` versus `hot_take` cases, while
85% precision makes the confident queue meaningfully more reliable than the
overall target.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
