// Script pro změnu popisů tlačítek rozklápěcích nabídek sidebaru a nastavení domácí stránky,
// a pro změnu přísleušné hodnoty v databázi - je-li to třeba.

/*
Scrip je použit v těchto částech kodu:
main/templates/1_home/_common/__edit_button__.html
main/templates/2_main/_sidebars/_common/__button_collapse__.html
main/templates/2_main/_sidebars/_common/__button_collapse_ajax__.html
*/

// Import funkcí
import { changeButtonText } from './_sidebar_settings_[fun]_change_text.js';
import { changeDatabaseValue } from './_sidebar_settings_[fun]_ajax_request.js';

// Seznam ID tlačítek pro __edit_button__.html
const editButton = [
    '#footerSectionCollapse',
    '#gallerySectionCollapse',
    '#heroSectionCollapse',
    '#introSectionCollapse',
    '#latestSectionCollapse',
    '#featuredSectionCollapse',
    '#dividerSectionCollapse',
    '#newsletterSectionCollapse'
];

// Seznam ID tlačítek pro __button_collapse__.html
const buttonCollapse = [
    '#sidebar_category',
    '#sidebar_search',
    '#sidebar_tags',
    '#sidebar_user'
];

// Seznam ID tlačítek pro __button_collapse_ajax__.html
const buttonCollapseAjax = [
    '#sidebar_category_options',
    '#sidebar_search_options',
    '#sidebar_tags_options',
    '#sidebar_user_author_menu',
    '#sidebar_user_user_menu'
];

// Seznam ID tlačítek pro funkci changeButtonText
const changeButtonTextButtons = editButton.concat(buttonCollapseAjax);

// Seznam ID tlačítek pro funkci toggleMenu
const changeDatabaseValueButtons = buttonCollapse.concat(buttonCollapseAjax);

// Získání všech vyklápěcích tlačítek
const buttons = document.querySelectorAll('[data-bs-toggle="collapse"]');

// Přidání event listeneru a následných akcí pro kliknutí na tlačítka
buttons.forEach(function(button) {
    /*
    Přidání odposlouchávače událostí do všech elementů šablony obsahující proměnou buttons,
    který po kliknutí spustí funkci changeButtonText(button) a changeDatabaseValue(menuId).
    */

    // Nastavení odposlouchávače
    button.addEventListener('click', function() {

        // Získání id nabídky z atributu data-bs-target
        const menuId = button.getAttribute('data-bs-target');
        // console.log("### menuIdXXX: " + menuId);

        // Spuštění funkce changeButtonText pro změnu textu, pokud je menuId obsaženo v seznamu
        if (changeButtonTextButtons.includes(menuId)) {
            // console.log("### changeButtonText(button)");
            changeButtonText(button);
        }

        // Spuštění funkce toggleMenu pro změnu hodnoty v databázi, pokud je menuId obsaženo v seznamu
        if (changeDatabaseValueButtons.includes(menuId)) {
            // console.log("### changeDatabaseValue(menuId)");
            changeDatabaseValue(menuId);
        }
    });
});




