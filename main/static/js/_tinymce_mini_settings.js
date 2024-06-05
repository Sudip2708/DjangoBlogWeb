// Script for setting up TinyMCE editor for editing the HomePage

/*
This script is included in this template:
main/templates/0_base/_head/__scripts__.html
This script is used in these parts of the code:
main/templates/1_home/_hero/__edit_section__.html
main/templates/1_home/_intro/__edit_section__.html
main/templates/1_home/_divider/__edit_section__.html
main/templates/1_home/_latest_articles/__edit_section__.html
main/templates/1_home/_newsletter/__edit_section__.html
*/

// Configuration for initializing the simple version of TinyMCE
tinymce.init({

    // Selecting the element using CSS class
    selector: '.tinymce-simple',

    // Use only basic plugin and automatic resizing based on text
    plugins: ['basic', 'autoresize'],

    // Hide menu items
    menubar: false,

    // Basic toolbar
    toolbar:  'styles fontfamily fontsizeinput | bold italic underline | lineheight | forecolor backcolor',

    // Hide TinyMCE branding
    branding: false,
    statusbar: false,

    // Set height (based on text)
    autoresize_bottom_margin: 25, // Bottom margin of the editor (in pixels)
    autoresize_overflow_padding: 10, // Padding on the sides of the editor (in pixels)
    max_height: 500, // Maximum height of the editor (in pixels)
    min_height: 50 // Minimum height of the editor (in pixels)

});
