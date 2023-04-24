from django import forms

class ContentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":15, "cols":200}), max_length=1000, help_text="1000 characters max.")