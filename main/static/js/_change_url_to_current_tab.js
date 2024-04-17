// Skript na odchycení změny záložky na stránce pro vytvoření a úpravu článku
// Po zachycení klinutí na záložku, přepíše adresu stránky

/*
Scrip je vložen v této šabloně:
main/templates/5_create_article/50__base__.html
Scrip je použit v těchto částech kodu:
main/templates/5_create_article/52__page_navigation__.html
*/

// Načtení elementů z šablony a přiřazení do seznamu tabLinks
const tabLinks = document.querySelectorAll('[data-bs-toggle="tab"]');

// Odchycení kliknutí na záložku
document.addEventListener("DOMContentLoaded", function () {
    /*
    Přidání odposlouchávače událostí do všech elementů šablony obsahující hodnotu konstanty tabLinks,
    který po kliknutí spustí funkci changeUrlToCurentTab(tabId) pro změnu URL adresy na základě aktuální záložky.
    */

    // Přidání odposlouchávače událostí ke každému elementu ze seznamu tabLinks
    tabLinks.forEach(function (tabLink) {
        tabLink.addEventListener("click", function (event) {

            // Zabrání výchozímu chování odkazu
            event.preventDefault();

            // Získání tabId z atributu data-tab-id
            const tabId = this.getAttribute('data-tab-id');

            // Zavolejte funkci changeTab s tabId
            changeUrlToCurentTab(tabId);
        });
    });
});

// Změna adersy
function changeUrlToCurentTab(tabId) {

    // Načtení id kliknuté záložky
    const tabElement = document.getElementById(`${tabId}-tab`);
    if (tabElement) {

        // Získání aktuální URL
        const currentUrl = window.location.href;

        // Získání pole segmentů cesty
        const pathSegments = currentUrl.split('/');

        // Nahraďte poslední segment (neprázdný)
        pathSegments[pathSegments.length - 2] = tabId;

        // Vytvoření nové URL
        const newUrl = pathSegments.join('/');

        // Nahraďte aktuální stav historie novým URL
        window.history.replaceState({}, document.title, newUrl);

    }
}