// Script pro nastavení zadávání tagů za pomoci tagify našeptávače

/*
Scrip je vložen v této šabloně:
main/templates/5_create_article/50__base__.html
Scrip je použit v těchto částech kodu:
main/templates/5_create_article/54__content__.html
*/

// Nastavení inicializace TinyMCE pro obsah článku
tinymce.init({

    // Výběr elementu pomocí selektoru CSS
    selector: 'textarea#id_content',

    // Minimální výška editoru v pixelech
    min_height: 800,

    // Povolené URL pro načítání obrázků (kvůli CORS)
    imagetools_cors_hosts: ['picsum.photos'],

    // Načtené pluginy TinyMCE
    plugins: ['advlist', 'anchor', 'autoresize', 'autosave', 'autolink',
              'charmap', 'code', 'codesample', 'emoticons', 'fullscreen', 'help',
              'image', 'insertdatetime', 'link', 'lists', 'media', 'nonbreaking',
              'pagebreak', 'preview', 'quickbars', 'searchreplace', 'table', 'template',
              'visualblocks', 'visualchars', 'wordcount'
             ],

    // Zobrazené položky v menu
    menubar: 'file edit view insert format tools table help',

    // Nástrojová lišta - část 1
    toolbar:  'undo redo |' +
              'styles fontfamily fontsizeinput lineheight forecolor backcolor |' +
              'bold italic underline |  charmap searchreplace selectall |' +
              'aligncenter alignjustify alignleft alignnone alignright |' +
              'indent outdent | bullist numlist  |' +
              'strikethrough subscript superscript removeformat hr nonbreaking |' +
              'blockquote visualblocks visualchars code codesample |' +
              'image emoticons insertdatetime anchor link openlink |' +  // **Nástrojová lišta - část 2**
              'cut copy paste pastetext | wordcount preview fullscreen |',

    // Udržuje nástrojovou lištu nahoře při scrollování
    toolbar_sticky: true,

    // Způsob zobrazení rozbalovací nabídky nástrojů
    toolbar_drawer: 'sliding',

    // Nástrojová lišta pro výběr textu
    quickbars_selection_toolbar: 'bold italic | quicklink h2 h3 blockquote quickimage quicktable',

    // Kontextové menu pro pravý klik
    contextmenu: "link image imagetools table",

    // Styly pro anotace TinyMCE
    content_style: '.mce-annotation { background: #fff0b7; } .tc-active-annotation {background: #ffe168; color: black; }',

    // Upozornění na neuložené změny
    autosave_ask_before_unload: true,

    // Zobrazení rozšířené záložky obrázků
    image_advtab: true,

    // Připojení vlastního CSS
    importcss_append: true,

    // Povolení popisků obrázků
    image_caption: true,

    // Třída pro neupravitelné prvky
    noneditable_noneditable_class: "mceNonEditable",

});


