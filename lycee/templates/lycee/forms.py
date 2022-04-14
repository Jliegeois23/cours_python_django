from django.forms.models import ModelForm
from lycee.models import Student

class StudentForm(ModelForm):
  class Meta:
    #le model u quel on se refere 
    model = Student

    # les champs qu'on veut voir apparaitre dans le formulaire 
    fields = (
      "first_name",
      "last_name",
      "birth_date",
      "email",
      "phone",
      "comments",
      "cursus",
    )