"""Minimale statische sitegenerator zonder dependencies."""
import html
import os
import re
import shutil
from datetime import date


# ---------------------------------------------------------------- markdown

def _inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r'\[([^\]]+)\]\(([^)\s]+)(?:\s+"nofollow")?\)',
                  lambda m: _link(m.group(1), m.group(2)), text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    return text


def _link(label, href):
    if href.startswith('http'):
        return ('<a href="%s" rel="nofollow noopener" target="_blank">%s</a>'
                % (href, label))
    return '<a href="%s">%s</a>' % (href, label)


def render(md):
    """Zet een compacte markdown-subset om naar html."""
    out = []
    lines = md.strip('\n').split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        if line.startswith('## '):
            out.append('<h2>%s</h2>' % _inline(line[3:].strip()))
            i += 1
        elif line.startswith('### '):
            out.append('<h3>%s</h3>' % _inline(line[4:].strip()))
            i += 1
        elif line.startswith('> '):
            block = []
            while i < len(lines) and lines[i].startswith('> '):
                block.append(_inline(lines[i][2:].strip()))
                i += 1
            out.append('<div class="kader"><p>%s</p></div>' % '</p><p>'.join(block))
        elif line.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                items.append('<li>%s</li>' % _inline(lines[i][2:].strip()))
                i += 1
            out.append('<ul>%s</ul>' % ''.join(items))
        elif re.match(r'^\d+\. ', line):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                items.append('<li>%s</li>' % _inline(re.sub(r'^\d+\. ', '', lines[i]).strip()))
                i += 1
            out.append('<ol>%s</ol>' % ''.join(items))
        elif line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                rows.append(cells)
                i += 1
            head = rows[0]
            body = [r for r in rows[1:] if not set(''.join(r)) <= set('-: ')]
            thead = ''.join('<th>%s</th>' % _inline(c) for c in head)
            tbody = ''.join(
                '<tr>%s</tr>' % ''.join('<td>%s</td>' % _inline(c) for c in r)
                for r in body)
            out.append('<div class="tabelwrap"><table><thead><tr>%s</tr></thead>'
                       '<tbody>%s</tbody></table></div>' % (thead, tbody))
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(
                    r'^(#{2,3} |- |\d+\. |\||> )', lines[i]):
                para.append(lines[i].strip())
                i += 1
            out.append('<p>%s</p>' % _inline(' '.join(para)))
    return '\n'.join(out)


# ---------------------------------------------------------------- site

