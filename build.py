# -*- coding: utf-8 -*-
"""Bouwt de statische site grootinkluswerk.nl naar dist/."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sitegen import Site, render
from theme import CSS, FAVICON
from content import klussen as C_KLUS
from content import voorbereiding as C_VOOR
from content import nieuws as C_NIEUWS

BASE = 'https://grootinkluswerk.nl'
NAAM = 'Grootinkluswerk.nl'
EMAIL = 'info@grootinkluswerk.nl'
BOUWDATUM = '2026-08-29'

KK = 'https://www.kleine-klussen.nl/'

NAV = [
    ('Klussen', '/klussen/'),
    ('Voorbereiding', '/voorbereiding/'),
    ('Kosten', '/kosten/'),
    ('Hulpmiddelen', '/hulpmiddelen/'),
    ('Nieuws', '/nieuws/'),
    ('Over', '/over/'),
    ('Contact', '/contact/'),
]

CRUMBS = {
    '/klussen/': 'Klussen',
    '/voorbereiding/': 'Voorbereiding',
    '/kosten/': 'Kosten',
    '/hulpmiddelen/': 'Hulpmiddelen',
    '/nieuws/': 'Nieuws',
}

FOOTERCOLS = """
<div>
  <h4>Grote klussen</h4>
  <ul>
    <li><a href="/klussen/badkamer-verbouwen/">Badkamer verbouwen</a></li>
    <li><a href="/klussen/keuken-plaatsen/">Keuken plaatsen</a></li>
    <li><a href="/klussen/uitbouw-aanbouw/">Uitbouw of aanbouw</a></li>
    <li><a href="/klussen/zolder-verbouwen/">Zolder verbouwen</a></li>
    <li><a href="/klussen/isolatie-woning/">Woning isoleren</a></li>
  </ul>
</div>
<div>
  <h4>Voorbereiding</h4>
  <ul>
    <li><a href="/voorbereiding/offertes-vergelijken/">Offertes vergelijken</a></li>
    <li><a href="/voorbereiding/aannemer-kiezen/">Aannemer kiezen</a></li>
    <li><a href="/voorbereiding/vergunning-en-melding/">Vergunning en melding</a></li>
    <li><a href="/voorbereiding/contract-en-oplevering/">Contract en oplevering</a></li>
    <li><a href="/kosten/">Kosten en budget</a></li>
  </ul>
</div>
<div>
  <h4>Hulpmiddelen</h4>
  <ul>
    <li><a href="/hulpmiddelen/verbouwbudget/">Verbouwbudget berekenen</a></li>
    <li><a href="/hulpmiddelen/opleverchecklist/">Opleverchecklist</a></li>
    <li><a href="/nieuws/">Nieuws</a></li>
    <li><a href="/over/">Over deze gids</a></li>
    <li><a href="/contact/">Contact</a></li>
  </ul>
