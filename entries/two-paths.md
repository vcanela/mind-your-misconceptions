---
title: Two paths
order: 29
misconception: Electricity takes only the path of least resistance
tagline: Current takes every path available to it, with the most going through the easiest one.
topic: Electricity and magnetism
levels: junior, senior
keywords: parallel circuit, resistance, current, Ohm's law, path of least resistance, short circuit, branches, safety, earthing
vault: Misconception - Electricity takes the path of least resistance
related: two-ammeters
---

## Question

A 10 Ω resistor and a 1000 Ω resistor are connected in parallel across a 10 V supply. A current of 1 A flows through the 10 Ω resistor.

![A 10 V supply with a 10 ohm resistor and a 1000 ohm resistor connected in parallel across it.](figures/two-paths.svg)

What current flows through the 1000 Ω resistor?

## Option

None: all the current takes the easier path, through 10 Ω.

> This is "electricity takes the path of least resistance" taken literally. But both resistors are connected directly across the 10 V supply, so each has 10 V across it, and each carries a current of $V/R$. The 1000 Ω path carries much less, 0.01 A, but not none.

## Option

100 A: a hundred times as much, as it has a hundred times the resistance.

> Resistance and current go opposite ways. With the same 10 V across it, a hundred times the resistance means a hundredth of the current: 0.01 A.

## Option (correct)

0.01 A: a hundredth of the current in the other path.

> Right. Each resistor has the full 10 V across it, so each carries a current $I = V/R$: 1 A through 10 Ω, and 0.01 A through 1000 Ω. The easier path takes far more of the current, but not all of it.

## Option

1 A: the same current flows through both paths.

> That would be true for resistors in series, one after the other, where the same current has to pass through both. In parallel, each resistor has the full 10 V across it, so each carries its own current, $V/R$.

## Why it's tempting

"The path of least resistance" is a familiar phrase, used about water, traffic and people, and it sounds like a law of nature. Applied to electricity, it is half right, which makes it persuasive.

It seems to explain things. A short circuit takes nearly all the current; a bird can sit on a power line safely. Both are often explained, loosely, by the current preferring the easy route.

And it matches a picture of current as something that makes a choice at each junction, like a driver picking the quickest road.

## A better picture

**Each branch gets its own current.** In a parallel circuit, every branch is connected across the same two points, so every branch has the same potential difference across it. Each one carries a current given by Ohm's law, $I = V/R$, regardless of what the other branches are doing, as long as the supply holds its voltage steady.

**"Least resistance" means "most current", not "all of it".** A branch with a hundredth of the resistance carries a hundred times the current. A short circuit is a special case: it draws such a large current that nearly all the supply's voltage is lost inside the supply and its wires, leaving almost no potential difference across the other branches. That is why the phrase seems to work there.

**The total.** The current from the supply is the sum of the branch currents: here 1.01 A. Adding the second branch increases the total, rather than stealing current from the first (for a supply that holds its voltage steady).

**The bird on the wire.** A bird standing on a single power line is safe because it isn't connected to anything at a different potential. The wire between its feet has very little resistance, so there is almost no potential difference between them, and almost no current flows through the bird. If it touched a second wire, or the pole, as well, it would carry a large current, however easy the wire beside it.

## In the classroom

- **Measure it.** Connect two resistors of very different values in parallel, with an ammeter in each branch. The high-resistance branch carries a small current, but not zero. Use a low voltage and modest values, for example 100 Ω and 10 kΩ on 3 V, giving 30 mA and 0.3 mA, so that the resistors don't overheat.
- **Calculate each branch.** Have students work out $V/R$ for each branch, then add them to find the supply current, and check with a third ammeter.
- **Rephrase it.** "Current takes every path between the same two points, in inverse proportion to its resistance" is less catchy and much more accurate.
- **Water pipes.** Two pipes leading out of the same tank, one wide and one narrow: water flows through both, more through the wide one.
- **Where it fits.** Parallel circuits in Years 9 and 10; circuit analysis in Years 11 to 13.

## Spotted in the wild

- **The phrase itself.** "Taking the path of least resistance" is everyday shorthand for doing the easy thing, and it quietly reinforces the idea that electricity does the same.
- **Birds on power lines.** Birds perch on high-voltage lines without harm, as long as they touch only one wire and nothing else. Large birds that bridge a wire and an earthed pole or crossarm are electrocuted.
- **Safety advice.** Explanations of electrical safety sometimes say an earth wire protects you by giving the current an easier path than your body. That is not quite how it works (see below).

## Going deeper

**How earthing really protects you.** If you touch a live conductor while also touching earth, you become a parallel path. The current through you is set by the voltage across you and your own resistance, $V/R$, and another, easier path elsewhere doesn't reduce it. Earthing protects in a different way: if a fault connects a metal case to the live wire, the earth wire lets a very large current flow, which blows a fuse or trips a circuit breaker within a fraction of a second, cutting off the supply. In the moment before that, the earth wire also keeps the case well below mains voltage, which limits any shock: it lowers the voltage across you, rather than luring current away from you. A residual current device (RCD) adds a second safeguard, switching off within a few hundredths of a second when even a small current, typically 30 mA, leaks to earth instead of returning along the neutral wire, for example through a person.

**Dividing a fixed current.** If a fixed total current $I$ is shared between two resistors $R_1$ and $R_2$ in parallel, the currents are in inverse proportion to the resistances: $I_1/I_2 = R_2/R_1$. That is the precise sense in which current "prefers" the easier path.
