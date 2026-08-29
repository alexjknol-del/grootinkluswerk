# grootinkluswerk.nl

Statische website over grote klussen en verbouwingen. Gebouwd met een Python-generator
zonder dependencies en gehost op Cloudflare Pages.

## Bouwen

```
python3 build.py    # schrijft dist/
python3 check.py    # controleert de gebouwde site
```

## Opbouw

- `build.py` stelt de pagina's samen en bevat de teksten van home, kosten, hulpmiddelen, over, contact en de juridische pagina's
- `sitegen.py` bevat de generator: markdown-subset, sjabloon, sitemap en rss
- `theme.py` bevat de css en het favicon
- `content/klussen.py` bevat de pagina's per type klus
- `content/voorbereiding.py` bevat de pagina's over de voorbereiding
- `content/nieuws.py` bevat de nieuwsartikelen
- `check.py` controleert kapotte links, dubbele meta, aanspreekvormen, streepjes, dummytekst, ankerteksten en de sitemap
- `dist/` is de gebouwde site en staat in de repo, zodat Cloudflare Pages niets hoeft te bouwen

## Cloudflare Pages

Framework preset None, build command leeg, output directory `dist`, production branch `main`.
