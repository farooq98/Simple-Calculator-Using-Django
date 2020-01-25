from django import forms
from maths.models import math

class calculation(forms.ModelForm):
    class Meta:
        model = math
        fields = "__all__"
