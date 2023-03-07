from django import forms

DIFFICULTY_CHOICES = (
    (1,"Easy"),
    (2,"Meduim"),
    (3,"Hard")
)

class QuestionForm(forms.Form):
    Question = forms.CharField(label='Question', max_length=512)
    Answer = forms.CharField(label='Answer', max_length=128)
    Difficulty = forms.ChoiceField(label="Difficulty", choices=DIFFICULTY_CHOICES)