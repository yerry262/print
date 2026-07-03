# print

Print-ready sales collateral for the helicopter-pilot **helmet** outreach
(companion to [`heli-bizz`](https://github.com/yerry262/heli-bizz), which builds
the operator/EMS lead list).

Everything here is self-contained HTML that prints cleanly to US-Letter PDF —
no design software needed. Open a sheet in Chrome and use **Print → Save as PDF**.

## Layout

- `sheets/sell-sheet.html` — one-page product sell sheet (leave-behind / mailer)
- `sheets/spec-sheet.html` — technical spec one-pager
- `serve.py` — serves the repo on http://localhost:8788 and opens the browser
- `.github/workflows/deploy-pages.yml` — publishes the sheets to GitHub Pages

## Quickstart

```bash
python3 serve.py          # opens http://localhost:8788/sheets/
# then in Chrome: Print (Cmd/Ctrl-P) → Save as PDF → Letter, margins: None
```

## Customizing

Each sheet is plain HTML with print CSS (`@media print`, `@page`). Edit the copy,
swap the placeholder logo/photo (embed as a `data:` URI to stay self-contained),
and adjust the accent color in the `:root` variables at the top of each file.
