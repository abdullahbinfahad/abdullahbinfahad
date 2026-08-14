# Schedule Dashboard Design Directions

## Approach 1 — Campus Field Notes
**Very Brief Intro:** A sunlit academic planner that feels like a beautifully annotated studio notebook: ivory paper, ink-blue navigation, and bright color tabs. It conveys calm control without becoming sterile.

**Probability:** 0.07

## Approach 2 — Transit Board Reframed
**Very Brief Intro:** A crisp wayfinding-inspired timetable with route colors, clear time rails, and operational visual language. It makes the week feel navigable, immediate, and dependable.

**Probability:** 0.04

## Approach 3 — Chromatic Study Room
**Very Brief Intro:** A soft, playful schedule experience using layered cards, pastel paper textures, and color as a memory cue. It is friendly and lively, but still organized enough for day-to-day planning.

**Probability:** 0.09

# Chosen Direction — Campus Field Notes

## Design Movement
Contemporary editorial stationery with the operational clarity of university wayfinding. The interface should resemble an intelligent academic field notebook rather than a generic productivity dashboard.

## Core Principles
1. Make the current day unmistakable through a large day marker, vertical time rail, and course-color identifiers.
2. Use color as a reliable scheduling language: one subject has one durable identity, while neutral paper backgrounds allow details to breathe.
3. Frame actions as physical planning tools—date tabs, clipped notes, and calendar controls—rather than anonymous interface chrome.
4. Let the layout read in a natural sequence: date and status first, classes second, supporting planning tools third.

## Color Philosophy
The base is warm paper and graphite ink, evoking a well-used academic notebook. Course colors are saturated but softened by pale tints: cobalt for computation, coral for mathematics, forest green for culture, lilac for language, and amber for circuit study. Color indicates function, not decoration, and must remain legible in every contrast state.

## Layout Paradigm
An asymmetric desk-like composition. A narrow permanent rail handles brand, date navigation, and week overview. The main canvas centers a tall “today” timetable on a time rail. A right planning strip surfaces location, next-class, and reminder tools. On small displays, the rail condenses into a top field notebook header and the planning strip folds below the schedule.

## Signature Elements
1. A vertical timeline with clipped color labels and small period markers.
2. Offset paper cards with a thin ink border, short shadow, and a colored binding edge tied to the course.
3. A warm “week ribbon” that moves with date search and marks the currently selected weekday.

## Interaction Philosophy
Every action should answer a planning question quickly. Date controls immediately redraw the appropriate day. Clicking a course exposes detailed information without leaving the schedule. Reminder controls are explicit, local, and honest about browser support. Filter and search controls alter the displayed agenda without hiding the selected date.

## Animation
Use quick, low-distraction paper-motion transitions: schedule cards enter with a 160–240 ms opacity and upward movement; date changes slide the content 10–14 px in the direction of navigation; class selection uses a subtle colored outline rather than a bounce. Motion is disabled for reduced-motion preferences. Buttons use a 0.97 press scale and no animation delays longer than 300 ms.

## Typography System
Use **DM Sans** for all functional reading and controls, paired with **Fraunces** as the expressive day/date and page-title voice. Titles carry weight and slightly condensed line height; course names use DM Sans 700; metadata uses a high-legibility 13–14 px regular style. Avoid default sans-only hierarchy and never use Inter.

## Brand Essence
**A daily academic command center for students who want every class, room, and reminder arranged at a glance.**

Personality: **assured, bright, considered**.

## Brand Voice
Headlines are observational and specific, while actions are concise and practical. Avoid generic encouragement or productivity clichés.

Example headline: “Your Tuesday begins at Duxue A 204.”

Example action: “Set a 20-minute leave reminder.”

## Wordmark & Logo
The mark is an offset square notebook tab intersected by a small circular location pin—an abstract “S” path appears in the negative space. The wordmark uses a strong but personable serif treatment for “Syllabus” with a restrained sans-serif “daily” descriptor.

## Signature Brand Color
**Library Cobalt — #275EDE.** It signals focus, navigation, and technology without defaulting to a generic corporate-blue interface.

## Style Decisions
- The headline must report the day’s actual academic situation—next course, room, time, or a genuine clear gap—rather than offer generic encouragement.
- The week ribbon is a signature strip of physical paper tabs: the selected day lifts into Library Cobalt, while surrounding days resemble annotated ivory index labels.
- Planner actions use clipped corners, stamped labels, and paper-dividing rules to reinforce a stationery toolset rather than standard SaaS control surfaces.
- The right strip is intentionally editorial: the next class is the urgent note, rooms are route cards, and the planner note is a captured-notebook surface.

## Reference-led redesign

The supplied reference is now the ground-truth specification. The redesign will use its clean, full-width timetable structure: a single concise identity row, a date control row, an explicit Daily/Weekly switch, a daily list with strong horizontal information bands, and a weekly graph grid. The implementation will preserve that simplicity while differentiating subjects through soft modern color fields, small geometric markers, and compact course-code/credit pills. No decorative hero area, oversized navigation rail, or secondary dashboard column will remain.

## Style Decisions

- The full-width reference structure is rendered as an academic field notebook: warm ivory paper, graphite rules, clipped planning surfaces, and purposeful color bindings replace neutral SaaS chrome.
- The header uses the Syllabus daily identity system: an offset notebook-tab/pin symbol, a serif-led “Syllabus” wordmark, restrained “daily” label, and a factual semester line with the verified 10-course, 28-credit total.
- Headings use Fraunces for an editorial academic voice, while DM Sans carries course names, metadata, and controls. The daily heading reports the actual next class, room, and time rather than generic productivity copy.
- Library Cobalt is reserved for navigation and principal actions; subject colors remain a consistent course-language across card edges, week pills, and weekly graph boxes.
