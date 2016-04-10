from django import forms

from portal.models import Robot

class PostForm(forms.ModelForm):

    class Meta:
        model = Robot
        fields = ('task_number','task1_speed', 'task1_duration', 'task1_mode', 'task1_command')
