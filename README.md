# Mind your misconceptions

Short physics questions that reveal the misconceptions we all carry. Each entry opens with a multiple choice question; only after answering does the reader see the misconception named, why it is tempting, a better picture, classroom ideas, everyday sightings, and a "Going deeper" extension.

Written for science teachers first, and for advanced students as extension.

## Files

- `entries/` one Markdown file per question. The file name is the entry's web address (`#swimmer-and-current`).
- `figures/` SVG figures, inlined into the page at build time. Colour them with the classes defined in `template.html` (`water`, `route`, `hull`, `wire` and so on) so they follow light and dark mode.
- `template.html` the page design and behaviour.
- `build.py` turns the entries into `index.html`. Run `python3 build.py` after any change.
- `index.html` the built page: one self-contained file, ready for GitHub Pages.

## Writing an entry

```
---
title: Neutral title that doesn't give the answer away
order: 4
misconception: The misconception, stated as people hold it
tagline: One sentence on the better idea.
topic: Motion and forces
levels: junior, senior
keywords: words for the search box (not shown)
credit: Optional line shown at the end.
related: other-entry-id, another-entry-id
vault: Name of the source note in the Physics vault (not shown)
---

## Question
Text, lists, $maths$ and figures: ![alt text](figures/name.svg "Optional caption")

## Option
Answer text, or a figure.

> Feedback shown under this option after answering.

## Option (correct)
...

## Why it's tempting
## A better picture
## In the classroom
## Spotted in the wild
## Going deeper
```

### Writing the options

Only physics should lead to the right answer: never the form of the options, and never a trick.

- Keep options similar in length. The build warns if the correct one is clearly the longest or the shortest.
- Give every option the same grammatical shape and register: if one option gives a reason, they all do.
- Balance hedges and absolutes. Don't let the only "roughly" or "almost" belong to the correct option, or the only "exactly" or "never" to a distractor.
- Don't let the correct option be the only one that rejects the question's premise.
- Put the explanation in the feedback, not in the correct option.
- Every distractor should be a wrong idea people genuinely hold, not filler. Three good options beat four with a weak one.
- Vary which letter is correct across entries.
- Keep the title and the file name neutral: both are visible before answering (the file name becomes the page address), so neither should echo the answer or steer towards a distractor.

Supported Markdown: paragraphs, `- ` lists, `**bold**`, `*italic*`, `[links](url)`, `[[entry-id]]` links to other entries, `### headings`, simple `| tables |`, `$inline$` and `$$display$$` maths (KaTeX).

Levels: `junior` is Years 7 to 10, `senior` is Years 11 to 13.

## Previewing

`python3 -m http.server 8765` in this folder, then open http://localhost:8765. Opening `index.html` directly also works.
