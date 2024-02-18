from django.db import models

class OrderedBooleanField(models.BooleanField):
    """
    Pole boolean s informací o pořadí.
    """
    def __init__(self, *args, **kwargs):
        self.order = kwargs.pop('order', None)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['order'] = self.order
        return name, path, args, kwargs

    def move_up(self):
        """
        Posune toto pole nahoru o jedno místo.
        """
        if self.order is not None and self.order > 1:
            prev_item = type(self).objects.filter(order=self.order - 1).first()
            if prev_item:
                self.order, prev_item.order = prev_item.order, self.order
                self.save()
                prev_item.save()

    def move_down(self):
        """
        Posune toto pole dolu o jedno místo.
        """
        if self.order is not None:
            next_item = type(self).objects.filter(order=self.order + 1).first()
            if next_item:
                self.order, next_item.order = next_item.order, self.order
                self.save()
                next_item.save()
