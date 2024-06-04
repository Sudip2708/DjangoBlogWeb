# Django Blog Web

Smyslem tohoto projektu bylo naučit se struktuře Django, 
jeho možnostem, ale také k nalezení optimálního přístupu k řešení výzev, 
které programování sebou přináší a osvojení si pracovních postupů.


## Popis projektu

Samotný projekt je zaměřen na stránky pro vytváření a správu mediálních článků. 
Základem projektu je tato šablona: https://bootstrapious.com/p/bootstrap-blog a jeho páteří jsou:

- Stránky pro zobrazení a vyhledávání v publikovaných článcích
- Stránky pro přihlášení a správu uživatele (a případného autora)
- Stránky pro vytvoření, úpravu a mazání článků
- Homepage s editovatelným obsahem pro superuživatele

Jedná se o můj třetí projekt (druhý dělaný v Django), který mě má posunout na cestě k práci programátora.


## Rozbor projektu

- Pro rychlou orientaci v projektu poslouží 
[seznam všech URL jmen použitých v projektu.](readme_data/01_url_list.md)
- Pro hlubší pochopení projektu pak poslouží 
[podrobný popis struktury pohledů](readme_data/02_view_list.md)
a
[podrobný popis struktury hlavičky.](readme_data/04_header.md)
- Pro přehled instalovaných balíčků je připraven 
[seznam pip instalací.](readme_data/03_pip_install.md)
- Pro kompletní obsah celého projektu slouží
[strom projektu s popisem souborů.](readme_data/05_tree.md)
- Pro představu jak vypadá samotný web je zde 
[kompletní seznam screenshotů.](readme_data/06_screenshots.md)



## Moje cesta

Python jsem se začal učit před více než dvěma roky a přibližně před rokem jsem úspěšně absolvoval 3-měsíční kurz, 
který mě obohatil o úvodní náhled do využití Pythonu pro programování webových aplikací.

Po kurzu jsem si pár měsíců osovojoval nabité zkušenosti na aplikaci psané ve Flasku. 
Ta byla velmi zjednodušenou verzí tohoto projektu. 
Doufal jsem, že po jejím dokončení již budu připraven pro pracovní trh. 
Ale pro práci z domova, s jejíž vidinou se toto vše učím, to stále bylo málo a mě došlo, 
že Flask nestačí a je potřeba se dobře dorozumět i s Django.

Začal jsem tím, že jsem projekt přepsal i do Django, abych pochopil, co je pojí. 
Následně jsem obdržel testovací úkol, který měl prověřit moje schopnosti. 
Zprvu jsem úkol vnímal jako snadný, neboť jeho zadání nebylo moc odlišné od toho, co už jsem dělal. 
Ale po čase mi došlo, že je toho ještě mnoho, co neví a co nutně potřebuji vědět, 
abych se mohl o takovouto práci ucházet. 
Z testovacího úkolu jsem udělal učební materiál.


## Učební proces

Tam, kde to šlo, snažil jsem se jít jinou cestou, než ve svém předešlém projektu, abych se co nejvíce naučil. 
Tomu jsem přizpůsobil i tempo a přednost mělo pochopit vše tak, abych tomu plně rozuměl. 
Tím se vše extrémně zpomalilo a z projektu, který jsem si původně myslel, že budu mít na měsíc, se stala téměř půlroční záležitost.

Jestli to byl dobře investovaný čas, se teprve dozvím. 
Ale osobní pokrok je pro mě patrný už jen v tom, že všemu, co je v mém kódu, plně rozumím a jsem i schopný diskutovat o výhodách a nevýhodách zvolených postupů. 
A tak doufám, že hlavní prioritu celého projektu, dobře porozumět a ovládnout Django, tak abych si s klidným svědomím mohl v tomto oboru hledat práci, jsem naplnil.


## Role ChatGPT

Nedocenitelným pomocníkem se mi stala bezplatná verze ChatGPT, která i přes pár let starou databázi stále držela krok s tím, co jsem od ní potřeboval. 
Dá se říct, že téměř vše, co jsem potřeboval vědět, jsem se dozvěděl díky ní. 
Postupně jsem se naučil i dobře specifikovat své dotazy tak, abych dostával velmi relevantní odpovědi. 
ChatGPT se mi stal asistentem, s jehož pomocí vím, že se nemusím obávat žádné výzvy. 
Mít takto propracovaný statistický nástroj k ruce je pro programátora opravdová radost, obzvláště když se s ním dá domluvit normální řečí.

## Pracovní postupy

Veškeré mé pracovní postupy se ustálily na rozebrání nejčastějších přístupů k dané věci s popisem výhod a nevýhod. 
I diagnostikování chyb a hledání nápravy se neskutečně zjednodušilo. 
Prakticky nikdy jsem nenarazil na to, že bych si něco vymyslel a pak se to nedalo provést. 
To ale paradoxně i trochu zdržovalo, protože jsem spoustu věcí, co jsem dělal, zase zrušil pro jejich zbytečnost. 
Ale tím vším jsem se učil. 
A kdykoliv nastala situace, že v hlavě se mi vše vařilo, šel jsem na procházku se psem, 
a domů jsem se vracel, už s promyšleným řešením.

## Závěr

Samotný projekt tedy není plně hotov, a nebude-li to po mně někdo chtít, asi ani nikdy plně hotový nebude. 
Ale splnil vše, co jsem od něj očekával, a vzhledem k mé momentální finanční situaci mi nedává moc smysl věnovat čas věcem, které již dobře umím. 
Raději bych se dále rozvíjel na projektech, za které budu i finančně odměněn.
Z tohoto pohledu dá se říct, že je projekt naprosto hotov, neb jeho úkolem bylo dostat mě na úroveň, 
kdy s klidným svědomím mohu v daném oboru začít hledat práci a postupně se dále vyvíjet a růst.

Pokud si tyto řádky čte potenciální zaměstnavatel, kterému je kód v tomto projektu primárně určen, 
doufám, že odhlédne od toho, co ještě nevím, a bude pro něj podstatné, jak zacházím s tím, co už znám. 
Snažil jsem se jít co nejvíce cestou modulárního přístupu, ale zároveň se vyhnout přílišné fragmentaci.
Popisky mohou být pro někoho obsáhlejší, ale bral jsem to tak, že se smazat je je snadné, než napsat je. 

Na unit testy mi už vůbec nevyšel čas. Možná se k nim dostanu, pokud o mě nebude mít pracovně nikdo zájem. 
Ale počítám, že asi nebudou náročnější než cokoliv, s čím jsem se doposut setkal, 
a tak věřím, že nejsou ani tak náročné na schopnosti, jako spíše na čas.

Celkově jsem tedy připraven. A pokud sháníte někoho, na koho se můžete spolehnout, 
že se vždy bude snažit odvést dobrou práci, jsem tu pro vás. 
Programování mě baví, mám ho v krvi a svou práci beru jako svoji vizitku.
Je toho ještě asi hodně, co se budu muset učit, ale základy mám a jsou dobré.
Hlavně mám i chuť dále se rozvíjet a těším se na nové výzvy a schopnosti.

[Dalibor Sova](https://www.linkedin.com/in/dalibor-sudip-sova/)

