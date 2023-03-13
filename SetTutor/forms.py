from django import forms

DIFFICULTY_CHOICES = (
    ("Easy","Easy"),
    ("Meduim","Meduim"),
    ("Hard","Hard")
)

class QuestionForm(forms.Form):
    Question = forms.CharField(label='Question', max_length=512)
    Answer = forms.CharField(label='Answer', max_length=128)
    Difficulty = forms.ChoiceField(label="Difficulty", choices=DIFFICULTY_CHOICES)

class AnswerForm(forms.Form):
    Answer = forms.CharField(label='Answer', max_length=128)

class AnswerFormReturned(forms.Form):
    Answer = forms.CharField(label='Answer', max_length=128)
    Question = forms.CharField(max_length=128)
    Difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES)

class LanguageForm(forms.Form):
    Language = forms.CharField(max_length=5)
    next = forms.CharField(max_length=128)