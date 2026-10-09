---
title: Swimmer and current
order: 1
misconception: A current that slows you one way and helps you the other cancels out
tagline: Speeds only average out over equal times, and the slow half of the swim always takes longer.
topic: Motion and forces
levels: junior, senior
keywords: speed, average speed, relative velocity, river, swimming, current, wind
credit: Question by Victor Canela.
---

## Question

A swimmer can keep up a steady speed $v$ through the water. She swims the same total distance, $L$, in two places.

- **In a river** with a steady current of speed $c$, slower than she can swim. She swims half the distance upstream, against the current, then turns and swims back downstream, with it.
- **In a swimming pool**, where the water is still. She swims half the distance out and half back.

![The two swims. In the river she swims half the distance upstream and half back downstream; in the pool the water is still.](figures/swimmer-and-current.svg)

Where does she finish her swim soonest?

## Option (correct)

In the swimming pool

> Against the current she moves past the bank at $v - c$; with it, at $v + c$. The two halves are the same distance, but she spends longer on the slow half than on the fast half, so the slow half counts for more. The river always loses.

## Option

In the river

> The current does give her a real boost on the way back. But it holds her back on the way out, and she spends longer being held back than being helped. No current, however fast, lets the river win.

## Option

It takes the same time in both

> This is a very common answer, from adults as well as students. The current takes $c$ away on the way out and gives $c$ back on the way home, so it seems to cancel. It would cancel if she spent equal *times* on each half. She doesn't: she covers equal *distances*, and the slow half takes longer.

## Option

There isn't enough information to decide

> With no numbers given, it feels as though nothing can be worked out. In fact the river loses for every swimmer and every current, as long as the current is slower than she is. (If it weren't, she would never finish the upstream half at all.)

## Why it's tempting

The situation looks perfectly symmetrical: the same current, the same distance, once against and once with. Symmetry is usually a good guide in physics, and here it suggests that the two effects cancel.

Underneath is a habit we all share: averaging speeds. "Two speeds, so take the average" is the first idea most of us reach for, and it is often nearly right. The average of $v - c$ and $v + c$ is exactly $v$, which seems to settle the matter. But a plain average of speeds is only correct when equal *times* are spent at each speed, and that condition is almost never checked.

## A better picture

Put in some numbers. Say she swims at 2 m/s, the current flows at 1 m/s, and the total distance is 100 m.

- **Pool:** 100 m at 2 m/s takes **50 s**.
- **River, upstream:** 50 m at 2 − 1 = 1 m/s takes 50 s. She has already used up the whole pool time, and she still has to come back.
- **River, downstream:** 50 m at 2 + 1 = 3 m/s takes about 17 s.

The river swim takes about **67 s**. Her average speed for it is 100 m ÷ 67 s = 1.5 m/s, not 2 m/s.

In general, for a total distance $L$, the river time is

$$t_\text{river} = \frac{L/2}{v-c} + \frac{L/2}{v+c} = \frac{L}{v}\cdot\frac{v^2}{v^2-c^2}$$

The first factor is the pool time. The second is greater than 1 whenever there is any current at all.

The safe rule is to go back to the definition: **average speed is total distance divided by total time.** Work out the time for each part, add the times, and divide.

## In the classroom

- **Vote first.** Show the question and have everyone commit to an answer, fingers up for a to d, before any discussion. Then pairs try to convince each other and vote again. This is Eric Mazur's peer instruction, and the question suits it well because classes usually split.
- **Push to an extreme.** Ask what happens if the current is almost as fast as the swimmer. The upstream half takes almost forever, and no downstream boost can repay that. Extreme cases are one of the best tools for testing an intuition, and worth naming as a tool.
- **Make the times visible.** Draw a time line for each swim, with each half drawn to scale. The long upstream block makes the answer obvious at a glance.
- **A road trip version.** You drive 60 km at 30 km/h, then 60 km at 90 km/h. Is your average speed 60 km/h? (No: it is 45 km/h, since the trip takes 2 hours and 40 minutes.)
- **Where it fits.** Average speed in Years 9 and 10; relative velocity in Years 12 and 13.

## Spotted in the wild

- **Wind on a round trip.** A cyclist riding out and back on a windy day, or an aircraft flying a return trip at the same airspeed both ways, with a headwind one way and a tailwind the other, always takes longer than in still air. Cyclists joke that the wind is always in their face. The tailwind is real, but it doesn't last as long; and for a cyclist, air resistance makes a headwind cost even more than a tailwind gives back.
- **Moving walkways.** Walk against an airport walkway one way and with it on the way back, and the round trip is slower than walking on the floor.
- **"It all evens out."** The everyday phrase carries the same assumption: that gains and losses balance, even when they don't last equally long.

## Going deeper

**Crossing instead.** Suppose she swims the same distance across the river and back. To go straight across she must aim partly upstream, so her speed across is $\sqrt{v^2-c^2}$, and the time is

$$t_\text{across} = \frac{L}{v}\cdot\frac{1}{\sqrt{1-c^2/v^2}}$$

This is longer than the pool, but shorter than up and down the river.

**Michelson and Morley.** This comparison is the heart of the Michelson–Morley experiment of 1887. Light was thought to travel through an "ether", and the Earth's motion through it should create an ether wind. Light sent along the wind and back should take a little longer than light sent across it and back, exactly like the swimmer. Michelson and Morley compared the two with an interferometer and found no difference: any shift was less than a fortieth of what the ether theory predicted. That null result is now seen as one of the key experimental supports for special relativity, although Einstein said it played little direct part in his own thinking.

**The harmonic mean.** For equal distances covered at speeds $v_1$ and $v_2$, the average speed is $\dfrac{2v_1v_2}{v_1+v_2}$, the harmonic mean, which is never larger than the ordinary average. A classic puzzle: you drive up a hill at 30 km/h. How fast must you drive down to average 60 km/h for the round trip? (You can't: you would have used up all the time on the way up.)
