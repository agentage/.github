# Brand asset generators

Sources for the org/LinkedIn brand assets (dark-galaxy: `#0a0e17` bg, amber `#f5a623`, blue accent `#5b9bef`).
Deps: `python3`, `rsvg-convert`, ImageMagick `convert`, headless Chrome.

## Plexus banner (1774x444, LinkedIn personal banner / org header bg)

```sh
python3 plexus.py > plexus.svg
rsvg-convert -w 3548 -h 888 plexus.svg | convert - -resize 1774x444 plexus-bg.png
```

Seeded (`SEED = 7`) so layouts are reproducible. Density is left-weighted and fades right; `LEFT_INSET` keeps the far-left from over-crowding.

## Org profile header (`../profile/assets/banner.png`)

`header.html` overlays the lockup (mark + wordmark + tagline) on `plexus-bg.png`:

```sh
google-chrome --headless=new --disable-gpu --no-sandbox --allow-file-access-from-files \
  --force-device-scale-factor=2 --window-size=1774,444 --screenshot=header-raw.png header.html
convert header-raw.png -resize 1774x444 banner.png
```

## LinkedIn company cover (1128x191)

Same recipe with `cover.html` and `--window-size=1128,191`.

## Icons

- `logo-fullbleed.svg` - full-bleed amber square (LinkedIn company logo; upload 400x400, LinkedIn rounds its own container).
- `icon-dark.svg` - dark-bg amber A-arrow with bloom (group-logo slot, shrinks to 92x92; also `../profile/assets/icon-dark.png`).

```sh
rsvg-convert -w 400 -h 400 icon-dark.svg > icon-dark.png
```

`mark.png` is the rounded product mark derived from the landing repo's `packages/landing/public/logo.png` - the canonical logo source; copy from there, don't re-derive. Inter woff2 subsets included so the HTML renders offline.
