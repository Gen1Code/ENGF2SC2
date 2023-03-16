from django import forms

DIFFICULTY_CHOICES = (
    ("Easy","Easy"),
    ("Meduim","Meduim"),
    ("Hard","Hard")
)

TYPE_CHOICES = (
    (1,"Simplify"),
    (2,"Diagram")
)

class QuestionForm(forms.Form):
    Question = forms.CharField(label='Question', max_length=512)
    Difficulty = forms.ChoiceField(label="Difficulty", choices=DIFFICULTY_CHOICES)
    Type = forms.ChoiceField(label="Type", choices=TYPE_CHOICES)

class AnswerFormReturned(forms.Form):
    Question = forms.CharField(max_length=128)
    Difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES)
    Type = forms.ChoiceField(choices=TYPE_CHOICES)
    Answer = forms.CharField(label='Answer', max_length=128)

class LanguageForm(forms.Form):
    Language = forms.CharField(max_length=5)
    next = forms.CharField(max_length=128)