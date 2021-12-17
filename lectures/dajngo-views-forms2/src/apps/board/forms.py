from django import forms


class CommentForm(forms.Form):
    message = forms.CharField(max_length=255)