</div>
"""

CFG = dict(
    base=BASE, name=NAAM, email=EMAIL, builddate=BOUWDATUM,
    brandhtml='Grootinkluswerk<span>.nl</span>',
    nav=NAV, crumb_labels=CRUMBS, css=CSS, favicon=FAVICON,
    footerline='Onafhankelijke gids over grote klussen en verbouwingen in Nederland.',
    footercols=FOOTERCOLS,
    rssdesc='Nieuws over verbouwen, bouwkosten, regelgeving en subsidies.',
)

site = Site(CFG)

MERK_SUFFIX = ' | Grootinkluswerk.nl'


def T(kern):
    """Merkachtervoegsel toevoegen zolang de title kort genoeg blijft."""
    volledig = kern + MERK_SUFFIX
    return volledig if len(volledig) <= 62 else kern



def kk_blok(tekst=None):
    """Het uitgelichte kader met de verwijzing naar Kleine-Klussen.nl."""
    tekst = tekst or (
        'Niet elke klus vraagt om een aannemer. Voor losse klussen als een lamp ophangen, '
        'meubelmontage, een kraan vervangen of een klemmende deur is een vakman per klus of '
        'per uur in te plannen bij Kleine-Klussen.nl. Online een datum en tijdslot kiezen, '
        'daarna komt een vakman uit het netwerk langs.')
    return ('<div class="uitgelicht"><h2>Uitbesteden zonder aannemer</h2><p>%s</p>'
            '<p class="knoprij"><a class="knop" href="%s" rel="nofollow noopener" '
            'target="_blank">Kleine-Klussen.nl</a></p></div>' % (tekst, KK))


def kaart(titel, href, tekst, meta=''):
    m = '<p class="meta">%s</p>' % meta if meta else ''
    return ('<article class="kaart"><h3><a href="%s">%s</a></h3><p>%s</p>%s</article>'
            % (href, titel, tekst, m))


NL_MAAND = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus',
            'september', 'oktober', 'november', 'december']


def nl_datum(iso):
    j, m, d = iso.split('-')
    return '%d %s %s' % (int(d), NL_MAAND[int(m) - 1], j)


# ---------------------------------------------------------------- home
KLUS_KORT = {
    'badkamer-verbouwen': 'Zeven vakgebieden in een vaste volgorde, met de kostenposten en de wachttijden.',
    'keuken-plaatsen': 'Inmeten, groepen in de meterkast, leidingwerk en de levertijd van zes tot twaalf weken.',
    'zolder-verbouwen': 'Vloerbelasting, hoogte, daglicht en de vluchtroute bepalen wat er mogelijk is.',
    'dakkapel-plaatsen': 'Vergunningvrij aan de achterzijde, prefab in een dag, zes tot tien weken vooraf.',
    'uitbouw-aanbouw': 'Fundering, ligger en de vergunningcheck, met kosten per vierkante meter.',
    'muurdoorbraak': 'Hoe blijkt of een wand draagt en wat de constructeur en de gemeente vragen.',
    'vloer-vervangen': 'Ondergrond, egaliseren, vloerverwarming en de geluidseis van de VvE.',
    'isolatie-woning': 'Volgorde op resultaat en de ISDE-bedragen per vierkante meter.',
    'schilderwerk-buiten': 'Onderhoudscyclus, houtrot en het verlaagde btw-tarief op arbeid.',
    'tuin-aanleggen': 'Grondwerk, afschot en drainage bepalen of de bestrating vlak blijft.',
}

VOOR_KORT = {
    'offertes-vergelijken': 'Welke posten erin horen en hoe stelposten vergelijkbaar worden.',
    'aannemer-kiezen': 'Inschrijving, verzekering, referenties en de signalen die op problemen wijzen.',
    'vergunning-en-melding': 'Omgevingsplanactiviteit, technische bouwactiviteit en de check per adres.',
    'planning-en-doorlooptijd': 'Levertijden en uithardingstijden bepalen de doorlooptijd, niet het tempo.',
    'budget-en-onvoorzien': 'De posten die vergeten worden, en hoe groot onvoorzien moet zijn.',
    'contract-en-oplevering': 'Waarschuwingsplicht, betaaltermijnen, opleverlijst en verborgen gebreken.',
    'overlast-en-buren': 'Werktijden, aankondigen, toestemming van de VvE en bouwen op de erfgrens.',
    'zelf-doen-of-uitbesteden': 'Waar de grens ligt bij elektra, gas en constructie.',
}

home_klussen = ''.join(
    kaart(t, '/klussen/%s/' % s, KLUS_KORT[s])
    for s, t, _d, _md in C_KLUS.KLUSSEN[:6])

home_voor = ''.join(
    kaart(t, '/voorbereiding/%s/' % s, VOOR_KORT[s])
    for s, t, _d, _md in C_VOOR.PAGINAS[:6])

home_nieuws = ''.join(
    kaart(t, '/nieuws/%s/' % s, sam, nl_datum(datum))
    for s, datum, _rfc, t, _d, sam, _md in C_NIEUWS.ARTIKELEN[:3])

HOME = """
<section class="hero">
  <div class="binnen">
    <h1>Grote klussen en verbouwingen, van plan tot oplevering</h1>
    <p class="lead">Grootinkluswerk.nl legt uit wat er bij een grote klus komt kijken: de
    volgorde van het werk, de kosten per onderdeel, de vergunningen en de afspraken die
    meerwerk voorkomen. Onafhankelijk, zonder bemiddeling en zonder offerteaanvraag.</p>
    <div class="cijfers">
      <div class="cijfer"><b>5,0%</b><span>hogere bouwkosten woningbouw in juni 2026 dan een jaar eerder, volgens het CBS</span></div>
      <div class="cijfer"><b>8 weken</b><span>reguliere beslistermijn op een omgevingsvergunning, met verlenging tot veertien</span></div>
      <div class="cijfer"><b>10 tot 15%</b><span>post onvoorzien die bij oudere woningen realistisch is</span></div>
    </div>
  </div>
</section>

<section>
  <h2>Klussen per type</h2>
  <p>Per klus de werkzaamheden in volgorde, de doorlooptijd, de kostenposten en de punten
  waarop het in de praktijk misgaat.</p>
  <div class="rooster">{klussen}</div>
  <p><a href="/klussen/">Alle klussen bekijken</a></p>
</section>

<section>
  <h2>Voorbereiding</h2>
  <p>Het grootste deel van de tegenvallers bij een verbouwing ontstaat voordat er gesloopt
  wordt. Deze onderwerpen behandelen de voorbereiding in de volgorde waarin die speelt.</p>
  <div class="rooster">{voorbereiding}</div>
  <p><a href="/voorbereiding/">Alle onderwerpen over voorbereiding</a></p>
</section>

<section>
  {kkblok}
</section>

<section>
  <h2>Zo verloopt een grote klus</h2>
  <ol class="stappen">
    <li><b>Plan en omvang bepalen</b>Vaststellen wat er precies moet gebeuren, welke vakgebieden nodig zijn en of de constructie geraakt wordt.</li>
    <li><b>Vergunning controleren</b>De check per adres op het Omgevingsloket, en bij een appartement toestemming van de vereniging van eigenaars.</li>
    <li><b>Offertes opvragen en vergelijken</b>Drie offertes, met dezelfde stelposten en dezelfde omschrijving, zodat het verschil zichtbaar wordt.</li>
    <li><b>Bestellen wat een levertijd heeft</b>Alles boven vier weken levertijd besteld voordat de eerste sloopdag begint.</li>
    <li><b>Uitvoeren met bufferdagen</b>Twintig procent extra doorlooptijd op de planning van de aannemer.</li>
    <li><b>Opleveren met een lijst</b>Rondgang bij daglicht, alles op de lijst, laatste termijn pas betalen na afhandeling.</li>
  </ol>
