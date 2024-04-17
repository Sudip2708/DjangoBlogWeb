// Rozšíření pro main/static/js/_change_url_to_current_tab_[el].js

// Funkce pro změnu URL adresy na základě aktuální záložky
export function changeUrlToCurentTab(tabId) {
    /*
    Tato funkce slouží k změně URL adresy stránky na základě aktuální záložky.
    Pokud je záložka s daným identifikátorem nalezena, je její identifikátor vložen do URL adresy,
    což umožňuje aktualizovat adresu stránky podle aktuálně vybrané záložky.
    Tímto způsobem lze uživatelům poskytnout odkazy s konkrétními záložkami a udržet jejich stav i po obnovení stránky.
    V kodu se používá pro navrácení se na stránku a aktuální záložku z pohledu pro uložení změn.
    */

    // Načtení id kliknuté záložky a kontrola, zda obsahuje hodnotu
    const tabElement = document.getElementById(`${tabId}-tab`);
    if (tabElement) {

        // Získání aktuální URL
        const currentUrl = window.location.href;

        // Rozdělení cesta na seznam segmentů
        const pathSegments = currentUrl.split('/');

        // Nahrazení posledního neprázdného segmentu hodnotou tabId
        pathSegments[pathSegments.length - 2] = tabId;

        // Vytvoření nové URL
        const newUrl = pathSegments.join('/');

        // Nahrazení URL v historii stránky
        window.history.replaceState({}, document.title, newUrl);

    }
}