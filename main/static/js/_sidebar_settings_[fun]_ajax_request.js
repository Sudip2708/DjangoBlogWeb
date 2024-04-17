// Rozšíření pro sidebar_settings.js

// Funkce pro odeslání AJAX požadavku pro změnu hodnoty pro nastavení sidebaru v databázi
export function changeDatabaseValue(menuId) {
    /*
    Tato funkce je volána při kliknutí na vyklápěcí tlačítko a má za úkol odeslat AJAX požadavek na server.
    Do dat požadavku přidá identifikátor nabídky (menuId) a předaný CSRF token.
    */

    // Odeslání AJAX požadavku na server
    $.ajax({

        // URL adresy a typ požadavku
        url: '/user_sidebar/appearance/',
        type: 'POST',

        // Data: Identifikátor nabídky + CSRF token (předaný z šablony)
        data: {
            'menu_id': menuId,
            csrfmiddlewaretoken: csrftoken
        },

        // Úkony provedené po úspěšném provedení
        success: function(response) {
            // Zde můžeš přidat další zpracování úspěšné odpovědi, pokud je potřeba
        },

        // Úkony provedené po neúspěšném provedení
        error: function(xhr, errmsg, err) {
            // Zde můžeš přidat další zpracování chybové odpovědi, pokud je potřeba
        }

    });

}