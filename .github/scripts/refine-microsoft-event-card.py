from pathlib import Path

p = Path('index.html')
text = p.read_text()

old_css = ".event-card--interactive { cursor: pointer; transition: transform .15s, box-shadow .15s; }\n.event-card--interactive:hover { transform: translateY(-2px); box-shadow: var(--shadow-md); }\n.event-card--interactive:focus-visible { outline: 3px solid rgba(0,180,216,.35); outline-offset: 3px; }"
new_css = ".event-card--interactive { cursor: pointer; transition: transform .15s, box-shadow .15s, border-color .15s; }\n.event-card--interactive:hover { transform: translateY(-2px); box-shadow: var(--shadow-md); border-color: var(--cdw-teal); }\n.event-card--interactive:focus-visible { outline: 3px solid rgba(0,180,216,.35); outline-offset: 3px; border-color: var(--cdw-teal); }\n.event-card__action { display: inline-flex; align-items: center; gap: 8px; margin-block-start: 8px; color: var(--cdw-purple); font-size: .88rem; font-weight: 700; }\n.event-card__action-arrow { display: inline-block; transition: transform .15s; }\n.event-card--interactive:hover .event-card__action-arrow,\n.event-card--interactive:focus-visible .event-card__action-arrow { transform: translateX(4px); }"
if text.count(old_css) != 1:
    raise SystemExit(f'Expected one interactive CSS block, found {text.count(old_css)}')
text = text.replace(old_css, new_css, 1)

old_card = '''        <p>Hear Canberra's data leaders reveal how government and industry are transforming citizen services, then put your questions to the panel. Save your seat for the event that launches the week.</p>\n        <p class="event-card__status">Confirmed &middot; View agenda</p>'''
new_card = '''        <p>Hear Canberra's data leaders reveal how government and industry are transforming citizen services, then put your questions to the panel. Save your seat for the event that launches the week.</p>\n        <p class="event-card__status">Confirmed</p>\n        <span class="event-card__action" aria-hidden="true">View event details <span class="event-card__action-arrow">&rarr;</span></span>'''
if text.count(old_card) != 1:
    raise SystemExit(f'Expected one Microsoft card action block, found {text.count(old_card)}')
text = text.replace(old_card, new_card, 1)

p.write_text(text)
