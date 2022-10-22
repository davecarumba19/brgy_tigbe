from django.forms import ModelForm
from .models import News, Events

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'featured_image', 'description', 'location']

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder':'Enter Title' ,'class':'createUpdateEventsNewsInput'})
        self.fields['featured_image'].widget.attrs.update({'class':'createUpdateEventsNewsInput'})
        self.fields['description'].widget.attrs.update({'placeholder':'Enter Description' ,'class':'createUpdateEventsNewsTextarea'})
        self.fields['location'].widget.attrs.update({'placeholder':'Your Location' ,'class':'createUpdateEventsNewsInput'})
    

class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = ['title', 'featured_image', 'description', 'location']

    def __init__(self, *args, **kwargs):
        super(EventsForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder':'Enter Title' ,'class':'createUpdateEventsNewsInput'})
        self.fields['featured_image'].widget.attrs.update({'class':'createUpdateEventsNewsInput'})
        self.fields['description'].widget.attrs.update({'placeholder':'Enter Description' ,'class':'createUpdateEventsNewsTextarea'})
        self.fields['location'].widget.attrs.update({'placeholder':'Your Location' ,'class':'createUpdateEventsNewsInput'})