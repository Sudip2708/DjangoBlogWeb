// Script for setting up TinyMCE editor for article editing

/*
This script is included in this template:
main/templates/0_base/_head/__scripts__.html
This script is used in these parts of the code:
main/templates/5_create_article/52__content__.html
*/

// Configuration for initializing TinyMCE for article content
tinymce.init({

    // Selecting the element using CSS selector
    selector: 'textarea#id_content',

    // Minimum height of the editor in pixels
    min_height: 800,

    // Allowed URLs for loading images (due to CORS)
    imagetools_cors_hosts: ['picsum.photos'],

    // Loaded TinyMCE plugins
    plugins: ['advlist', 'anchor', 'autoresize', 'autosave', 'autolink',
              'charmap', 'code', 'codesample', 'emoticons', 'fullscreen', 'help',
              'image', 'insertdatetime', 'link', 'lists', 'media', 'nonbreaking',
              'pagebreak', 'preview', 'quickbars', 'searchreplace', 'table', 'template',
              'visualblocks', 'visualchars', 'wordcount'
             ],

    // Displayed items in the menu
    menubar: 'file edit view insert format tools table help',

    // Toolbar - part 1
    toolbar:  'undo redo |' +
              'styles fontfamily fontsizeinput lineheight forecolor backcolor |' +
              'bold italic underline |  charmap searchreplace selectall |' +
              'aligncenter alignjustify alignleft alignnone alignright |' +
              'indent outdent | bullist numlist  |' +
              'strikethrough subscript superscript removeformat hr nonbreaking |' +
              'blockquote visualblocks visualchars code codesample |' +
              'image emoticons insertdatetime anchor link openlink |' +  // **Toolbar - part 2**
              'cut copy paste pastetext | wordcount preview fullscreen |',

    // Keep the toolbar at the top when scrolling
    toolbar_sticky: true,

    // How the toolbar drawer is displayed
    toolbar_drawer: 'sliding',

    // Toolbar for text selection
    quickbars_selection_toolbar: 'bold italic | quicklink h2 h3 blockquote quickimage quicktable',

    // Context menu for right-click
    contextmenu: "link image imagetools table",

    // Styles for TinyMCE annotations
    content_style: '.mce-annotation { background: #fff0b7; } .tc-active-annotation {background: #ffe168; color: black; }',

    // Warning for unsaved changes
    autosave_ask_before_unload: true,

    // Display the advanced image tab
    image_advtab: true,

    // Attach custom CSS
    importcss_append: true,

    // Enable image captions
    image_caption: true,

    // Class for non-editable elements
    noneditable_noneditable_class: "mceNonEditable",

});
