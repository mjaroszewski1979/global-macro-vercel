from django import forms

class MyForm(forms.Form):
    website = forms.CharField(label='WEBSITE', max_length=200)
    keyword = forms.CharField(label='KEYWORD', max_length=200)
    pages = forms.IntegerField(label='PAGES', max_value=10, min_value=1)
    csv = forms.BooleanField(label='CSV', required=False)