</section>

<section>
  <h2>Laatste artikelen</h2>
  <div class="rooster">{nieuws}</div>
  <p><a href="/nieuws/">Alle artikelen</a></p>
</section>

<section>
  <h2>Waarvoor deze gids niet bedoeld is</h2>
  <p>Grootinkluswerk.nl bemiddelt niet, vraagt geen offertes aan en verkoopt geen leads. Er
  staat geen formulier op deze site. Wie contact zoekt, mailt naar
  <a href="mailto:{email}">{email}</a>. Meer daarover staat op <a href="/over/">de
  pagina over deze gids</a>.</p>
</section>
""".format(klussen=home_klussen, voorbereiding=home_voor, nieuws=home_nieuws,
           kkblok=kk_blok(), email=EMAIL)

ORG_SCHEMA = json.dumps({
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": NAAM,
    "url": BASE + "/",
    "inLanguage": "nl-NL",
    "description": "Onafhankelijke gids over grote klussen en verbouwingen in Nederland.",
}, ensure_ascii=False)

site.add('/', T('Grote klussen en verbouwingen, van plan tot oplevering'),
         'Gids over grote klussen: volgorde van het werk, kosten per onderdeel, vergunningen, '
         'planning en de afspraken die meerwerk voorkomen.',
         HOME, h1='Grote klussen en verbouwingen', schema=ORG_SCHEMA, priority='1.0')

# ---------------------------------------------------------------- klussen
klus_index = ('<section class="smal"><h1>Grote klussen</h1>%s</section>'
              '<section><div class="rooster">%s</div></section><section>%s</section>'
              % (render(C_KLUS.INDEX_INTRO),
                 ''.join(kaart(t, '/klussen/%s/' % s, KLUS_KORT[s])
                         for s, t, _d, _md in C_KLUS.KLUSSEN),
                 kk_blok()))

site.add('/klussen/', T('Grote klussen: overzicht per type klus'),
         'Overzicht van grote klussen in en om het huis, met per klus de werkzaamheden, '
         'de doorlooptijd, de kostenposten en de veelgemaakte fouten.',
         klus_index, h1='Grote klussen', priority='0.9')

for slug, titel, desc, md in C_KLUS.KLUSSEN:
    body = ('<section class="smal"><h1>%s</h1>%s%s</section>'
            % (titel, render(md), kk_blok()))
    site.add('/klussen/%s/' % slug, T('%s: werk, kosten en doorlooptijd' % titel),
             desc, body, h1=titel)

# ---------------------------------------------------------------- voorbereiding
voor_index = ('<section class="smal"><h1>Voorbereiding</h1>%s</section>'
              '<section><div class="rooster">%s</div></section>'
              % (render(C_VOOR.INDEX_INTRO),
                 ''.join(kaart(t, '/voorbereiding/%s/' % s, VOOR_KORT[s])
                         for s, t, _d, _md in C_VOOR.PAGINAS)))

site.add('/voorbereiding/', T('Verbouwing voorbereiden: offertes, vergunning en planning'),
         'Alles wat voor de eerste sloopdag geregeld moet zijn: offertes vergelijken, '
         'aannemer kiezen, vergunning controleren, planning en budget.',
         voor_index, h1='Voorbereiding', priority='0.9')

for slug, titel, desc, md in C_VOOR.PAGINAS:
    extra = kk_blok() if slug != 'zelf-doen-of-uitbesteden' else ''
    body = '<section class="smal"><h1>%s</h1>%s%s</section>' % (titel, render(md), extra)
    site.add('/voorbereiding/%s/' % slug, T(titel), desc, body, h1=titel)

# ---------------------------------------------------------------- kosten
KOSTEN_MD = """
Wat een verbouwing kost, hangt af van drie dingen: de omvang van het werk, de staat van wat
eronder zit en het moment waarop de offerte is gemaakt. De bedragen hieronder zijn
indicaties voor een gemiddelde eengezinswoning, exclusief btw tenzij anders vermeld.

## Richtprijzen per klus

| Klus | Indicatie |
| --- | --- |
| Badkamer compleet, 4 tot 6 vierkante meter | 8.000 tot 18.000 euro |
| Keuken plaatsen, arbeid en installatiewerk | 2.000 tot 5.000 euro |
| Zolder tot slaapkamer | 8.000 tot 20.000 euro |
| Prefab dakkapel tot 2,5 meter, geplaatst | 7.000 tot 11.000 euro |
| Uitbouw, per vierkante meter afgewerkt | 2.500 tot 3.800 euro |
| Muurdoorbraak met stalen ligger | 2.800 tot 7.000 euro |
| Vloer vervangen, per vierkante meter | 40 tot 90 euro |
| Buitenschilderwerk woning | 1.800 tot 5.000 euro |
| Dakisolatie binnenzijde, per vierkante meter | 60 tot 120 euro |

## Uurtarieven

