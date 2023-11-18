from django import forms
from .models import Mountaineer, Activity

class MountaineerActivityForm(forms.ModelForm):
    class Meta:
        model = Mountaineer
        fields = ['activity']

    def __init__(self, *args, **kwargs):
        super(MountaineerActivityForm, self).__init__(*args, **kwargs)
        self.fields['activity'].queryset = Activity.objects.all()