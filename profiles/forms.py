from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profiles, Reports, Requests, Messages, Verificationss


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Enter Username', 'class':'registerInput'})
        self.fields['first_name'].widget.attrs.update({'placeholder':'Enter First Name', 'class':'registerInput'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'Enter Last Name', 'class':'registerInput'})
        self.fields['email'].widget.attrs.update({'placeholder':'Enter Email', 'class':'registerInput'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Enter Password', 'class':'registerInput'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm Password', 'class':'registerInput'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profiles
        fields = ['email','address','status', 'gender', 'vaccine', 'profile_image']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder':'Edit Email', 'class':'editUpdateAccountInput'})
        self.fields['address'].widget.attrs.update({'placeholder':'Edit Address', 'class':'editUpdateAccountInput'})
        self.fields['status'].widget.attrs.update({'placeholder':'Edit Status', 'class':'editUpdateAccountInput'})
        self.fields['gender'].widget.attrs.update({'placeholder':'Edit Gender', 'class':'editUpdateAccountInput'})
        self.fields['vaccine'].widget.attrs.update({'placeholder':'Vaccinated?', 'class':'editUpdateAccountInput'})
        self.fields['profile_image'].widget.attrs.update({'class':'editUpdateAccountInput'})


class ReportsForm(ModelForm):
    class Meta:
        model = Reports
        fields = ['location', 'message']

    def __init__(self, *args, **kwargs):
        super(ReportsForm, self).__init__(*args, **kwargs)
        self.fields['location'].widget.attrs.update({'placeholder':'Enter Location', 'class':'reportsConcernInput'})
        self.fields['message'].widget.attrs.update({'placeholder':'Your Message', 'class':'reportsConcernInput'})

class RequestsForm(ModelForm):
    class Meta:
        model = Requests
        fields = ['document_type', 'purpose']

    def __init__(self, *args, **kwargs):
        super(RequestsForm, self).__init__(*args, **kwargs)
        self.fields['document_type'].widget.attrs.update({'class':'requestDocumentInput'})
        self.fields['purpose'].widget.attrs.update({'placeholder':'Document Purpose' ,'class':'requestDocumentInput'})



class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['your_message', 'your_file']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['your_message'].widget.attrs.update({'placeholder':'Enter Message' ,'class':'sendMessageInputTextarea'})
        self.fields['your_file'].widget.attrs.update({'class':'sendMessageInput'})


class VerificationForm(ModelForm):
    class Meta:
        model = Verificationss
        fields = ['address', 'brgy_id']

    def __init__(self, *args, **kwargs):
        super(VerificationForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({'placeholder':'Enter Address' ,'class':'verificationInput'})
        self.fields['brgy_id'].widget.attrs.update({'class':'verificationInput'})
        self.fields['brgy_id'].label = "Upload your Barangay I.D.:"


class VerifyProfileForm(ModelForm):
    class Meta:
        model = Profiles
        fields = ['verified']

    def __init__(self, *args, **kwargs):
        super(VerifyProfileForm, self).__init__(*args, **kwargs)
        self.fields['verified'].widget.attrs.update({'class':'editUpdateAccountInput'})