from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profiles, Reports, Requests, Messages, SendMessages, Verificationss, WalkInProfiles
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Enter Username', 'class':'registerInput', 'required':'required'})
        self.fields['first_name'].widget.attrs.update({'placeholder':'Enter Full Name ex.John Paul M. Bual', 'class':'registerInput', 'required':'required'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'Enter Suffix ex.Jr.', 'class':'registerInput'})
        self.fields['email'].widget.attrs.update({'placeholder':'Enter Email ex.john@email.com', 'class':'registerInput'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Enter Password ex.Akosijohn12345', 'class':'registerInput', 'required':'required'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm Password', 'class':'registerInput', 'required':'required'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profiles
        fields = ['email','phone_number', 'blk_unit', 'phase_street', 'status', 'gender', 'vaccine', 'village', 'profile_image']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder':'Edit Email', 'class':'editUpdateAccountInput'})
        self.fields['blk_unit'].widget.attrs.update({'placeholder':'Edit Blk/Unit', 'class':'editUpdateAccountInput'})
        self.fields['phase_street'].widget.attrs.update({'placeholder':'Edit Phase/Street', 'class':'editUpdateAccountInput'})
        self.fields['status'].widget.attrs.update({'placeholder':'Edit Status', 'class':'editUpdateAccountInput'})
        self.fields['gender'].widget.attrs.update({'class':'editUpdateAccountInput'})
        self.fields['vaccine'].widget.attrs.update({'class':'editUpdateAccountInput'})
        self.fields['village'].widget.attrs.update({'class':'editUpdateAccountInput'})
        self.fields['phone_number'].widget.attrs.update({'placeholder':'Phone Number', 'class':'editUpdateAccountInput'})
        self.fields['profile_image'].widget.attrs.update({'class':'editUpdateAccountInput'})


class ReportsForm(ModelForm):
    class Meta:
        model = Reports
        fields = ['location', 'message']

    def __init__(self, *args, **kwargs):
        super(ReportsForm, self).__init__(*args, **kwargs)
        self.fields['location'].widget.attrs.update({'placeholder':'Enter Location', 'class':'reportsConcernInput', 'required':'required'})
        self.fields['message'].widget.attrs.update({'placeholder':'Your Message', 'class':'reportsConcernInput', 'required':'required'})

class RequestsForm(ModelForm):
    class Meta:
        model = Requests
        fields = ['document_type', 'purpose']

    def __init__(self, *args, **kwargs):
        super(RequestsForm, self).__init__(*args, **kwargs)
        self.fields['document_type'].widget.attrs.update({'class':'requestDocumentInput', 'required':'required'})
        self.fields['purpose'].widget.attrs.update({'placeholder':'Document Purpose' ,'class':'requestDocumentInput', 'required':'required'})



class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['document_type', 'purpose']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['document_type'].widget.attrs.update({'class':'sendMessageInputTextarea', 'required':'required'})
        self.fields['purpose'].widget.attrs.update({'placeholder':'Enter Purpose','class':'sendMessageInput'})


class SendMessageForm(ModelForm):
    class Meta:
        model = SendMessages
        fields = ['message']

    def __init__(self, *args, **kwargs):
        super(SendMessageForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'placeholder':'Enter Message','class':'sendMessageInput2'})


class VerificationForm(ModelForm):
    class Meta:
        model = Verificationss
        fields = ['brgy_id']

    def __init__(self, *args, **kwargs):
        super(VerificationForm, self).__init__(*args, **kwargs)
        self.fields['brgy_id'].widget.attrs.update({'class':'verificationInput', 'required':'required'})
        self.fields['brgy_id'].label = "Upload your Barangay I.D.:"


class VerifyProfileForm(ModelForm):
    class Meta:
        model = Profiles
        fields = ['verified']

    def __init__(self, *args, **kwargs):
        super(VerifyProfileForm, self).__init__(*args, **kwargs)
        self.fields['verified'].widget.attrs.update({'hidden':'hidden'})


class WalkInProfileForm(ModelForm):
    class Meta:
        model = WalkInProfiles
        fields = ['first_name','last_name','blk_unit','phase_street','email','phone_number','status','gender','vaccine','verified','village','profile_image']

    def __init__(self, *args, **kwargs):
        super(WalkInProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder':'First Name', 'class':'createProfileWalkInInput'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'Last Name', 'class':'createProfileWalkInInput'})
        self.fields['blk_unit'].widget.attrs.update({'placeholder':'Enter Blk/Unit', 'class':'createProfileWalkInInput'})
        self.fields['phase_street'].widget.attrs.update({'placeholder':'Enter Phase/Street', 'class':'createProfileWalkInInput'})
        self.fields['email'].widget.attrs.update({'placeholder':'Enter Email', 'class':'createProfileWalkInInput'})
        self.fields['phone_number'].widget.attrs.update({'placeholder':'Enter Phone Number', 'class':'createProfileWalkInInput'})
        self.fields['status'].widget.attrs.update({'placeholder':'Enter Status', 'class':'createProfileWalkInInput'})
        self.fields['gender'].widget.attrs.update({'class':'createProfileWalkInInput'})
        self.fields['vaccine'].widget.attrs.update({'class':'createProfileWalkInInput'})
        self.fields['verified'].widget.attrs.update({'class':'createProfileWalkInInput'})
        self.fields['village'].widget.attrs.update({'class':'createProfileWalkInInput'})
        self.fields['profile_image'].widget.attrs.update({'class':'createProfileWalkInInput'})
        self.fields['vaccine'].label = 'Vaccinated?'
        self.fields['verified'].label = 'Verified Resident?'
