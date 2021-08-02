from django import forms


class PaginaForm(forms.Form):
    Title = forms.CharField(max_length=100)
    Markdown = forms.CharField(max_length=650,widget=forms.Textarea,label="Page body")



class EditarForm(forms.Form):
    txarea=forms.CharField(widget=forms.Textarea(),label="Page body")