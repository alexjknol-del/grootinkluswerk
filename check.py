# -*- coding: utf-8 -*-
"""Controleert de gebouwde site in dist/ op fouten die bezoekers of zoekmachines raken."""
import os
import re
import sys
from collections import Counter

DIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist')

EIGEN_HOST = 'grootinkluswerk.nl'
TOEGESTANE_HOSTS = {'www.kleine-klussen.nl'}
TOEGESTANE_ANKERS = {
    'kleine-klussen.nl',
    'Kleine-Klussen.nl',
    'https://www.kleine-klussen.nl/',
    'www.kleine-klussen.nl',
}
AANSPREEK = ['je', 'jij', 'jou', 'jouw', 'jullie', 'uw', 'we', 'wij', 'ons', 'onze']
DUMMY = ['lorem ipsum', 'placeholder', 'tekst volgt', 'nog invullen', 'todo', 'xxx',
         'voorbeeldtekst', 'vul hier', 'dummy']

fouten = []
waarschuwingen = []


def lees(pad):
    with open(pad, encoding='utf-8') as fh:
        return fh.read()


def strip_tags(h):
    h = re.sub(r'<script.*?</script>', ' ', h, flags=re.S)
    h = re.sub(r'<style.*?</style>', ' ', h, flags=re.S)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = h.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&copy;', '(c)')
    return re.sub(r'\s+', ' ', h)


bestanden = []
for wortel, _dirs, namen in os.walk(DIST):
    for naam in namen:
        if naam.endswith('.html'):
            bestanden.append(os.path.join(wortel, naam))

paden = set()
for pad in bestanden:
    rel = os.path.relpath(pad, DIST)
    if rel == '404.html':
        continue
    url = '/' + rel.replace('index.html', '')
    url = url.replace(os.sep, '/')
    paden.add(url if url.endswith('/') else url + '/')

videos = {}
titels = Counter()
descripties = Counter()
inkomend = Counter()

