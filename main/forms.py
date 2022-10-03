from django.forms import ModelForm
from .models import News, Events

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'featured_image', 'description', 'location']

class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = ['title', 'featured_image', 'description', 'location']