---
title: Two power supplies
order: 40
misconception: It's the current that kills, not the voltage
tagline: Current through the body does the harm, but the voltage across the body decides how much current flows.
topic: Electricity and magnetism
levels: junior, senior
keywords: electrical safety, electric shock, current, voltage, resistance, Ohm's law, mains, car battery, body resistance
vault: Misconception - It's the current that kills, not the voltage
related: two-paths
---

## Question

There are two power supplies: a 12 V battery that can deliver up to 500 A, and a 230 V AC supply that can deliver at most 0.2 A.

Someone with dry hands grips one terminal of a supply in each hand, so that current crosses their chest from hand to hand. Which supply would drive the more dangerous current through them?

## Option

The 12 V battery, because it can deliver far more current.

> The battery can deliver hundreds of amps, but only through something with very low resistance, like a car's starter motor. The current through a person is set by the voltage across them and their body's resistance, $I = V/R$. At 12 V, dry skin lets through only a few milliamps at most.

## Option

Both equally, because the body's resistance limits the current.

> The body's resistance does limit the current, but by $I = V/R$ the same resistance lets through far more current at a higher voltage. And the skin's resistance itself falls steeply at higher voltages. 230 V drives a vastly larger current through a person than 12 V does.

## Option

Neither: 0.2 A is far too small a current to be dangerous.

> 0.2 A is 200 mA, well above the current that can disrupt the heart's rhythm when it crosses the chest for a second or so. And at 230 V, through dry hands, a current of the order of a hundred milliamps can flow, and this supply can deliver it.

## Option (correct)

The 230 V supply, because its higher voltage pushes more current through the body.

> Right. The current through a body is set by the voltage across it and the body's resistance, $I = V/R$. At 12 V, dry skin keeps the current to a few milliamps at most. At 230 V the skin resists far less, the body's resistance from hand to hand is typically one to two kilohms, and a current of the order of a hundred milliamps can flow: enough to send the heart into fibrillation. The battery's ability to deliver 500 A is irrelevant, because 12 V can't push that through a person.

## Why it's tempting

"It's the current that kills, not the voltage" is a popular slogan, and it is half true: current through the body is what does the damage. Repeated often enough, it sounds like the sophisticated answer.

Van de Graaff generators seem to prove it. They reach hundreds of thousands of volts, yet the spark from one is normally harmless, so high voltage alone can't be dangerous.

And a battery that can deliver hundreds of amps sounds powerful and dangerous, while a supply limited to a fraction of an amp sounds tame.

## A better picture

**Current does the damage.** Current through the body heats tissue and, most dangerously, disrupts the electrical signals that control the heart. For alternating current, about 1 mA is just felt; around 10 mA makes it hard to let go; a few tens of milliamps from hand to feet for about a second can make the heart lose its rhythm (more, around a hundred milliamps, for a hand-to-hand path, which carries less of the current through the heart).

**Voltage drives the current.** The current through the body is $I = V/R$, where $V$ is the voltage across the body and $R$ its resistance. Most of the resistance is in the skin. Dry skin resists strongly at low voltages, but above about 50 V its resistance falls steeply, and at mains voltage the resistance from hand to hand is typically one to two kilohms. Above about 500 V the skin breaks down completely.

- **12 V** is far too low to lower the skin's resistance much, and drives only a few milliamps at most.
- **230 V** drives of the order of a hundred milliamps or more, which can be lethal.

**What the supply can deliver into a short circuit doesn't set the current through you.** A car battery can push hundreds of amps through a starter motor, which has a tiny resistance, but not through you. A supply's capacity matters only when it is too small to sustain a dangerous current at all, as with a Van de Graaff generator or a static shock.

**Voltage, resistance and time all matter.** The voltage and the body's resistance set the current, and the current, how long it flows and its path through the body together decide the harm.

## In the classroom

- **Put numbers through Ohm's law.** Work out the current through a body of, say, 5 kΩ at 12 V (a firm grip with dry hands), and of 1.5 kΩ at 230 V. The difference makes both slogans, "voltage kills" and "current kills", look incomplete.
- **Explain the Van de Graaff properly.** When using one, say *why* it is safe: it stores only a tiny charge and can't keep up a current (its belt supplies only microamps), so the discharge is over in a tiny fraction of a second and delivers less than a joule. Even so, anyone with a pacemaker or a heart condition should not take part.
- **Safety first.** Mains electricity is dangerous precisely because its voltage is high enough to drive a lethal current through the body. No demonstration should suggest otherwise.
- **Where it fits.** Electrical safety in Years 9 and 10; Ohm's law and circuits in Years 11 to 13.

## Spotted in the wild

- **Extra-low voltage.** Wiring rules in New Zealand and Australia treat supplies not exceeding 50 V AC or 120 V ripple-free DC as "extra-low voltage", because they can't normally drive a dangerous current through the body.
- **Static shocks.** The spark from a door handle after walking on carpet can involve thousands of volts, yet it is harmless, because only a tiny charge flows, for a tiny time.
- **Electric fences.** Farm electric fences use high-voltage pulses, several thousand volts, but each pulse is very short and carries limited energy, so it gives a painful but normally safe shock.

## Going deeper

**What fuses and RCDs protect.** A fuse or circuit breaker protects wiring from overheating: it acts only at currents of many amps, hundreds of times more than the few tens of milliamps that can disrupt the heart. A residual current device (RCD) protects people, by switching off when current leaks to earth, for example through someone touching a live wire while standing on the ground. But if a person touches both the live and the neutral wires, the current goes out along one and back along the other, and an RCD can't tell it from a normal appliance.

**A car battery's real dangers.** A 12 V car battery can't drive a dangerous current through skin, but it has other dangers. A spanner or a metal ring that bridges its terminals can carry hundreds of amps and get hot enough to cause serious burns. Charging batteries give off hydrogen, which a spark can ignite, and the explosion sprays sulfuric acid. The traction battery of an electric or hybrid car is a different matter: at hundreds of volts, it can kill.

**Deliberate shocks.** A defibrillator works by passing a large, brief current across the chest and through the heart, stopping its chaotic rhythm so that a normal one can restart. A typical shock delivers 150 to 200 joules in about a hundredth of a second.