| Vakgebied | Tarief per uur |
| --- | --- |
| Klusjesman, algemeen | 45 tot 65 euro |
| Timmerman | 50 tot 75 euro |
| Loodgieter | 55 tot 85 euro |
| Elektricien | 55 tot 85 euro |
| Stukadoor | 50 tot 75 euro |
| Schilder | 45 tot 70 euro |
| Tegelzetter | 50 tot 80 euro |

Voorrijkosten liggen doorgaans tussen 25 en 60 euro. Spoedwerk buiten kantooruren kent een
toeslag van vijftig tot honderd procent.

## Bijkomende kosten

- Ontwerp, tekenwerk en constructieberekening: 5 tot 12 procent van de bouwkosten
- Leges omgevingsvergunning: een percentage van de bouwsom, per gemeente verschillend
- Afvalcontainer: 250 tot 900 euro afhankelijk van maat en aantal wissels
- Asbestinventarisatie bij woningen van voor 1994: 400 tot 800 euro
- Post onvoorzien: 10 tot 15 procent van de bouwkosten

## Btw

Het algemene tarief is 21 procent. Voor schilder-, stukadoors- en isolatiewerk aan woningen
ouder dan twee jaar geldt onder voorwaarden 9 procent over de arbeid. Voorwaarde is een
offerte waarin arbeid en materiaal gescheiden staan. De actuele lijst staat op
https://www.belastingdienst.nl

## Waarom prijzen blijven stijgen

Het CBS meldde over juni 2026 een stijging van vijf procent in de bouwkosten voor
woningbouw ten opzichte van een jaar eerder, met loonkosten als grootste opwaartse kracht.
Een raming van een jaar oud is daarmee geen bruikbare basis meer voor een besluit.

## Subsidie

Voor isolatie, warmtepompen en per 2026 ook voor energiezuinige ventilatie bestaat de ISDE.
Bedragen, minimumoppervlakken en voorwaarden staan op https://www.rvo.nl
"""

site.add('/kosten/', T('Wat kost een verbouwing? Richtprijzen en uurtarieven'),
         'Richtprijzen per klus, uurtarieven per vakgebied, bijkomende kosten, btw-tarieven '
         'en de post onvoorzien bij een verbouwing.',
         '<section class="smal"><h1>Wat kost een verbouwing</h1>%s%s</section>'
         % (render(KOSTEN_MD), kk_blok()), h1='Wat kost een verbouwing', priority='0.9')

# ---------------------------------------------------------------- hulpmiddelen
HULP_INDEX = """
<section class="smal">
<h1>Hulpmiddelen</h1>
<p>Twee hulpmiddelen die volledig in de browser draaien. Er wordt niets opgeslagen en
niets verstuurd.</p>
</section>
<section>
<div class="rooster">
%s
</div>
</section>
""" % (kaart('Verbouwbudget berekenen', '/hulpmiddelen/verbouwbudget/',
             'Bouwkosten, bijkomende kosten en post onvoorzien in een keer doorgerekend.')
       + kaart('Opleverchecklist', '/hulpmiddelen/opleverchecklist/',
               'Punt voor punt langs het werk voordat de laatste termijn betaald wordt.'))

site.add('/hulpmiddelen/', T('Hulpmiddelen: verbouwbudget en opleverchecklist'),
         'Verbouwbudget berekenen en een opleverchecklist doorlopen. Beide werken volledig '
         'in de browser, zonder opslag.',
         HULP_INDEX, h1='Hulpmiddelen', priority='0.8')

BUDGET_TOOL = """
<section class="smal">
<h1>Verbouwbudget berekenen</h1>
<p>Deze rekenhulp zet de bouwkosten om in een totaalbudget, inclusief de posten die het
vaakst vergeten worden. De uitkomst is een indicatie op basis van gangbare percentages,
geen offerte.</p>

<div class="tool">
  <label for="bouwsom">Geschatte bouwkosten, aanneemsom in euro</label>
  <input type="number" id="bouwsom" value="40000" min="0" step="500">

  <label for="ontwerp">Ontwerp, tekenwerk en constructie</label>
  <select id="ontwerp">
    <option value="0">Niet nodig, geen tekening of berekening</option>
    <option value="0.05">Beperkt, alleen een constructieberekening (5 procent)</option>
    <option value="0.09" selected>Tekening en berekening (9 procent)</option>
    <option value="0.12">Ontwerp, tekening, berekening en begeleiding (12 procent)</option>
  </select>

  <label for="vergunning">Vergunning en leges</label>
  <select id="vergunning">
    <option value="0" selected>Vergunningvrij</option>
    <option value="0.03">Vergunningplichtig, leges circa 3 procent van de bouwsom</option>
    <option value="0.05">Vergunningplichtig in een complexe situatie, circa 5 procent</option>
  </select>

  <label for="onvoorzien">Post onvoorzien</label>
  <select id="onvoorzien">
    <option value="0.10">Woning na 1990, 10 procent</option>
    <option value="0.12" selected>Woning tussen 1970 en 1990, 12 procent</option>
    <option value="0.15">Woning van voor 1970, 15 procent</option>
  </select>

  <label for="extra">Container, opslag en tijdelijke huisvesting in euro</label>
  <input type="number" id="extra" value="600" min="0" step="50">

  <div class="uitkomst" id="uitkomst" aria-live="polite"></div>
  <p class="let">De berekening draait in de browser. Er wordt niets opgeslagen en niets
  verstuurd. Percentages zijn gangbare praktijkwaarden en geen norm.</p>
