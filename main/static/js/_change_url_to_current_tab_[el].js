// Skript na odchycení změny záložky na stránce pro vytvoření a úpravu článku
// Skript po zachyccení klinutí na záložku, přepíše adresu stránky

/*
Scrip je použit v těchto částech kodu:
main/templates/5_create_article/52__page_navigation__.html
*/

// Import funkce
import { changeUrlToCurentTab } from './_change_url_to_current_tab_[fun].js';

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