class Site:
    def __init__(self, cfg):
        self.cfg = cfg
        self.pages = []

    def add(self, path, title, description, body, h1=None, extra_head='',
            schema=None, nav_group=None, lastmod=None, priority='0.7'):
        self.pages.append(dict(
            path=path, title=title, description=description, body=body,
            h1=h1 or title.split(' |')[0], extra_head=extra_head,
            schema=schema, nav_group=nav_group,
            lastmod=lastmod or self.cfg['builddate'], priority=priority))

    # ------------------------------------------------------------ chrome
    def nav_html(self, current):
        items = []
        for label, href in self.cfg['nav']:
            cls = ' class="actief"' if href == current else ''
            items.append('<li><a href="%s"%s>%s</a></li>' % (href, cls, label))
        return ''.join(items)

    def breadcrumb(self, path, title):
        if path == '/':
            return ''
        parts = [p for p in path.strip('/').split('/') if p]
        crumbs = ['<a href="/">Home</a>']
        acc = ''
        for idx, part in enumerate(parts):
            acc += '/' + part
            label = self.cfg['crumb_labels'].get(acc + '/', part.replace('-', ' ').capitalize())
            if idx == len(parts) - 1:
                crumbs.append('<span>%s</span>' % html.escape(title))
            else:
                crumbs.append('<a href="%s/">%s</a>' % (acc, html.escape(label)))
        return ('<nav class="kruimels" aria-label="Kruimelpad">%s</nav>'
                % ' <span class="sep">/</span> '.join(crumbs))

    def page_html(self, page):
        c = self.cfg
        url = c['base'] + page['path']
        schema = ''
        if page['schema']:
            schema = '<script type="application/ld+json">%s</script>' % page['schema']
        return """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{name}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="{name} nieuws" href="/rss.xml">
<link rel="stylesheet" href="/stijl.css">
{extra}
{schema}
</head>
<body>
<a class="overslaan" href="#hoofd">Naar de inhoud</a>
<header class="kop">
  <div class="binnen kopbalk">
    <a class="merk" href="/">{brandhtml}</a>
    <button class="menuknop" aria-expanded="false" aria-controls="hoofdmenu">Menu</button>
    <nav id="hoofdmenu" aria-label="Hoofdmenu"><ul>{nav}</ul></nav>
  </div>
</header>
<main id="hoofd">
{crumbs}
{body}
</main>
<footer class="voet">
  <div class="binnen voetgrid">
    <div>
      <p class="voetmerk">{name}</p>
      <p>{footerline}</p>
      <p><a href="mailto:{email}">{email}</a></p>
    </div>
    {footercols}
  </div>
  <div class="binnen voetonder">
    <p>&copy; {year} {name}</p>
    <p><a href="/privacybeleid/">Privacybeleid</a> <span class="sep">/</span> <a href="/cookiebeleid/">Cookiebeleid</a> <span class="sep">/</span> <a href="/contact/">Contact</a></p>
  </div>
</footer>
<script>
(function(){{
  var b=document.querySelector('.menuknop'),n=document.getElementById('hoofdmenu');
  if(!b||!n)return;
  b.addEventListener('click',function(){{
    var open=n.classList.toggle('open');
    b.setAttribute('aria-expanded',open?'true':'false');
  }});
}})();
</script>
</body>
</html>
""".format(
            title=html.escape(page['title']),
            desc=html.escape(page['description']),
            url=url,
            name=html.escape(c['name']),
            extra=page['extra_head'],
            schema=schema,
            brandhtml=c['brandhtml'],
            nav=self.nav_html(page['path']),
            crumbs=self.breadcrumb(page['path'], page['h1']),
            body=page['body'],
            footerline=c['footerline'],
            email=c['email'],
            footercols=c['footercols'],
            year=date.today().year,
        )

    # ------------------------------------------------------------ write
    def build(self, outdir='dist'):
        if os.path.isdir(outdir):
            shutil.rmtree(outdir)
        os.makedirs(outdir)
        for page in self.pages:
            if page['path'] == '/404/':
                continue
            rel = page['path'].strip('/')
            target = os.path.join(outdir, rel, 'index.html') if rel else os.path.join(outdir, 'index.html')
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, 'w', encoding='utf-8') as fh:
                fh.write(self.page_html(page))
        # extra bestanden
        with open(os.path.join(outdir, 'stijl.css'), 'w', encoding='utf-8') as fh:
            fh.write(self.cfg['css'])
        with open(os.path.join(outdir, 'favicon.svg'), 'w', encoding='utf-8') as fh:
            fh.write(self.cfg['favicon'])
        with open(os.path.join(outdir, 'robots.txt'), 'w', encoding='utf-8') as fh:
            fh.write('User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % self.cfg['base'])
        with open(os.path.join(outdir, '_headers'), 'w', encoding='utf-8') as fh:
            fh.write('/*\n  X-Content-Type-Options: nosniff\n'
                     '  Referrer-Policy: strict-origin-when-cross-origin\n'
                     '  X-Frame-Options: SAMEORIGIN\n'
                     '  Permissions-Policy: geolocation=(), microphone=(), camera=()\n')
        # sitemap
        urls = []
        for page in sorted(self.pages, key=lambda p: p['path']):
            if page['path'] == '/404/':
                continue
            urls.append('<url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>'
                        % (self.cfg['base'], page['path'], page['lastmod'], page['priority']))
        with open(os.path.join(outdir, 'sitemap.xml'), 'w', encoding='utf-8') as fh:
            fh.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                     '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n'
                     % '\n'.join(urls))
        # 404 op de wortel
        for page in self.pages:
            if page['path'] == '/404/':
                with open(os.path.join(outdir, '404.html'), 'w', encoding='utf-8') as fh:
                    fh.write(self.page_html(page))
        return len(self.pages)

    def rss(self, outdir, items):
        entries = []
        for it in items:
            entries.append(
                '<item><title>%s</title><link>%s%s</link><guid>%s%s</guid>'
                '<pubDate>%s</pubDate><description>%s</description></item>'
                % (html.escape(it['title']), self.cfg['base'], it['path'],
                   self.cfg['base'], it['path'], it['rfc822'],
                   html.escape(it['summary'])))
        xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<rss version="2.0"><channel>\n'
               '<title>%s nieuws</title><link>%s/nieuws/</link>'
               '<description>%s</description><language>nl-nl</language>\n%s\n'
               '</channel></rss>\n'
               % (html.escape(self.cfg['name']), self.cfg['base'],
                  html.escape(self.cfg['rssdesc']), '\n'.join(entries)))
        with open(os.path.join(outdir, 'rss.xml'), 'w', encoding='utf-8') as fh:
            fh.write(xml)