</div>

<h2>Toelichting per post</h2>
<p>De aanneemsom is het bedrag dat de aannemer offreert voor het werk zelf. Daar komen
kosten bij die niet in die offerte staan.</p>
<ul>
<li><strong>Ontwerp en berekening.</strong> Een constructieberekening kost 500 tot 1.500 euro. Bij een uitbouw of een ingrijpende verbouwing komen tekenwerk en soms begeleiding daarbovenop.</li>
<li><strong>Leges.</strong> Gemeenten rekenen een percentage van de bouwsom. Dat percentage verschilt per gemeente en staat in de legesverordening.</li>
<li><strong>Onvoorzien.</strong> Bedoeld voor wat achter de wand tevoorschijn komt, niet voor keuzes die tijdens het werk duurder uitvallen.</li>
<li><strong>Overig.</strong> Afvalcontainer, opslag van inboedel en eventueel tijdelijke huisvesting.</li>
</ul>
<p>Meer achtergrond staat op <a href="/voorbereiding/budget-en-onvoorzien/">budget en
onvoorzien</a> en op <a href="/kosten/">wat kost een verbouwing</a>.</p>
</section>
"""

BUDGET_SCRIPT = """<script>
(function(){
  var v=function(id){return parseFloat(document.getElementById(id).value)||0;};
  var euro=function(n){return n.toLocaleString('nl-NL',{style:'currency',currency:'EUR',maximumFractionDigits:0});};
  function reken(){
    var bouw=v('bouwsom');
    var ontwerp=bouw*parseFloat(document.getElementById('ontwerp').value);
    var leges=bouw*parseFloat(document.getElementById('vergunning').value);
    var onv=bouw*parseFloat(document.getElementById('onvoorzien').value);
    var extra=v('extra');
    var totaal=bouw+ontwerp+leges+onv+extra;
    document.getElementById('uitkomst').innerHTML=
      '<b>'+euro(totaal)+'</b>'+
      '<p>Bouwkosten '+euro(bouw)+'<br>'+
      'Ontwerp en berekening '+euro(ontwerp)+'<br>'+
      'Vergunning en leges '+euro(leges)+'<br>'+
      'Onvoorzien '+euro(onv)+'<br>'+
      'Container, opslag en huisvesting '+euro(extra)+'</p>';
  }
  ['bouwsom','ontwerp','vergunning','onvoorzien','extra'].forEach(function(id){
    var el=document.getElementById(id);
    el.addEventListener('input',reken);el.addEventListener('change',reken);
  });
  reken();
})();
</script>"""

site.add('/hulpmiddelen/verbouwbudget/', T('Verbouwbudget berekenen'),
         'Rekenhulp die bouwkosten omzet in een totaalbudget, inclusief ontwerp, leges, '
         'onvoorzien en bijkomende kosten. Draait volledig in de browser.',
         BUDGET_TOOL + BUDGET_SCRIPT, h1='Verbouwbudget berekenen')

OPLEVER = """
<section class="smal">
<h1>Opleverchecklist</h1>
<p>Bij de oplevering wordt het werk aanvaard. Artikel 7:758 van het Burgerlijk Wetboek
bepaalt dat de aannemer daarna niet meer aansprakelijk is voor gebreken die op dat moment
zichtbaar waren en niet zijn gemeld. De rondgang is daarmee het belangrijkste half uur van
de hele verbouwing.</p>

<h2>Vooraf</h2>
<ul class="checklist">
<li>Rondgang bij daglicht, niet in de avond</li>
<li>De opdrachtgever loopt mee, niet alleen de uitvoerder</li>
<li>Papier en telefoon mee voor foto's van elk punt</li>
<li>De offerte en het meerwerkoverzicht bij de hand</li>
<li>Laatste betaaltermijn nog niet voldaan</li>
</ul>

<h2>Bouwkundig</h2>
<ul class="checklist">
<li>Wanden en plafonds vlak, zonder zichtbare naden of bollingen bij strijklicht</li>
<li>Naden en aansluitingen strak afgekit, zonder scheuren of gaten</li>
<li>Deuren sluiten zonder klemmen, sloten en krukken werken</li>
<li>Plinten aangebracht en aangesloten op de vloer</li>
<li>Vloer vlak en zonder holklinkende plekken</li>
<li>Tegelwerk in lijn, voegen gelijkmatig en volledig gevuld</li>
<li>Geen beschadigingen aan kozijnen, trapleuning of vensterbanken</li>
</ul>

<h2>Installaties</h2>
<ul class="checklist">
<li>Alle wandcontactdozen getest, ook die achter de kasten</li>
<li>Schakelaars schakelen wat ze horen te schakelen</li>
<li>Groepenkast voorzien van een leesbaar en kloppend schema</li>
<li>Aardlekschakelaar getest met de testknop</li>
<li>Kranen zonder lekkage, ook bij de aansluiting onder de wastafel</li>
<li>Afvoeren lopen door, sifons gevuld en reukvrij</li>
<li>Ventilatie getest op alle standen, met een blaadje papier bij het rooster</li>
<li>Radiatoren warm over de volle hoogte, systeem ontlucht en op druk</li>
<li>Rookmelders aanwezig op elke bouwlaag met een verblijfsruimte, en getest</li>
</ul>