for pad in sorted(bestanden):
    rel = os.path.relpath(pad, DIST)
    h = lees(pad)
    tekst = strip_tags(h)

    # meta
    t = re.search(r'<title>(.*?)</title>', h, re.S)
    if not t:
        fouten.append('%s: geen title' % rel)
    else:
        titel = t.group(1).strip()
        titels[titel] += 1
        if len(titel) > 65:
            waarschuwingen.append('%s: title %d tekens: %s' % (rel, len(titel), titel))
        if len(titel) < 20:
            waarschuwingen.append('%s: title kort (%d)' % (rel, len(titel)))

    d = re.search(r'<meta name="description" content="(.*?)">', h, re.S)
    if not d:
        fouten.append('%s: geen meta description' % rel)
    else:
        desc = d.group(1).strip()
        descripties[desc] += 1
        if not (90 <= len(desc) <= 175):
            waarschuwingen.append('%s: description %d tekens' % (rel, len(desc)))

    if '<link rel="canonical"' not in h:
        fouten.append('%s: geen canonical' % rel)

    n_h1 = len(re.findall(r'<h1[ >]', h))
    if n_h1 != 1:
        fouten.append('%s: %d h1-elementen' % (rel, n_h1))

    # dubbele id
    ids = re.findall(r'\sid="([^"]+)"', h)
    dubbel = [i for i, c in Counter(ids).items() if c > 1]
    if dubbel:
        fouten.append('%s: dubbele id %s' % (rel, dubbel))

    # afbeeldingen
    for img in re.findall(r'<img[^>]*>', h):
        if 'alt=' not in img:
            fouten.append('%s: img zonder alt' % rel)

    # streepjes en emoji
    for teken, naam in (('—', 'em-dash'), ('–', 'en-dash')):
        if teken in tekst:
            fouten.append('%s: %s in de tekst' % (rel, naam))
    if re.search(r'[\U0001F300-\U0001FAFF☀-➿]', tekst):
        fouten.append('%s: emoji in de tekst' % rel)

    # dummytekst
    lower = tekst.lower()
    for term in DUMMY:
        if term in lower:
            fouten.append('%s: dummytekst "%s"' % (rel, term))

    # aanspreekvormen
    for woord in AANSPREEK:
        if re.search(r'(?<![\w-])%s(?![\w-])' % woord, lower):
            hit = re.search(r'.{0,45}(?<![\w-])%s(?![\w-]).{0,45}' % woord, lower)
            fouten.append('%s: aanspreekvorm "%s" -> %s' % (rel, woord, hit.group(0).strip()))
    if re.search(r'(?<![\w-])u(?![\w-])', tekst):
        hit = re.search(r'.{0,45}(?<![\w-])u(?![\w-]).{0,45}', tekst)
        fouten.append('%s: aanspreekvorm "u" -> %s' % (rel, hit.group(0).strip()))


    # geen externe bronnen in de opgeleverde html
    for m in re.finditer(r'\s(?:src|srcset|data-src)="(https?://[^"]+)"', h):
        fouten.append('%s: externe bron in de html: %s' % (rel, m.group(1)))
    for m in re.finditer(r'<link[^>]+href="(https?://[^"]+)"', h):
        if not m.group(1).startswith('https://%s' % EIGEN_HOST):
            fouten.append('%s: externe stylesheet of link: %s' % (rel, m.group(1)))

    # videoblokken
    for m in re.finditer(r'data-video="([^"]*)"', h):
        vid = m.group(1)
        videos.setdefault(vid, []).append(rel)
        if not re.fullmatch(r'[A-Za-z0-9_-]{11}', vid):
            fouten.append('%s: ongeldig video-id %r' % (rel, vid))
    if 'data-video=' in h and 'youtube-nocookie.com/embed/' not in h:
        fouten.append('%s: videoblok zonder afspeelscript' % rel)
    if 'data-video=' in h and '<iframe' in h:
        fouten.append('%s: iframe staat al in de html, video laadt dus zonder klik' % rel)

    # links
    for m in re.finditer(r'<a\s([^>]*)>(.*?)</a>', h, re.S):
        attrs, label = m.group(1), strip_tags(m.group(2)).strip()
        href = re.search(r'href="([^"]*)"', attrs)
        href = href.group(1) if href else ''
        if not href:
            fouten.append('%s: link zonder href' % rel)
            continue
        if not label:
            fouten.append('%s: lege ankertekst bij %s' % (rel, href))
        if href.startswith('http'):
            host = re.sub(r'^https?://([^/]+).*$', r'\1', href)
            if host not in TOEGESTANE_HOSTS:
                fouten.append('%s: externe host niet toegestaan: %s' % (rel, host))
            if 'nofollow' not in attrs or 'noopener' not in attrs:
                fouten.append('%s: externe link zonder nofollow noopener: %s' % (rel, href))
            if label not in TOEGESTANE_ANKERS:
                fouten.append('%s: ankertekst niet toegestaan: "%s"' % (rel, label))
        elif href.startswith(('mailto:', 'tel:', '#')):
            continue
        else:
            doel = href.split('#')[0]
            if doel.endswith(('.css', '.svg', '.xml', '.txt')):
                continue
            if not doel.startswith('/'):
                fouten.append('%s: relatieve link %s' % (rel, href))
                continue
            if doel not in paden:
                fouten.append('%s: kapotte interne link %s' % (rel, doel))
            else:
                inkomend[doel] += 1

for vid, paden_ in videos.items():
    if len(paden_) > 1:
        waarschuwingen.append('video %s staat op meerdere pagina\'s: %s' % (vid, paden_))

for titel, n in titels.items():
    if n > 1:
        fouten.append('dubbele title (%dx): %s' % (n, titel))
for desc, n in descripties.items():
    if n > 1:
        fouten.append('dubbele description (%dx): %s' % (n, desc[:60]))

for p in sorted(paden):
    if p != '/' and inkomend[p] == 0:
        fouten.append('verweesde pagina zonder interne link: %s' % p)

# sitemap
sm = lees(os.path.join(DIST, 'sitemap.xml'))
in_sm = set(re.findall(r'<loc>https://[^/]+(/[^<]*)</loc>', sm))
ontbreekt = paden - in_sm
overbodig = in_sm - paden
if ontbreekt:
    fouten.append('ontbreekt in sitemap: %s' % sorted(ontbreekt))
if overbodig:
    fouten.append('staat ten onrechte in sitemap: %s' % sorted(overbodig))

print('%d html-bestanden gecontroleerd, %d unieke url\'s, %d video\'s'
      % (len(bestanden), len(paden), len(videos)))
if waarschuwingen:
    print('\nWaarschuwingen (%d):' % len(waarschuwingen))
    for w in waarschuwingen:
        print('  ' + w)
if fouten:
    print('\nFOUTEN (%d):' % len(fouten))
    for f in fouten:
        print('  ' + f)
    sys.exit(1)
print('\nGeen fouten gevonden.')
