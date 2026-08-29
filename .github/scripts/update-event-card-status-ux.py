from pathlib import Path

path = Path('index.html')
text = path.read_text()

# CSS: make all interactive event cards share the same hover/focus treatment and add date/status/action styles.
css_old = ".event-card:hover { box-shadow: var(--shadow-md); transform: translateY(-2px); }\n"
css_new = ".event-card:hover { box-shadow: var(--shadow-md); transform: translateY(-2px); }\n.event-card--interactive { cursor: pointer; transition: transform .15s, box-shadow .15s, border-color .15s; }\n.event-card--interactive:hover { border-color: var(--cdw-teal); }\n.event-card--interactive:focus-visible { outline: 3px solid rgba(0,180,216,.35); outline-offset: 3px; border-color: var(--cdw-teal); }\n.event-card__date { font-size: .78rem; font-weight: 800; letter-spacing: .02em; color: var(--cdw-purple); }\n.event-card__action { display: inline-flex; align-items: center; gap: 8px; margin-block-start: 4px; color: var(--cdw-purple); font-size: .82rem; font-weight: 700; }\n.event-card__action-arrow { display: inline-block; transition: transform .15s; }\n.event-card--interactive:hover .event-card__action-arrow,\n.event-card--interactive:focus-visible .event-card__action-arrow { transform: translateX(4px); }\n.event-card__status--confirmed::before { color: var(--cdw-turquoise); }\n.event-card__status--host::before { color: var(--cdw-orange); }\n"
text = text.replace(css_old, css_new, 1)

# Microsoft confirmed card. Keep existing modal trigger and add visible date before title.
text = text.replace(
'''      <article class="event-card event-card--interactive" data-type="panel" role="button" tabindex="0" aria-haspopup="dialog" aria-controls="microsoft-event-dialog" data-open-microsoft-event>\n        <div class="event-card__meta">\n          <span class="tag tag--panel">Panel</span>\n          <span class="tag tag--venue">Microsoft Canberra &middot; Anchor Event</span>\n        </div>\n        <h3>Opening Event: Data and the Future of Public Services</h3>''',
'''      <article class="event-card event-card--interactive" data-type="panel" role="button" tabindex="0" aria-haspopup="dialog" aria-controls="microsoft-event-dialog" data-open-microsoft-event>\n        <div class="event-card__meta">\n          <span class="tag tag--panel">Panel</span>\n          <span class="tag tag--venue">Microsoft Canberra &middot; Anchor Event</span>\n        </div>\n        <p class="event-card__date">TUE 29 SEP · 10:00 AM–2:40 PM</p>\n        <h3>Opening Event: Data and the Future of Public Services</h3>''',1)
text = text.replace('<p class="event-card__status">Confirmed</p>\n        <span class="event-card__action" aria-hidden="true">View event details <span class="event-card__action-arrow">&rarr;</span></span>', '<p class="event-card__status event-card__status--confirmed">Confirmed</p>\n        <span class="event-card__action" aria-hidden="true">View event details <span class="event-card__action-arrow">&rarr;</span></span>', 1)

# Turn every remaining event card into a host opportunity that opens the Get Involved modal.
start = text.index('      <article class="event-card" data-type="walk">')
end = text.index('    </div>\n\n    <div class="events-cta">', start)
section = text[start:end]
section = section.replace('<article class="event-card"', '<article class="event-card event-card--interactive" role="button" tabindex="0" data-open-host-form')

# Standardize status copy and add explicit action. Preserve any known venue text. No confirmed dates are invented.
section = section.replace('<p class="event-card__status">Open to Partner Hosts</p>', '<p class="event-card__status event-card__status--host">Host opportunity</p>\n        <span class="event-card__action" aria-hidden="true">Interested in hosting this? <span class="event-card__action-arrow">&rarr;</span></span>')
section = section.replace('<p class="event-card__status event-card__status--open">Apply to Host</p>', '<p class="event-card__status event-card__status--host">Host opportunity</p>\n        <span class="event-card__action" aria-hidden="true">Interested in hosting this? <span class="event-card__action-arrow">&rarr;</span></span>')

# Add Date TBC immediately before each unconfirmed event title.
section = section.replace('        <h3>', '        <p class="event-card__date">DATE TBC</p>\n        <h3>')
text = text[:start] + section + text[end:]

path.write_text(text)