<h2>Documenten</h2>
<ul class="checklist">
<li>Garantiebewijzen per onderdeel, met de termijn erbij</li>
<li>Handleidingen van apparatuur en installaties</li>
<li>Constructieberekening en definitieve tekeningen</li>
<li>Foto's van leidingwerk en elektra voordat de wanden dichtgingen</li>
<li>Overzicht van het uitgevoerde meerwerk met bedragen</li>
<li>Certificaat of meetrapport van de elektrische installatie, indien afgesproken</li>
</ul>

<h2>Afspraken vastleggen</h2>
<ul class="checklist">
<li>Alle punten op één lijst, ondertekend door beide partijen</li>
<li>Termijn afgesproken waarbinnen de punten verholpen worden</li>
<li>Vastgelegd welk bedrag pas wordt betaald na afhandeling</li>
<li>Datum voor de controle van de restpunten in de agenda</li>
</ul>

<div class="kader">
<p>Gebreken die bij de oplevering niet zichtbaar waren, kunnen later alsnog worden gemeld.
Artikel 7:761 van het Burgerlijk Wetboek geeft daarvoor een verjaringstermijn van twee jaar
na de melding. Schriftelijk melden zodra iets wordt ontdekt is daarbij de enige route die
achteraf stand houdt.</p>
</div>

<p>Meer over de juridische kant staat op <a href="/voorbereiding/contract-en-oplevering/">contract,
meerwerk en oplevering</a>.</p>
</section>
"""

site.add('/hulpmiddelen/opleverchecklist/', T('Opleverchecklist verbouwing'),
         'Checklist voor de oplevering van een verbouwing: bouwkundig, installaties, '
         'documenten en de afspraken die op papier moeten voordat de laatste termijn wordt betaald.',
         OPLEVER, h1='Opleverchecklist')

# ---------------------------------------------------------------- nieuws
nieuws_index_kaarten = ''.join(
    kaart(t, '/nieuws/%s/' % s, sam, nl_datum(datum))
    for s, datum, _rfc, t, _d, sam, _md in C_NIEUWS.ARTIKELEN)

site.add('/nieuws/', T('Nieuws over verbouwen, bouwkosten en regelgeving'),
         'Artikelen over bouwkosten, subsidies, vergunningen en de praktijk van verbouwen '
         'in Nederland.',
         '<section class="smal"><h1>Nieuws</h1><p>Artikelen over bouwkosten, subsidies, '
         'regelgeving en de praktijk van verbouwen. Nieuwe artikelen verschijnen ook via '
         '<a href="/rss.xml">de rss-feed</a>.</p></section>'
         '<section><div class="rooster">%s</div></section>' % nieuws_index_kaarten,
         h1='Nieuws', priority='0.9')

for slug, datum, rfc, titel, desc, sam, md in C_NIEUWS.ARTIKELEN:
    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": titel,
        "datePublished": datum,
        "dateModified": datum,
        "inLanguage": "nl-NL",
        "description": desc,
        "mainEntityOfPage": BASE + '/nieuws/%s/' % slug,
        "publisher": {"@type": "Organization", "name": NAAM},
    }, ensure_ascii=False)
    body = ('<section class="smal"><h1>%s</h1>'
            '<p class="artikelmeta">Gepubliceerd op %s</p>%s%s'
            '<p><a href="/nieuws/">Terug naar het nieuwsoverzicht</a></p></section>'
            % (titel, nl_datum(datum), render(md), kk_blok()))
    site.add('/nieuws/%s/' % slug, T(titel), desc, body,
             h1=titel, schema=schema, lastmod=datum)

# ---------------------------------------------------------------- over
OVER_MD = """
Grootinkluswerk.nl is een informatieve gids over grote klussen en verbouwingen aan
woningen in Nederland. De site verzamelt op één plek wat er bij zo'n klus komt kijken: de
volgorde van het werk, de kosten per onderdeel, de regels rond vergunningen en meldingen,
en de afspraken die achteraf het verschil maken.

## Wat deze site wel doet

- Uitleggen hoe een klus technisch in elkaar zit en in welke volgorde het werk gebeurt
- Richtprijzen geven per klus en per vakgebied, met de bandbreedte erbij
- Verwijzen naar de officiële bronnen voor vergunningen, subsidies en fiscale regels
- Twee hulpmiddelen aanbieden die volledig in de browser draaien: een budgetberekening en een opleverchecklist

## Wat deze site niet doet

- Bemiddelen tussen opdrachtgevers en aannemers
- Offertes aanvragen of doorsturen
- Contactgegevens verzamelen of verkopen

Er staat geen formulier op deze site. Er is geen offerteaanvraag, geen vergelijkingsdienst
en geen doorverwijzing tegen betaling.

## Herkomst van de cijfers

