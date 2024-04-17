// Script pro nastavení editoru TinyMCE pro editaci článků

/*
Scrip je vložen v této šabloně:
main/templates/0_base/_head/__scripts__.html
Scrip je použit v těchto částech kodu:
main/templates/5_create_article/_settings/__tags__.html
*/

// Načtení proměné pro řetězec tagů (předaný z šablony) a převod na seznam
var tags_list = tags_name_str.split(',');

// Načtení elementu vstupního pole, kde má být použit tagify
var input = document.querySelector('input[name=tags]'),

// Přepsání chování vstupního pole dle nastavených parametrů
tagify = new Tagify(input, {

    // Nastavení maximální délky tagu na 20 znaků.
    pattern : /^.{0,20}$/,

    // Nastavení oddělování tagů, za pomoci čárky
    delimiters : ",",

    // Nastavení odebrání případných mezer před a za tagem.
    trim : true,

    // Nastavení odstranění neplatných tagů přímo po zadání
    keepInvalidTags : false,

    // Nastavení editace již vytvořených tagů dvojitým klikem a zakázání nepovolených tagů jako výsledek úpravi
    editTags : {
      clicks: 2,
      keepInvalid: false
    },

    // Nastavení maximálního počtu tagů na 25 pro jeden článek
    maxTags : 25,

    // Nastavení našeptávače tagů (z proměné získané ze šablony a převedené na seznam)
    whitelist : tags_list,

    // Nastavení editace tagu při stisku klávesy "Backspace"
    backspace : "edit",

    // Nastavení zobrazení našeptávače v poli zadávání na jednu hodnotu a dle těchto parametrů:
    // Hodnotu zobrazit dle počátečního písmena, zobrazit ji u textu a nerozlišovat mezi velkým a malým písmenem.
    dropdown : {
        enabled: 1,
          fuzzySearch: false,
          position: 'text',
          caseSensitive: false
    },
})



