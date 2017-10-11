from .models import School,Dpts_985
from django.forms import ModelForm,Form

class SchoolForm(Form):
    
    class Meta:
        model= Dpts_985
        fields=('__all__')#'__all__'"school"