De bedragen in deze gids zijn indicaties, gebaseerd op gangbare marktprijzen voor
particuliere opdrachtgevers in Nederland. Ze zijn bedoeld om een orde van grootte te
bepalen, niet om een offerte te vervangen. Regionale verschillen en de staat van de woning
zorgen in de praktijk voor afwijkingen van tientallen procenten.

Waar het om wetgeving, subsidies of officiële cijfers gaat, staat de bron erbij vermeld.
Dat zijn onder meer het Centraal Bureau voor de Statistiek, de Rijksdienst voor Ondernemend
Nederland, het Informatiepunt Leefomgeving en de Belastingdienst.

## Actualiteit

Regels en bedragen veranderen. De pagina's in deze gids vermelden de stand op het moment
van schrijven en verwijzen naar de plek waar de actuele versie staat. Bij twijfel geldt de
officiële bron, niet deze site.

## Kleine klussen

Deze gids gaat over werk waar meerdere vakgebieden of een vergunning aan te pas komen. Voor
losse klussen die binnen een dagdeel af zijn, is een andere aanpak logischer. Zie
Kleine-Klussen.nl voor het per klus of per uur inplannen van een vakman, met online een
datum en tijdslot: https://www.kleine-klussen.nl/

## Contact

Vragen of opmerkingen over de inhoud kunnen naar info@grootinkluswerk.nl. Meer daarover
staat op de contactpagina.
"""

site.add('/over/', T('Over Grootinkluswerk.nl'),
         'Wat Grootinkluswerk.nl is: een onafhankelijke gids over grote klussen en '
         'verbouwingen, zonder bemiddeling, offerteaanvraag of leadverkoop.',
         '<section class="smal"><h1>Over deze gids</h1>%s</section>' % render(OVER_MD),
         h1='Over deze gids', priority='0.6')

# ---------------------------------------------------------------- contact
CONTACT = """
<section class="smal">
<h1>Contact</h1>
<p>Grootinkluswerk.nl is een informatieve gids. Er is één contactmogelijkheid en dat is
e-mail.</p>

<div class="kader">
<p><strong>E-mail</strong><br><a href="mailto:info@grootinkluswerk.nl">info@grootinkluswerk.nl</a></p>
</div>

<h2>Waar deze site niet voor is</h2>
<p>Er wordt niet bemiddeld tussen opdrachtgevers en vakmensen. Er worden geen offertes
aangevraagd, doorgestuurd of vergeleken. Een verzoek om een klus in te plannen kan hier
niet worden behandeld.</p>

<h2>Waarvoor wel</h2>
<ul>
<li>Een feitelijke onjuistheid op een pagina melden</li>
<li>Een suggestie voor een onderwerp dat ontbreekt</li>
<li>Een vraag over de herkomst van een cijfer of een verwijzing</li>
<li>Een verzoek in het kader van de privacywetgeving</li>
</ul>

<h2>Een vakman inplannen</h2>
<p>Voor het daadwerkelijk inplannen van een klus is Kleine-Klussen.nl een optie. Daar wordt
online een datum en tijdslot gekozen voor kleine klussen aan huis. Zie
<a href="https://www.kleine-klussen.nl/" rel="nofollow noopener" target="_blank">https://www.kleine-klussen.nl/</a></p>

<h2>Reactietermijn</h2>
<p>E-mail wordt doorgaans binnen enkele werkdagen beantwoord. Berichten met een commercieel
aanbod of een verzoek tot linkplaatsing blijven onbeantwoord.</p>
</section>
"""

site.add('/contact/', T('Contact'),
         'Contact met Grootinkluswerk.nl loopt uitsluitend via info@grootinkluswerk.nl. '
         'Geen formulier, geen bemiddeling, geen offerteaanvraag.',
         CONTACT, h1='Contact', priority='0.5')

# ---------------------------------------------------------------- privacy
PRIVACY_MD = """
Deze verklaring beschrijft hoe Grootinkluswerk.nl omgaat met persoonsgegevens. Laatste
wijziging: 29 augustus 2026.

## Uitgangspunt

Grootinkluswerk.nl is een informatieve website zonder inlogfunctie, zonder
contactformulier, zonder nieuwsbrief en zonder webwinkel. Er worden geen accounts
aangemaakt en er worden geen gegevens gevraagd om de site te gebruiken.

## Welke gegevens worden verwerkt

### Bij het bezoeken van de site
De website wordt gehost bij Cloudflare Pages. De hostingpartij verwerkt technische gegevens
die nodig zijn om de site te tonen en te beveiligen, waaronder het IP-adres, het tijdstip
van het verzoek, de opgevraagde pagina en het type browser. Die verwerking vindt plaats op
grond van een gerechtvaardigd belang: het beschikbaar en veilig houden van de website.

Er wordt geen bezoekersstatistiek van derden geladen, geen advertentienetwerk, geen
socialemediaknop en geen ingesloten inhoud van andere partijen. De pagina's laden geen
externe bestanden.

### Bij e-mail
Wie mailt naar info@grootinkluswerk.nl, verstuurt daarmee een e-mailadres en de inhoud van
het bericht. Die gegevens worden gebruikt om het bericht te beantwoorden en daarna niet
langer bewaard dan nodig. Er wordt geen mailinglijst opgebouwd en er worden geen
e-mailadressen gedeeld met derden.

