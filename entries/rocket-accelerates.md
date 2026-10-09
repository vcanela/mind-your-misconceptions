---
title: Rocket accelerates
order: 2
misconception: Objects move in the direction they are pushed
tagline: A force changes the motion an object already has. It doesn't replace it.
topic: Motion and forces
levels: junior, senior
keywords: force, Newton's first law, Newton's second law, inertia, projectile, trajectory, path, space, rocket, thrust
credit: Question by Victor Canela. Questions of this kind were made famous by the Force Concept Inventory (Hestenes, Wells and Swackhamer, 1992), which showed how widely this misconception survives physics teaching.
vault: Misconception - Force means motion
---

## Question

Far out in space, well away from any planet or star, a rocket is drifting to the right at a steady speed. Its engine is off, and it points straight up the page, at right angles to the way it is moving.

![The rocket drifting to the right with its engine off, pointing up the page.](figures/rocket-start.svg)

Then the engine fires, and keeps firing with a steady thrust. The rocket doesn't turn: it keeps pointing straight up the page.

Which path does the rocket follow once the engine is on?

## Option

![A straight path, slanting up and to the right.](figures/rocket-a.svg)

> This straight, slanting path is what you would get if the engine instantly added an upward velocity to the sideways one, and the rocket then kept that new direction. But a path stays straight only if the force points along it. Here the push is upwards while the rocket is moving sideways, so its direction of motion has to keep changing. The engine doesn't hand over an upward speed all at once: it builds one up gradually, from zero. So the path must start out horizontal and then bend. (A straight slant *would* be right for a single, instant kick.)

## Option

![A straight path, going directly up the page.](figures/rocket-b.svg)

> This is the idea that an object goes where it is pushed: push up, and up it goes. It is one of the most deeply held ideas there is, and goes back to Aristotle. But nothing takes away the rocket's sideways motion. There is no sideways force, so the sideways speed stays exactly what it was, and the rocket keeps drifting right while it speeds up upwards.

## Option

![A curved path that sets off steeply upwards, then flattens out towards the horizontal.](figures/rocket-c.svg)

> This path curves, which is a good sign, but the wrong way. It sets off steeply upwards and then flattens out, as though the engine's push fades and the old drift takes over again. In fact the engine keeps pushing up for as long as it fires, so the path keeps getting steeper. A path always bends towards the side the force pushes on.

## Option (correct)

![A curved path that sets off horizontally, then bends upwards, getting steeper and steeper.](figures/rocket-d.svg)

> The sideways speed never changes, because nothing pushes sideways. The upward speed starts at zero and grows steadily. Put the two together and you get a curve that starts out horizontal and gets ever steeper: a parabola, the same shape as the path of a ball rolling off a table, turned upside down.

## Why it's tempting

On Earth, it is usually true. Push a box across the floor and it goes where you push; stop pushing and it stops. Friction quietly removes any motion you aren't actively keeping up, so in everyday life the direction of a push and the direction of motion nearly always match. Our intuitions are built in that world.

So it is natural to treat a force as the thing that *sets* motion, when in fact it *changes* motion. This was Aristotle's view, and studies of students before and after physics courses find that many still hold it at the end.

Space makes it harder still. We have no everyday experience of motion without friction, and films rarely help, with spacecraft that bank and swoop like aircraft.

## A better picture

Treat the two directions separately: they don't affect each other.

- **Sideways:** no force, so no change. The rocket keeps moving right at the speed it already had, covering equal distances in equal times (Newton's first law).
- **Upwards:** a steady force, so a steady acceleration from rest. In equal time intervals, the total height gained grows as 1, 4, 9, 16, 25 (Newton's second law).

![Positions of the rocket at equal time intervals after the engine fires.](figures/rocket-strobe.svg "Positions of the rocket at equal time intervals after the engine fires. The sideways steps stay equal; the height gained grows as 1, 4, 9, 16, 25.")

Equal sideways steps combined with ever larger upward ones give a curve that starts flat and gets steeper. In symbols, with sideways speed $u$ and upward acceleration $a$:

$$x = ut, \qquad y = \tfrac{1}{2}at^2 \quad\Longrightarrow\quad y = \frac{a}{2u^2}\,x^2$$

which is a parabola. The force set the *change* in velocity. The velocity the rocket already had carried on as before.

## In the classroom

- **Bowling ball and broom.** Roll a heavy ball (a bowling ball or a medicine ball) along a smooth floor, and have students steer it round a course using only taps from a broom. They soon discover that tapping towards the target doesn't send the ball there: first they have to deal with the motion it already has.
- **Two balls at once.** Drop one ball and launch another horizontally at the same moment, from the same height. They land together: the sideways motion doesn't affect the vertical one. It is the same independence, with gravity in place of the engine.
- **Predict, then dot.** Before anyone draws a curve, ask students to mark where the rocket is at equal time intervals. Building the path from dots makes the shape hard to avoid.
- **Language.** Prefer "the force changes the motion" to "the force makes it move".
- **Where it fits.** Newton's first law, qualitatively, in Years 9 and 10; projectile motion and vectors in Years 12 and 13.

## Spotted in the wild

- **Asteroids.** In the 1979 arcade game, the ship keeps drifting long after you stop thrusting. (The game adds a little drag, so it does slow down eventually.) To stop quickly, you turn round and thrust the other way, which many new players find surprisingly hard: a sign of how Aristotelian our instincts are.
- **Space films.** Spacecraft that bank into turns like aircraft, or slow down when their engines cut out, are everywhere. Series that get it right, such as *The Expanse*, are rare enough to be praised for it.
- **Skids.** A car or bike that hits ice on a bend carries on almost straight, in the direction it was heading when it lost grip, even if it spins. With almost no sideways grip, almost nothing changes its direction.

## Going deeper

**A lightening rocket.** A real rocket burns fuel, so it gets lighter, and the same thrust gives an ever larger acceleration. The path bends upwards faster than a true parabola, but it still starts horizontal and steepens, so option d is still the best choice.

**Charges in a field.** An electron fired between two charged plates feels a steady force at right angles to its motion, and follows the same parabola. This is how the beam was steered in an oscilloscope tube (television tubes mostly used magnetic coils instead), and part of how J. J. Thomson measured the charge-to-mass ratio of the electron.

**Turn the rocket, get a circle.** Suppose the rocket rotated so that its thrust stayed at right angles to its *velocity*, rather than to the page. Its speed would never change, only its direction, and it would travel in a circle (ignoring the fuel it burns; with that, the circle slowly tightens). A steady force in a fixed direction gives a parabola; a force that always points sideways to the motion gives a circle.

**Orbits are stranger still.** On Gemini 4 in 1965, the crew tried to fly towards a spent rocket stage by thrusting straight at it, and watched it drift away; Jim McDivitt used nearly half his manoeuvring fuel before giving up. In orbit, thrusting forwards raises you into a higher orbit, where you go round more slowly. The intuition that you go where you push fails even more badly there.
