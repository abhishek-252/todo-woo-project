from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm): # our custom form
    class Meta: # specifying what model we are working with
        model = Todo
        fields = ['title','memo','important']
