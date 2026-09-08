---
name: update-event-tiles
description: Update Canberra Data Week event tiles in index.html, including card copy, status, metadata, details dialogs, and registration links. Use for requests to add, revise, confirm, or link an event in the Events program while keeping tiles visually consistent and accessible.
---

# Update Event Tiles

Keep event cards concise and make confirmed event interactions match the established Microsoft event pattern.

## Workflow

1. Read `index.html` around `.events-grid`, the existing event dialogs, their CSS, and their JavaScript handlers.
2. Find the requested card by its heading. Treat the Microsoft event card and dialog as the canonical interaction pattern.
3. Keep card content compact:
   - Use an `article.event-card`, not an anchor around the full card.
   - Add `event-card--interactive`, `role="button"`, `tabindex="0"`, `aria-haspopup="dialog"`, and `aria-controls` only when a details dialog exists.
   - Shorten dates in card metadata, such as `30 Sept`; put the complete date in the dialog.
   - Use a brief description that is visually comparable to nearby cards.
   - End interactive cards with `View event details` and the existing arrow markup.
4. Put full event information in a `dialog.mailing-dialog.event-dialog`:
   - Give the dialog and title unique IDs and connect them with `aria-labelledby`.
   - Include only confirmed date, time, venue, and description details. Do not invent missing information.
   - Place external booking URLs on a clear primary button inside the dialog, using `target="_blank" rel="noopener noreferrer"`.
5. Wire the card and dialog consistently with existing JavaScript:
   - Open on click, Enter, or Space.
   - Close from the close button, backdrop, or Escape.
   - Use unique `data-open-*` and `data-close-*` attributes.
6. Reuse existing classes before adding CSS. Add narrowly scoped dialog styles only when the supplied content needs them.

## Validation

- Run `git diff --check`.
- Parse `index.html` and verify the trigger, `aria-controls`, dialog ID, close control, and booking URL agree.
- Extract inline JavaScript and run `node --check` on it.
- For a perceptible UI change, serve the site locally and capture a screenshot when browser tooling is available. Check desktop and narrow layouts, card heights, wrapping, hover state, focus state, dialog content, and registration button.
- Confirm the full card does not become a hyperlink; the site-wide `a:hover` rule underlines links.
