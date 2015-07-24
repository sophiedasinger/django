from django import forms
from blog.models import Post
from blog.models import Category
from django.contrib.admin.widgets import FilteredSelectMultiple
from chosen import forms as chosenforms


class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'body', 'category']
    	category= chosenforms.ChosenModelMultipleChoiceField(queryset=Category.objects.all(), widget=chosenforms.ChosenSelectMultiple, required=False)

        







