// Script pro přepnutí se na požadovanou záložku stránky dle hodnoty z URL

/*
Scrip je vložen v této šabloně:
main/templates/5_create_article/50__base__.html
Scrip je použit v těchto částech kodu:
main/templates/5_create_article/52__page_navigation__.html
*/

// Nastavení odposlouchávače
document.addEventListener("DOMContentLoaded", function () {
    /*
    Tento skript odposlouchá událost DOMContentLoaded, což je událost spuštěná po načtení stránky.
    Skript provede kontrolu, zda je uživatel na stránce pro úpravu příspěvku.
    Pokud ano získá část URL adresy obsahující identifikátor záložky.
    Vytvoří URL adresu s přidáním identifikátoru jako kotvy.
    Zkontroluje existenci kotvy na stránce se shodným identifikátorem.
    Pokud kotva existuje, vyvolá její simulované kliknutí.
    */

    // Extrahovíní URL
    const pathFromURL = window.location.pathname;

    // Rozložení URL
    const pathSegments = pathFromURL.split('/').filter(Boolean);

    // Vytažení předposlední části
    const pathFromURL_last_last = pathSegments[pathSegments.length - 2];

    // Kontrola, zda jsme na stránce pro úpravu příspěvku
    if (pathFromURL_last_last === 'update') {

        // Vytažení poslední části
        const pathFromURL_last = pathSegments[pathSegments.length - 1];

        // Přidání znaku # před poslední část
        const pathWithHash = `#${pathFromURL_last}`;

        // Ověření existence kotvy s href="#content"
        const contentAnchor = document.querySelector(`a[href="${pathWithHash}"]`);
        if (contentAnchor) {

            // Simulace kliknutí na odkaz
            contentAnchor.click();

        } else {
            // console.log("Kotva s href=\"#content\" nebyla nalezena.");
        }

    }

});