from django.db import models
from django.db.models import JSONField


class UserSettingsMixin(models.Model):
    sidebar_data = JSONField(default=dict)

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.sidebar_data:
            self.sidebar_data = {
                "sidebar_appearance": True,
                "sidebar_search": {"value": True, "order": 1},
                "sidebar_search_options": False,
                "sidebar_user": {"value": True, "order": 2},
                "sidebar_user_user_menu": False,
                "sidebar_user_author_menu": False,
                "sidebar_category": {"value": True, "order": 3},
                "sidebar_category_navigation": True,
                "sidebar_tags": {"value": True, "order": 4},
            }

    @property
    def sidebar(self):
        return self.sidebar_data["sidebar_appearance"]

    @property
    def sidebar_search(self):
        return self.sidebar_data["sidebar_search"]["value"]

    @property
    def sidebar_search_order(self):
        return self.sidebar_data["sidebar_search"]["order"]

    @property
    def sidebar_search_options(self):
        return self.sidebar_data["sidebar_search_options"]

    @property
    def sidebar_user(self):
        return self.sidebar_data["sidebar_user"]["value"]

    @property
    def sidebar_user_order(self):
        return self.sidebar_data["sidebar_user"]["order"]

    @property
    def sidebar_user_user_menu(self):
        return self.sidebar_data["sidebar_user_user_menu"]

    @property
    def sidebar_user_author_menu(self):
        return self.sidebar_data["sidebar_user_author_menu"]

    @property
    def sidebar_category(self):
        return self.sidebar_data["sidebar_category"]["value"]

    @property
    def sidebar_category_order(self):
        return self.sidebar_data["sidebar_category"]["order"]

    @property
    def sidebar_category_navigation(self):
        return self.sidebar_data["sidebar_category_navigation"]

    @property
    def sidebar_tags(self):
        return self.sidebar_data["sidebar_tags"]["value"]

    @property
    def sidebar_tags_order(self):
        return self.sidebar_data["sidebar_tags"]["order"]



    def change_sidebar_value(self, field_id):
        """
        Změní hodnotu zadaného pole v postranním panelu na opačnou.
        """
        if field_id in self.sidebar_data:
            if isinstance(self.sidebar_data[field_id], bool):  # Ověří, zda se jedná o bool hodnotu
                self.sidebar_data[field_id] = not self.sidebar_data[field_id]
            elif isinstance(self.sidebar_data[field_id], dict):  # Ověří, zda se jedná o slovník
                self.sidebar_data[field_id]["value"] = not self.sidebar_data[field_id]["value"]
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
            aktual_sidebar = self.sidebar_data[sidebar]
            aktual_position = aktual_sidebar["order"]

            if movement == '#MoveUp':
                previous_position = aktual_position - 1
                previous_sidebar = self.find_sidebar_by_order(previous_position)
                aktual_sidebar["order"], previous_sidebar["order"] = previous_sidebar["order"], aktual_sidebar["order"]

            elif movement == '#MoveDn':
                next_position = aktual_position + 1
                next_sidebar = self.find_sidebar_by_order(next_position)
                aktual_sidebar["order"], next_sidebar["order"] = next_sidebar["order"], aktual_sidebar["order"]

            self.save()

