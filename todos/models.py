from django.db.models import Model
from django.db.models.fields import BooleanField, CharField, DateField, IntegerField

class Todo(Model):
    title = CharField(blank=True, max_length=100)
    content = CharField(blank=True, max_length=250)
    done = BooleanField(default=False)
    location = CharField(max_length=75, null=True, blank=True) # blank=True as not required in forms
    temp = IntegerField(null=True, blank=True) # blank=True as not required in forms
    created_at = DateField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
