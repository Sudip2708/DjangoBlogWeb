// Script pro nastavení editoru TinyMCE pro editaci HomePage

/*
Scrip je vložen v této šabloně:
main/templates/0_base/_head/__scripts__.html
Scrip je použit v těchto částech kodu:
main/templates/1_home/_hero/__edit_section__.html
main/templates/1_home/_intro/__edit_section__.html
main/templates/1_home/_divider/__edit_section__.html
main/templates/1_home/_latest_articles/__edit_section__.html
main/templates/1_home/_newsletter/__edit_section__.html
*/

// **Nastavení inicializace TinyMCE simple verze**
tinymce.init({

    // **Výběr elementu pomocí třídy CSS**
    selector: '.tinymce-simple',

    // **Použít pouze základní plugin a atomatické nastavování velikosti dle textu**
    plugins: ['basic', 'autoresize'],

    // **Skrytí položek menu**
    menubar: false,

    // **Základní nástrojová lišta**
    toolbar:  'styles fontfamily fontsizeinput | bold italic underline | lineheight | forecolor backcolor',

    // Skrytí loga TinyMCE
    branding: false,
    statusbar: false,
    // Nastavení výšky (dle textu)
    autoresize_bottom_margin: 25, // Dolní okraj editoru (v pixelech)
    autoresize_overflow_padding: 10, // Padding po stranách editoru (v pixelech)
    max_height: 500, // Maximální výška editoru (v pixelech)
    min_height: 50 // Minimální výška editoru (v pixelech)

});