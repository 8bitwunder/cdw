from pathlib import Path

path = Path('index.html')
text = path.read_text()
old = ".event-dialog{inline-size:min(760px,calc(100% - 32px))}.event-dialog__body{padding:0 30px 30px}.event-dialog__details{display:flex;flex-wrap:wrap;gap:8px 18px;margin-block:4px 22px;color:var(--grey-600);font-size:.88rem}.event-dialog__agenda{display:grid;gap:0;margin-block:8px 26px;border-block-start:1px solid var(--grey-200)}"
new = ".event-dialog{inline-size:min(760px,calc(100% - 32px));overflow:hidden;display:flex;flex-direction:column}.event-dialog .mailing-dialog__header{flex:0 0 auto}.event-dialog__body{padding:0 30px 30px;display:flex;flex-direction:column;min-block-size:0;overflow:hidden}.event-dialog__details{display:flex;flex-wrap:wrap;gap:8px 18px;margin-block:4px 22px;color:var(--grey-600);font-size:.88rem}.event-dialog__agenda{display:grid;gap:0;margin-block:8px 26px;border-block-start:1px solid var(--grey-200);overflow-y:auto;max-block-size:min(44dvh,420px);overscroll-behavior:contain;padding-inline-end:8px}"
if old not in text:
    raise SystemExit('Target event dialog CSS not found')
path.write_text(text.replace(old, new, 1))

# Triggered as a one-shot patch for PR 12.
