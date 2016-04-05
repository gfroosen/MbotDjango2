from django import forms

from portal.models import Robot

class PostForm(forms.ModelForm):

    class Meta:
        model = Robot
        fields = ('task_number',)
