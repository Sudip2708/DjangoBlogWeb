// Script for setting up tag input using the tagify suggester

/*
This script is included in this template:
main/templates/0_base/_head/__scripts__.html
This script is used in these parts of the code:
main/templates/5_create_article/_settings/__tags__.html
*/

// Load the variable for the string of tags (passed from the template) and convert to a list
var tags_list = tags_name_str.split(',');

// Load the input field element where tagify should be used
var input = document.querySelector('input[name=tags]'),

// Override the behavior of the input field according to the set parameters
tagify = new Tagify(input, {

    // Set the maximum tag length to 20 characters
    pattern : /^.{0,20}$/,

    // Set the tag delimiter to a comma
    delimiters : ",",

    // Remove any spaces before and after the tag
    trim : true,

    // Remove invalid tags immediately after input
    keepInvalidTags : false,

    // Allow editing of already created tags with a double click and disable invalid tags as a result of the edit
    editTags : {
      clicks: 2,
      keepInvalid: false
    },

    // Set the maximum number of tags to 25 per article
    maxTags : 25,

    // Set the tag suggester (from the variable obtained from the template and converted to a list)
    whitelist : tags_list,

    // Set tag editing with the "Backspace" key press
    backspace : "edit",

    // Set the display of the suggester in the input field to one value and according to these parameters:
    // Display the value according to the initial letter, show it next to the text, and ignore case
    dropdown : {
        enabled: 1,
        fuzzySearch: false,
        position: 'text',
        caseSensitive: false
    },
})
