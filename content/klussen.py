# -*- coding: utf-8 -*-
"""Pagina's over grote klussen: wat komt erbij kijken, wat kost het, wat duurt het."""

INDEX_INTRO = """
Een grote klus onderscheidt zich van een kleine niet door het aantal uren, maar door het
aantal partijen. Zodra er een tweede vakman aan te pas komt, een vergunning nodig is of
de constructie geraakt wordt, verandert de aanpak. De volgorde van het werk gaat dan
zwaarder wegen dan de prijs per uur.

Hieronder staan de klussen die het vaakst in die categorie vallen, met per klus de
werkzaamheden, de doorlooptijd, de kostenposten en de punten waarop het in de praktijk
misgaat.
"""

KLUSSEN = [
    # ------------------------------------------------------------------
    ("badkamer-verbouwen", "Badkamer verbouwen",
     "Badkamer verbouwen: volgorde van het werk, doorlooptijd, kostenposten en de fouten die het vaakst tot meerwerk leiden.",
     """
Een complete badkamer is de klus waarin de meeste vakgebieden samenkomen. Sloopwerk,
loodgieterswerk, elektra, tegelwerk, ventilatie en soms stucwerk moeten in een vaste
volgorde langskomen. Loopt een van die partijen uit, dan schuift alles erachter mee.

## Volgorde van het werk

1. Slopen en afvoeren van tegels, sanitair en oude leidingen
2. Leidingwerk aanpassen: aan- en afvoer op de nieuwe posities
3. Elektra aanpassen: groepen, wandcontactdozen buiten de spatzones, aansluiting voor de ventilator
4. Wanden en vloer vlak maken, kimband en waterdichte laag aanbrengen
5. Tegelwerk wand en vloer, daarna voegen
6. Sanitair plaatsen en aansluiten
7. Kitwerk als laatste, na het uitharden van de voegen

## Doorlooptijd

Een standaard badkamer van vier tot zes vierkante meter kost doorgaans acht tot vijftien
werkdagen, verspreid over twee tot drie weken. De uitloop zit vrijwel altijd in het
wachten: op levering van tegels of sanitair, op het uitharden van de egaline en op de
volgende vakman in de rij.

## Kostenposten

| Post | Indicatie |
| --- | --- |
| Sloop en afvoer | 400 tot 900 euro |
| Leidingwerk aanpassen | 800 tot 2.000 euro |
| Elektra en ventilatie | 500 tot 1.500 euro |
| Tegelwerk arbeid | 45 tot 75 euro per vierkante meter |
| Sanitair, materiaal | 1.500 tot 6.000 euro |
| Tegels, materiaal | 25 tot 90 euro per vierkante meter |

Dit zijn indicaties voor een eengezinswoning zonder verrassingen. De grootste
prijsverschillen zitten niet in de arbeid maar in de keuze van sanitair en tegelformaat.
Grote formaten vragen een vlakkere ondergrond en dus meer voorbereidend werk.

## Waar het misgaat

- Ventilatie te licht gekozen. Een badkamer zonder buitenraam vraagt mechanische afvoer met voldoende capaciteit, anders volgt schimmel op de kitranden binnen een jaar.
- Leidingen niet ingemeten voordat de tegels besteld zijn. Een afvoer die tien centimeter verschuift, kost een halve dag hakwerk.
- Sanitair te laat besteld. Levertijden van zes tot twaalf weken zijn gebruikelijk bij niet-voorraadmodellen.
- Geen waterdichte laag onder de tegels in de doucheruimte. Tegels en voegen zijn niet waterdicht, de laag eronder is dat wel.

## Vergunning

Een badkamer binnen de bestaande indeling is vergunningvrij. Zodra er een dragende wand
wijkt of er een raamopening bij komt, verandert dat. De vergunningcheck staat op
https://omgevingswet.overheid.nl
"""),
    # ------------------------------------------------------------------
    ("keuken-plaatsen", "Keuken plaatsen of vervangen",
     "Keuken vervangen: inmeten, leidingwerk, elektragroepen, montage en de doorlooptijd van bestelling tot aansluiting.",
     """
Bij een keuken zit het werk voor en na de montage. De montage zelf duurt een tot drie
dagen. Het inmeten, het aanpassen van water en elektra en het aansluiten van de apparatuur
bepalen of die dagen soepel verlopen.

## Wat er vooraf moet kloppen

- De aansluitpunten voor water en afvoer op de nieuwe positie van de spoelbak
- Voldoende groepen in de meterkast. Een moderne keuken vraagt al snel drie tot vier aparte groepen voor oven, kookplaat, vaatwasser en koelkast
- Een aparte krachtstroomgroep bij inductie met een aansluitwaarde boven de 3,7 kilowatt
- Een afvoerkanaal voor de afzuigkap, of de keuze voor recirculatie met koolstoffilter
- Een vlakke, waterpas vloer, zeker bij hoge kasten

## Volgorde

1. Inmeten door de leverancier of de monteur, met de definitieve indeling op papier
2. Oude keuken demonteren en afvoeren
3. Leidingwerk en elektra verleggen, wanden herstellen en sausen
4. Kasten stellen, werkblad plaatsen of laten inmeten voor steen
5. Apparatuur inbouwen en aansluiten
6. Kitwerk en plinten

## Doorlooptijd

Van bestelling tot werkende keuken zit doorgaans zes tot twaalf weken. De montage beslaat
daarvan twee tot vier dagen. Bij een stenen werkblad komt daar een week tussenruimte bij:
dat blad wordt pas ingemeten als de onderkasten staan.

## Kostenposten

| Post | Indicatie |
| --- | --- |
| Demontage en afvoer oude keuken | 300 tot 700 euro |
| Elektra uitbreiden, per groep | 150 tot 350 euro |
| Water en afvoer verleggen | 300 tot 900 euro |
| Montage keuken, arbeid | 700 tot 2.500 euro |
| Stenen werkblad, inmeten en plaatsen | 1.200 tot 4.000 euro |

## Waar het misgaat

- De meterkast blijkt vol. Een extra groep vraagt ruimte in de kast en soms een zwaardere hoofdaansluiting.
- De afzuigkap wordt op een bestaand kanaal aangesloten dat te smal is, waardoor de capaciteit tegenvalt.
- De vloer is niet vlak, waardoor het werkblad niet strak aansluit op de wand.
- Apparatuur wordt besteld zonder de nismaten van de kastenlijn te controleren.
"""),
    # ------------------------------------------------------------------
    ("zolder-verbouwen", "Zolder verbouwen tot kamer",
     "Zolder verbouwen tot slaapkamer of werkkamer: vloerbelasting, isolatie, daglicht, elektra en de eisen aan een verblijfsruimte.",
     """
Een zolder ombouwen tot verblijfsruimte lijkt eenvoudig omdat de ruimte er al is. In de
praktijk gaat het om vier vragen: draagt de vloer, is de ruimte hoog genoeg, komt er
genoeg daglicht en lucht binnen, en is de vluchtroute in orde.

## De vier vragen vooraf

### Draagt de vloer
Een zoldervloer die als bergzolder is gebouwd, is niet altijd berekend op de belasting van
een verblijfsruimte. Bij twijfel rekent een constructeur de balklaag na. Verzwaren kan
door balken bij te leggen of door een dubbele beplating aan te brengen.

### Hoogte
Voor een verblijfsruimte geldt een minimale vrije hoogte over een deel van het oppervlak.
Bij een lage nokhoogte blijft alleen de middenstrook bruikbaar, wat de indeling bepaalt.

### Daglicht en ventilatie
Een dakraam of dakkapel levert daglicht en luchtverversing. Zonder te openen raam is
mechanische ventilatie nodig.

### Vluchtroute
Een slaapkamer op zolder vraagt een veilige route naar buiten en werkende rookmelders op
elke verdieping. Rookmelders zijn in alle woningen verplicht op iedere bouwlaag met een
verblijfsruimte.

## Isolatie

Een onbewerkte zolder is meestal de grootste warmteverliespost van de woning. Isoleren
gebeurt aan de binnenzijde tussen en onder de sporen, of aan de buitenzijde bij vervanging
van de dakbedekking. Voor dakisolatie en zoldervloerisolatie bestaat subsidie via de ISDE,
met een minimum van twintig vierkante meter en aanvraag binnen vierentwintig maanden na
uitvoering. De voorwaarden staan op https://www.rvo.nl

## Kostenposten

| Post | Indicatie |
| --- | --- |
| Dakisolatie binnenzijde, per vierkante meter | 60 tot 120 euro |
| Vloer verzwaren | 900 tot 3.000 euro |
| Wanden en plafond afwerken | 45 tot 90 euro per vierkante meter |
| Elektra, nieuwe groep en punten | 700 tot 1.800 euro |
| Dakraam inclusief plaatsen | 900 tot 2.200 euro |

## Doorlooptijd

Drie tot zes weken voor een complete zolderkamer, inclusief wachttijd op stucwerk en
schilderwerk.
"""),
    # ------------------------------------------------------------------
    ("dakkapel-plaatsen", "Dakkapel plaatsen",
     "Dakkapel plaatsen: vergunningvrij of niet, prefab of op maat, doorlooptijd van een dag en de aansluitdetails die lekkage voorkomen.",
     """
Een dakkapel levert hoofdruimte en daglicht op een plek waar het schuine dak dat wegneemt.
De plaatsing zelf duurt bij een prefab uitvoering meestal een dag. Het traject ervoor duurt
langer.

## Vergunningvrij of niet

Een dakkapel aan het achterdakvlak is onder voorwaarden vergunningvrij. Het gaat dan om de
plaats op het dakvlak, de hoogte, de afstand tot de dakranden en het achtererfgebied. Aan
de voorzijde of aan de straatkant is vrijwel altijd een omgevingsvergunning nodig, en in
een beschermd stadsgezicht geldt een strenger regime. De vergunningcheck staat op
https://omgevingswet.overheid.nl

Ook zonder vergunningplicht kan een vereniging van eigenaars toestemming vragen. Bij een
appartement is dat de eerste stap, niet de laatste.

## Prefab of op maat

Een prefab dakkapel komt als geheel op de wagen en wordt met een kraan of hoogwerker
geplaatst. Voordeel is de korte overlast: een dag dak open, een dag dicht. Op maat bouwen
gebeurt op het dak zelf en duurt drie tot vijf dagen, maar past bij afwijkende maten en
bij een bestaande kapconstructie die niet standaard is.

## Kostenposten

| Post | Indicatie |
| --- | --- |
| Prefab dakkapel tot 2,5 meter, geplaatst | 7.000 tot 11.000 euro |
| Per extra strekkende meter | 1.200 tot 1.900 euro |
| Kraan of hoogwerker | 400 tot 900 euro |
| Afwerking binnenzijde, stucwerk en schilderwerk | 900 tot 2.500 euro |
| Omgevingsvergunning, leges | afhankelijk van de gemeente |

## Details die lekkage voorkomen

- De aansluiting van het loodwerk op de dakpannen, met voldoende overlap
- Een doorlopende dampremmende laag aan de binnenzijde, zonder gaten bij de stopcontacten
- Ventilatie van de spouw achter de zijwangen
- Een goede afvoer van het platte dakje, met een noodoverloop

## Doorlooptijd

Bij prefab: zes tot tien weken van opdracht tot plaatsing, waarvan de productie het
grootste deel is. Bij vergunningplicht komt de behandeltermijn van de gemeente daar nog
bij, doorgaans acht weken voor de reguliere procedure.
"""),
    # ------------------------------------------------------------------
    ("uitbouw-aanbouw", "Uitbouw of aanbouw",
     "Uitbouw aan de achterzijde: vergunningvrije maten, fundering, constructie, isolatie-eisen en een realistische doorlooptijd.",
     """
Een uitbouw aan de achterzijde is de meest gevraagde uitbreiding van een rijwoning. Het is
ook de klus waarbij de grond, de constructie en de regelgeving alle drie meespelen.

## Vergunningvrij tot een bepaalde maat

In het achtererfgebied mag onder voorwaarden een uitbouw van beperkte diepte
vergunningvrij worden gebouwd, mits die aan de achtergevel grenst en binnen de gestelde
hoogte blijft. Boven die maat geldt een vergunningplicht, en in sommige gevallen een
toets aan het omgevingsplan. De check per adres staat op https://omgevingswet.overheid.nl

Belangrijk detail: vergunningvrij bouwen betekent niet regelvrij bouwen. De eisen aan
constructie, isolatie, ventilatie en brandveiligheid uit het Besluit bouwwerken
leefomgeving gelden onverkort.

## Wat de constructie vraagt

De achtergevel die wegvalt, moet worden opgevangen. Dat gebeurt met een stalen ligger op
kolommen of penanten. De maat van die ligger volgt uit een constructieberekening. Wie de
berekening overslaat, ontdekt het gevolg pas als er scheuren in het metselwerk boven de
opening verschijnen.

De fundering van de uitbouw sluit aan op de bestaande. Bij een woning op palen betekent
dat vaak nieuwe palen of een gefundeerde plaat, anders zakt de aanbouw los van het huis en
scheurt de aansluiting open.

## Kostenposten

| Post | Indicatie |
| --- | --- |
| Uitbouw casco, per vierkante meter | 1.800 tot 2.800 euro |
| Compleet afgewerkt, per vierkante meter | 2.500 tot 3.800 euro |
| Constructieberekening | 600 tot 1.500 euro |
| Bouwtekening en vergunningaanvraag | 900 tot 2.500 euro |
| Leges gemeente | percentage van de bouwsom |

## Doorlooptijd

- Ontwerp en berekening: twee tot zes weken
- Vergunningprocedure indien nodig: acht weken, met mogelijkheid tot verlenging
- Bouw: zes tot twaalf weken voor een uitbouw van twintig vierkante meter

## Waar het misgaat

- De buren worden pas geïnformeerd als de kraan er staat. Bij bouwen op of tegen de erfgrens is overleg vooraf de goedkoopste verzekering tegen vertraging.
- De kozijnen worden besteld voordat de exacte dagmaten na het metselwerk bekend zijn.
- Er wordt geen rekening gehouden met de afvoer van hemelwater vanaf het nieuwe dak.
"""),
    # ------------------------------------------------------------------
    ("muurdoorbraak", "Muurdoorbraak en dragende wanden",
     "Muurdoorbraak: hoe blijkt of een wand draagt, wat een constructeur berekent, welke melding nodig is en wat het kost.",
     """
Een doorbraak tussen woonkamer en keuken verandert de plattegrond ingrijpend met relatief
weinig sloopwerk. De vraag die alles bepaalt: draagt de wand.

## Hoe blijkt of een wand draagt

Een aantal aanwijzingen samen geeft uitsluitsel, maar geen daarvan is op zichzelf bewijs.

- Dikte. Een wand van tien centimeter of minder draagt zelden, een wand van twintig centimeter of meer vaak wel.
- Richting van de vloerbalken. Balken die haaks op de wand liggen, steunen er meestal op.
- Positie in het gebouw. Een wand die op iedere verdieping op dezelfde plek staat, is verdacht.
- Bouwtekening. Bij veel gemeenten is het bouwdossier van de woning digitaal op te vragen.

De enige betrouwbare route is een constructeur die de situatie ter plaatse beoordeelt en
narekent.

## Wat de constructeur levert

Een berekening met de benodigde profielmaat, de oplegging aan beide zijden en de
belasting op de fundering onder de penanten. Dat document is ook het stuk dat de gemeente
wil zien bij een melding of vergunningaanvraag.

## Melding of vergunning

Het aanpassen van een dragende constructie valt onder de technische bouwactiviteit. Voor
een deel van de gevallen geldt een meldingsplicht, voor een deel een vergunningplicht.
De check per situatie staat op https://omgevingswet.overheid.nl. Het Informatiepunt
Leefomgeving publiceert de achtergrond op https://iplo.nl

## Kostenposten

| Post | Indicatie |
| --- | --- |
| Constructieberekening | 500 tot 1.200 euro |
| Stalen ligger, materiaal | 400 tot 1.400 euro |
| Sloopwerk en stempelen | 700 tot 1.800 euro |
| Aanbrengen ligger en herstel | 1.200 tot 3.500 euro |
| Stuc- en schilderwerk na afloop | 400 tot 1.200 euro |

## Praktijk

Het werk zelf duurt twee tot vier dagen. Stof is de grootste overlast: een stofwand met
rits en een afgeschermde vluchtroute schelen dagen schoonmaak. In een appartement is
toestemming van de vereniging van eigenaars nodig, omdat dragende wanden tot de
gemeenschappelijke delen horen.
"""),
    # ------------------------------------------------------------------
    ("vloer-vervangen", "Vloer vervangen",
     "Vloer vervangen: ondergrond beoordelen, egaliseren, vloerverwarming, geluidseisen bij appartementen en de kosten per vierkante meter.",
     """
De zichtbare vloer is het laatste onderdeel. Wat eronder ligt, bepaalt het resultaat en het
grootste deel van de rekening.

## Ondergrond beoordelen

- Vlakheid. Een afwijking van meer dan drie millimeter over twee meter vraagt egaliseren.
- Vocht. Op een zandcementdekvloer of beton wordt het restvocht gemeten voordat er een gesloten vloer op gaat. Te vroeg dichtleggen leidt tot bolstaande delen.
- Ondergrondtype. Houten vloeren vragen een andere opbouw dan beton, met een verende laag of een onderplaat.

## Vloerverwarming

Bij nieuw aan te leggen vloerverwarming zijn er twee routes: infrezen in de bestaande
dekvloer, of een nieuwe verdeelvloer aanbrengen. Infrezen is sneller en verlaagt de
opbouwhoogte, maar levert minder vermogen per vierkante meter. Een nieuwe vloer vraagt
uithardingstijd van meerdere weken voordat er afwerking op mag.

## Appartement en geluid

Veel verenigingen van eigenaars stellen een minimale contactgeluidisolatie als eis, vaak
uitgedrukt in decibel. Dat staat in het huishoudelijk reglement of de splitsingsakte.
Een harde vloer zonder gekwalificeerde ondervloer is de meest voorkomende oorzaak van
burenconflicten na een verbouwing.

## Kostenposten

| Post | Indicatie |
| --- | --- |
| Oude vloer verwijderen en afvoeren | 12 tot 25 euro per vierkante meter |
| Egaliseren | 15 tot 30 euro per vierkante meter |
| Leggen laminaat of pvc, arbeid | 15 tot 30 euro per vierkante meter |
| Leggen tapijt of vinyl, arbeid | 12 tot 22 euro per vierkante meter |
| Vloerverwarming infrezen | 45 tot 75 euro per vierkante meter |
| Nieuwe dekvloer | 30 tot 55 euro per vierkante meter |

## Volgorde

Een vloer gaat er pas in als het stof uit de rest van de verbouwing weg is. Schilderwerk
aan plinten en kozijnen gebeurt bij voorkeur ervoor, de laatste laag erna.
"""),
    # ------------------------------------------------------------------
    ("isolatie-woning", "Woning isoleren",
     "Woning isoleren: welke maatregel het meeste oplevert, de ISDE-bedragen per vierkante meter en de voorwaarde van twee maatregelen.",
     """
Isoleren is de enige verbouwing die zichzelf deels terugverdient. De volgorde waarin het
gebeurt, bepaalt hoeveel dat is.

## Volgorde op resultaat

1. Dak of zoldervloer. Warmte verdwijnt naar boven, hier zit doorgaans het grootste verlies.
2. Spouwmuur, als de spouw breed genoeg en droog is.
3. Vloer of bodem van de kruipruimte, tegelijk met het aanpakken van vocht.
4. Glas. Van enkel naar HR++ levert veel op, van HR++ naar triple veel minder.
5. Kierdichting. Weinig kosten, direct merkbaar comfortverschil.

## ISDE-bedragen

De Investeringssubsidie duurzame energie en energiebesparing kent vaste bedragen per
vierkante meter. Stand per 2025 en doorlopend in 2026:

| Maatregel | Bedrag per vierkante meter | Minimum oppervlak |
| --- | --- | --- |
| Spouwmuurisolatie | 5,25 euro | 10 |
| Gevelisolatie | 20,25 euro | 10 |
| Bodemisolatie | 3,00 euro | 20 |
| Vloerisolatie | 5,50 euro | 20 |
| Dakisolatie | 16,25 euro | 20 |
| Zoldervloerisolatie | 4,00 euro | 20 |
| Glasisolatie, HR++ | 25,00 euro | 3 |

Bij twee of meer maatregelen binnen vierentwintig maanden verdubbelen de bedragen. Voor
biobased materialen geldt een extra bedrag. De aanvraag gebeurt binnen vierentwintig
maanden na uitvoering. Per 2026 is er ook een vast bedrag van 400 euro voor energiezuinige
ventilatie in combinatie met een isolatiemaatregel. De actuele voorwaarden staan op
https://www.rvo.nl

## Wat er misgaat

- Isoleren zonder ventileren. Een dichte woning zonder luchtverversing levert vocht en schimmel op. Ventilatie hoort bij het plan, niet erna.
- Spouwmuurisolatie in een spouw met doorslag of vochtproblemen. Eerst de oorzaak, dan de isolatie.
- Dakisolatie zonder dampremmende laag aan de warme zijde, met condens in de constructie als gevolg.
- Een vloer isoleren terwijl de kruipruimte nat blijft.

## Btw

Voor het aanbrengen van isolatiemateriaal aan woningen ouder dan twee jaar geldt onder
voorwaarden het verlaagde btw-tarief over de arbeid. De actuele regels staan op
https://www.belastingdienst.nl
"""),
    # ------------------------------------------------------------------
    ("schilderwerk-buiten", "Buitenschilderwerk",
     "Buitenschilderwerk: houtrot herstellen, het juiste seizoen, onderhoudscyclus en het verlaagde btw-tarief op arbeid.",
     """
Buitenschilderwerk is onderhoud, geen verfraaiing. Het verfsysteem beschermt het hout tegen
vocht. Zodra dat systeem open ligt, begint het rekenwerk aan de andere kant: houtrot
herstellen kost een veelvoud van tijdig overschilderen.

## Onderhoudscyclus

- Beschermd gelegen houtwerk op het noorden: zes tot acht jaar
- Zonbelast houtwerk op het zuiden en westen: vier tot zes jaar
- Kozijnen met dekkende lak houden het langer vol dan transparante beits
- Kunststof en aluminium kozijnen vragen geen verfonderhoud, wel reiniging en controle van de rubbers

## Het juiste seizoen

Verf hecht en droogt binnen een bepaald temperatuur- en vochttraject. In de praktijk komt
dat neer op april tot oktober, met een ondergrens rond de vijf graden en een droge
ondergrond. Werken bij hoge luchtvochtigheid of in de directe zon geeft glansverschil en
slechte hechting.

## Houtrot

Kleine aantastingen zijn te herstellen met epoxy of een houtinzet. Bij aantasting dieper
dan een derde van de doorsnede, of bij een aangetaste onderdorpel, is vervangen van het
onderdeel de verstandiger route. Een reparatie die op vochtig hout wordt gezet, komt binnen
twee jaar terug.

## Kostenposten

| Post | Indicatie |
| --- | --- |
| Schilderwerk kozijnen buiten, per woning | 1.800 tot 5.000 euro |
| Steiger of hoogwerker | 300 tot 1.200 euro |
| Houtrotherstel, per plek | 80 tot 350 euro |
| Onderdorpel vervangen | 250 tot 600 euro |

## Btw

Voor schilder- en stukadoorswerk aan woningen ouder dan twee jaar geldt het verlaagde
btw-tarief van 9 procent over de arbeid. Het materiaal blijft belast tegen het algemene
tarief. Dat scheelt op een offerte van vierduizend euro een paar honderd euro, mits de
aannemer arbeid en materiaal gescheiden vermeldt. De voorwaarden staan op
https://www.belastingdienst.nl
"""),
    # ------------------------------------------------------------------
    ("tuin-aanleggen", "Tuin aanleggen of herstraten",
     "Tuin aanleggen: grondwerk, afschot, drainage, bestrating en beplanting, met kosten per vierkante meter en het beste seizoen.",
     """
Een tuin die na twee jaar nog vlak ligt, dankt dat aan het grondwerk. Bestrating en
beplanting zijn zichtbaar, de voorbereiding eronder bepaalt het resultaat.

## Grondwerk

- Uitgraven tot voldoende diepte: bij bestrating doorgaans dertig tot veertig centimeter onder het gewenste peil
- Een zandbed aanbrengen en verdichten in lagen, niet in een keer
- Afschot van minstens een centimeter per meter, weg van de gevel
- Bij natte grond een drainageleiding naar een infiltratiekoffer of het riool, waar dat is toegestaan

## Bestrating

Het formaat bepaalt de verwerkingstijd. Kleine klinkers vragen meer arbeid per vierkante
meter dan grote betontegels, maar zijn eenvoudiger te herstellen na een verzakking.
Keramische tegels op tegeldragers of in split zijn onderhoudsarm maar vragen een strakke,
stabiele fundering.

## Kostenposten

| Post | Indicatie |
| --- | --- |
| Grondwerk en afvoeren grond, per vierkante meter | 25 tot 55 euro |
| Bestrating leggen, arbeid, per vierkante meter | 30 tot 60 euro |
| Betontegels, materiaal, per vierkante meter | 15 tot 40 euro |
| Keramiek, materiaal, per vierkante meter | 45 tot 100 euro |
| Schutting plaatsen, per strekkende meter | 90 tot 200 euro |
| Beplanting en grond | sterk afhankelijk van maat en soort |

## Seizoen

Grondwerk en bestrating kunnen het hele jaar door, behalve bij vorst in de grond.
Beplanting gaat het beste in het najaar, tussen half oktober en half december, of vroeg in
het voorjaar. Gazon inzaaien lukt bij een bodemtemperatuur boven de tien graden.

## Regels

Voor een schutting geldt een maximale hoogte op de erfgrens; daarboven is toestemming van
de gemeente nodig. Bomen kennen in veel gemeenten een kapvergunning boven een bepaalde
stamomtrek. De check staat op https://omgevingswet.overheid.nl
"""),
]
