from django import forms

DIFFICULTY_CHOICES = (
    ("Easy","Easy"),
    ("Meduim","Meduim"),
    ("Hard","Hard")
)

SIZE_CHOICES = (
    (2,2),
    (3,3)
)

class QuestionForm(forms.Form):
    Question = forms.CharField(label='Question', max_length=512)
    Answer = forms.CharField(label='Answer', max_length=128)
    Difficulty = forms.ChoiceField(label="Difficulty", choices=DIFFICULTY_CHOICES)
    Size = forms.CharField(max_length=10)

class AnswerForm(forms.Form):
    Answer = forms.CharField(label='Answer', max_length=128)

class AnswerFormReturned(forms.Form):
    Answer = forms.CharField(label='Answer', max_length=128)
    Question = forms.CharField(max_length=128)
    Size = forms.ChoiceField(choices=SIZE_CHOICES)

class LanguageForm(forms.Form):
    Language = forms.CharField(max_length=5)
    next = forms.CharField(max_length=128)