## Cookies

Deze website plaatst geen cookies voor analyse, advertenties of profilering. Zie het
cookiebeleid voor de details.

## Bewaartermijn

E-mailcorrespondentie wordt bewaard zolang dat nodig is voor de afhandeling, en daarna
verwijderd. Technische logbestanden bij de hostingpartij worden volgens het beleid van die
partij bewaard en daarna verwijderd.

## Delen met derden

Persoonsgegevens worden niet verkocht en niet gedeeld voor commerciële doeleinden. Delen
gebeurt alleen als een wettelijke verplichting daartoe verplicht.

## Rechten

Op grond van de Algemene verordening gegevensbescherming bestaat het recht op inzage,
correctie, verwijdering, beperking en bezwaar. Een verzoek daartoe kan naar
info@grootinkluswerk.nl. Er wordt binnen een maand gereageerd.

Wie een klacht heeft over de verwerking van persoonsgegevens, kan die indienen bij de
Autoriteit Persoonsgegevens via https://www.autoriteitpersoonsgegevens.nl

## Beveiliging

De site wordt uitsluitend over https aangeboden. Er worden geen gegevens op de website
opgeslagen, omdat er geen formulieren en geen database zijn.

## Externe links

Deze site verwijst naar websites van derden. Op die websites geldt het privacybeleid van
die partij. Grootinkluswerk.nl is niet verantwoordelijk voor de inhoud of de
gegevensverwerking van externe websites.

## Wijzigingen

Deze verklaring kan worden aangepast als de opzet van de website verandert. De datum
bovenaan geeft de laatste wijziging aan.
"""

site.add('/privacybeleid/', T('Privacybeleid'),
         'Hoe Grootinkluswerk.nl omgaat met persoonsgegevens: geen formulieren, geen '
         'tracking, geen cookies voor analyse of advertenties.',
         '<section class="smal"><h1>Privacybeleid</h1>%s</section>' % render(PRIVACY_MD),
         h1='Privacybeleid', priority='0.3')

COOKIE_MD = """
Laatste wijziging: 29 augustus 2026.

## Geen cookies

Grootinkluswerk.nl plaatst geen cookies. Er is geen analysepakket, geen advertentienetwerk,
geen socialemediaknop en geen ingesloten inhoud van derden. Daarom staat er ook geen
cookiemelding op deze site: een toestemmingsvraag zonder cookies heeft geen functie.

## Wat er technisch wel gebeurt

De website draait op Cloudflare Pages. De hostingpartij kan een technische voorziening
inzetten om misbruik en overbelasting tegen te gaan. Dat is geen cookie voor analyse of
advertenties en er wordt geen bezoekersprofiel mee opgebouwd.

## Lokale opslag

De hulpmiddelen op deze site, zoals de budgetberekening, rekenen volledig in de browser.
Er wordt niets opgeslagen in de browser en er gaat niets naar een server. Wie de pagina
sluit, laat niets achter.

## Externe links

Links naar andere websites openen in een nieuw tabblad. Zodra een externe website wordt
geopend, geldt het cookiebeleid van die partij. Dat kan afwijken van het beleid op deze
site.

## Cookies uitzetten

Elke browser biedt de mogelijkheid cookies te blokkeren of te verwijderen. Omdat deze site
geen cookies plaatst, heeft dat geen invloed op de werking ervan.

## Vragen

Vragen over dit cookiebeleid kunnen naar info@grootinkluswerk.nl
"""

site.add('/cookiebeleid/', T('Cookiebeleid'),
         'Grootinkluswerk.nl plaatst geen cookies voor analyse, advertenties of '
         'profilering. Uitleg over wat er technisch wel gebeurt.',
         '<section class="smal"><h1>Cookiebeleid</h1>%s</section>' % render(COOKIE_MD),
         h1='Cookiebeleid', priority='0.3')

# ---------------------------------------------------------------- 404
site.add('/404/', T('Pagina niet gevonden'),
         'Deze pagina bestaat niet of is verplaatst.',
         '<section class="smal"><h1>Pagina niet gevonden</h1>'
         '<p>Deze pagina bestaat niet of is verplaatst. Onderstaande overzichten geven '
         'toegang tot de rest van de gids.</p>'
         '<ul><li><a href="/">Home</a></li>'
         '<li><a href="/klussen/">Grote klussen</a></li>'
         '<li><a href="/voorbereiding/">Voorbereiding</a></li>'
         '<li><a href="/kosten/">Wat kost een verbouwing</a></li>'
         '<li><a href="/hulpmiddelen/">Hulpmiddelen</a></li>'
         '<li><a href="/nieuws/">Nieuws</a></li>'
         '<li><a href="/contact/">Contact</a></li></ul></section>',
         h1='Pagina niet gevonden')

# ---------------------------------------------------------------- schrijven
if __name__ == '__main__':
    aantal = site.build('dist')
    site.rss('dist', [dict(title=t, path='/nieuws/%s/' % s, rfc822=rfc, summary=sam)
                      for s, _d, rfc, t, _desc, sam, _md in C_NIEUWS.ARTIKELEN])
    print('%d pagina\'s geschreven naar dist/' % aantal)
