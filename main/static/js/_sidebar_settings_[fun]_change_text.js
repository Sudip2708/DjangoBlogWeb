// Rozšíření pro sidebar_settings.js

// Funkce pro změnu textu tlačítka na základě id nabídky
export function changeButtonText(button) {
    /*
    Tato funkce je volána při kliknutí na tlačítko a má za úkol změnit text tlačítka na základě stavu vyklápění menu.
    Funkce přijímá celé tlačítko jako argument.
    Aktualizuje text tlačítka na základě hodnoty atributu aria-expanded.
    */

    // Získání aktuální hodnoty aria-expanded
    var ariaExpanded = button.getAttribute('aria-expanded');

    // Rozdělení textu na část s Hide/Show a zbytek textu
    var splitText = button.textContent.trim().split(' ');
    var actionText = splitText[0];
    var remainingText = splitText.slice(1).join(' ');

    // Aktualizace textu tlačítka podle hodnoty aria-expanded
    if (ariaExpanded === 'true') {
        button.textContent = 'Hide ' + remainingText;
    } else {
        button.textContent = 'Show ' + remainingText;
    }
}