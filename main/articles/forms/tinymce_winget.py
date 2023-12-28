### Definuje formuláře (na webu) pro aplikaci.

from tinymce.widgets import TinyMCE


class TinyMCEWidget(TinyMCE):
    # Předefinování metody use_required_attribute pro zakázání vyžadovaného atributu pro TinyMCEWidget
    def use_required_attribute(self, *args):
        return False
