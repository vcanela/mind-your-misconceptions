---
title: Two half-lives
order: 21
misconception: After two half-lives, a radioactive sample has all decayed
tagline: In each half-life, half of what is left decays. The amount halves again and again, rather than running out.
topic: Atoms and nuclei
levels: junior, senior
keywords: half-life, radioactive decay, radioactivity, exponential decay, isotope, nucleus, carbon dating
vault: Misconception - After two half-lives everything has decayed
---

## Question

A sample contains 8000 atoms of a radioactive isotope with a half-life of 1 hour.

Roughly how many of those atoms will still be undecayed after 2 hours?

## Option

None of them

> This treats decay like a steady process, a bath emptying at a constant rate: half gone in the first hour, the rest in the second. But in each half-life, half of what *remains* decays. After the first hour, 4000 remain; in the second hour, half of those decay, leaving about 2000.

## Option

About 1000

> That would be three half-lives' worth: 8000, then 4000, then 2000, then 1000. After two hours, only two halvings have happened, leaving about 2000.

## Option (correct)

About 2000

> Right. In the first hour, half of the 8000 decay, leaving 4000. In the second hour, half of the remaining 4000 decay, leaving about 2000. Because decay is random, the actual number will be close to 2000, but probably not exactly.

## Option

About 4000

> That is how many remain after one half-life, one hour. In the second hour, half of those 4000 decay too, leaving about 2000.

## Why it's tempting

Many everyday processes run at a steady rate. A bath that loses half its water in ten minutes, draining steadily, is empty in twenty. It is natural to apply the same reasoning to radioactive decay.

The name doesn't help. "Half-life" can sound like "half of its life", and two halves make a whole.

And the halving pattern is genuinely unfamiliar. The idea that each step removes a fraction of what is left, rather than a fixed amount, takes some getting used to.

## A better picture

**Each nucleus has a fixed chance.** Every nucleus of a given isotope has the same, fixed chance of decaying in any given time. So the number that decay in each hour depends on how many are still there: the more there are, the more decay. In each half-life, on average, half of the nuclei that are still there decay.

| Half-lives | Fraction remaining |
|---|---|
| 0 | 1 |
| 1 | 1/2 |
| 2 | 1/4 |
| 3 | 1/8 |
| 10 | about 1/1000 |
| 20 | about one in a million |

**It never quite runs out on schedule.** The amount halves again and again. For a real sample, with a finite number of nuclei, the last one does eventually decay, but at a moment nobody can predict.

**Nuclei have no memory.** A nucleus that has survived for one half-life is no more likely to decay in the next than a brand new one. There is no sense in which its time is "due", just as a die doesn't remember its previous rolls.

## In the classroom

- **The dice.** Give the class a large number of dice. Roll them all, remove the sixes as "decayed", and count the rest. Repeat. The numbers fall by about a sixth each roll, halving every three or four rolls, never all at once, and the last few dice go at unpredictable moments.
- **Coins.** Flip a large number of coins and remove the heads each time. Here the "half-life" is one flip, so the halving is easy to see.
- **Graph it.** Plot the number remaining against time, and on the same axes draw the straight line the "steady rate" idea predicts. The difference between the two is the whole point.
- **Tearing paper, with care.** Tearing a sheet of paper in half again and again shows the halving pattern, but it is exact and predictable, unlike real decay. Use it for the arithmetic, and the dice for the randomness.
- **Where it fits.** Radioactivity in Years 9 and 10; half-life and exponential decay in Years 11 to 13. The same mathematics appears in biology (drug levels in the body) and chemistry (first-order reactions).

## Spotted in the wild

- **Carbon dating.** Carbon-14 has a half-life of about 5,730 years. After 50,000 years, nearly nine half-lives, only about a quarter of one percent of the original carbon-14 remains, which is why radiocarbon dating works only for things younger than about that.
- **Medical tracers.** Technetium-99m, the most widely used tracer in nuclear medicine, has a half-life of about 6 hours. After a day, about a sixteenth is left; after two days, less than half a percent.
- **Caffeine.** Caffeine and many medicines are cleared from the body in a similar halving pattern. Caffeine's half-life is around five hours on average, though it varies a great deal from person to person, which is why an afternoon coffee can still be at work at bedtime.

## Going deeper

**The exponential law.** The number of undecayed nuclei after time $t$ is $N = N_0 \left(\tfrac{1}{2}\right)^{t/T}$, where $T$ is the half-life. The average lifetime of a nucleus is about 1.44 times the half-life: some decay almost at once, others last many half-lives.

**Can anything change a half-life?** Heating, compressing or chemically combining a radioactive substance has almost no effect on its half-life, because these processes involve the electrons, far from the nucleus. There are small exceptions. Nuclei that decay by capturing one of their own electrons, such as beryllium-7, change their half-life by up to about one percent depending on their chemical surroundings. And in 1996, physicists stripped every electron from rhenium-187: its half-life fell from about 42 billion years to 33 years, because the bare nucleus can decay in a way that is otherwise blocked.
