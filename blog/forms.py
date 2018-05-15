## @brief Forms for the Blog app.

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Interest,Document,Rate,Community,Advertise,Profile
#from uploads.core.models import Document

## @brief This class represents the Form used to edit profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture','first_name', 'last_name', 'email',)

## @brief This class represents the Form used to sign-up
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    #email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    #prophoto = forms.ImageField(required=False)
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for fieldname in [ 'password1']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password1', 'password2',)

## @brief This class represents the Form used to edit interests of user
class InterestForm(forms.ModelForm):
	
	class Meta:
		model=Interest
		fields = ('my_field',)

## @brief This class represents the Form used to upload document
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title','author','genre','description', 'document', 'image','public')

## @brief This class represents the Form used to upload document in community
class DocumentCForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title','author','genre','description', 'document', 'image',)

## @brief This class represents the Form used to rate a book
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('rating',)

## @brief This class represents the Form used to create community
class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ('name','description',)

## @brief This class represents the Form used to upload advertise
class AdvertiseForm(forms.ModelForm):
    class Meta:
        model = Advertise
        fields = ('title','author','genre','description', 'image')
