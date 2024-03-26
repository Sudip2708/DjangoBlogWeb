from django.db import models
from django.db.models import JSONField


class UserSettingsMixin(models.Model):
    sidebar_data = JSONField(default=dict)


    class Meta:
        abstract = True


    default_values = {
        "sidebar": True,
        "sidebar_search": {"value": True, "order": 1},
        "sidebar_search_options": False,
        "sidebar_user": {"value": True, "order": 2},
        "sidebar_user_user_menu": False,
        "sidebar_user_author_menu": False,
        "sidebar_category": {"value": True, "order": 3},
        "sidebar_category_options": True,
        "sidebar_category_navigation": True,
        "sidebar_tags": {"value": True, "order": 4},
        "sidebar_tags_options": True,
        "show_tab_for_similar": True,
    }


    def item_control(self):
        for key, value in self.default_values.items():
            if key not in self.sidebar_data:
                self.sidebar_data[key] = value


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Inicializace která kontroluje i zda má uživatel všechny položky
        if not self.sidebar_data:
            self.sidebar_data = self.default_values
        else:
            self.item_control()

        # Dynamické přidání vlastností na základě defaultních hodnot
        for key, value in self.default_values.items():
            if isinstance(value, dict):
                setattr(self.__class__, key, property(lambda self, k=key: self.sidebar_data[k]["value"]))
                setattr(self.__class__, f"{key}_order", property(lambda self, k=key: self.sidebar_data[k]["order"]))
            else:
                setattr(self.__class__, key, property(lambda self, k=key: self.sidebar_data[k]))


    def change_sidebar_value(self, field_key):
        """
        Změní hodnotu zadaného pole v postranním panelu na opačnou.
        """
        print("### def change_sidebar_value(self, field_key):")
        print("### field_key: ", field_key)

        # Ověření zda je hodnota přítomna jako klíč v sidebar_data
        if field_key in self.sidebar_data:

            # Ověří, zda se jedná o bool hodnotu, pokud ano, změní ji
            if isinstance(self.sidebar_data[field_key], bool):
                self.sidebar_data[field_key] = not self.sidebar_data[field_key]

            # Ověří, zda se jedná o slovník,pokud ano, změní v něm hodnotu
            elif isinstance(self.sidebar_data[field_key], dict):
                self.sidebar_data[field_key]["value"] = not self.sidebar_data[field_key]["value"]

            # uložení
            self.save()


    def find_sidebar_by_order(self, order):
        for i in self.sidebar_data:
            if isinstance(self.sidebar_data[i], dict):
                if self.sidebar_data[i]["order"] == order:
                    return self.sidebar_data[i]


    def sidebar_move(self, hash):
        movement = hash[0:7]
        sidebar = "sidebar" + hash[7:]

        if sidebar in self.sidebar_data:
            actual_sidebar = self.sidebar_data[sidebar]
            actual_position = actual_sidebar["order"]

            if movement == '#MoveUp':
                previous_position = actual_position - 1
                previous_sidebar = self.find_sidebar_by_order(previous_position)
                actual_sidebar["order"], previous_sidebar["order"] = previous_sidebar["order"], actual_sidebar["order"]

            elif movement == '#MoveDn':
                next_position = actual_position + 1
                next_sidebar = self.find_sidebar_by_order(next_position)
                actual_sidebar["order"], next_sidebar["order"] = next_sidebar["order"], actual_sidebar["order"]

            self.save()

