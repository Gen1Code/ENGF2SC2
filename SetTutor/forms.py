from django import forms
from django.utils.translation import gettext_lazy as _


DIFFICULTY_CHOICES = (
    ("Easy",_("Easy")),
    ("Medium",_("Medium")),
    ("Hard",_("Hard"))
)

TYPE_CHOICES = (
    (1,_("Simplify")),
    (2,_("Diagram"))
)

class QuestionForm(forms.Form):
    Question = forms.CharField(label=_('Question'), max_length=512)
    Difficulty = forms.ChoiceField(label=_("Difficulty"), choices=DIFFICULTY_CHOICES)
    Type = forms.ChoiceField(label=_("Type"), choices=TYPE_CHOICES,initial=2)

class AnswerFormReturned(forms.Form):
    Question = forms.CharField(max_length=128)
    Difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES)
    Type = forms.ChoiceField(choices=TYPE_CHOICES)
    Answer = forms.CharField(label='Answer', max_length=128)

class LanguageForm(forms.Form):
    Language = forms.CharField(max_length=5)
    next = forms.CharField(max_length=128)