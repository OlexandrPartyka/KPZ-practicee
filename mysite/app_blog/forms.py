# -*- coding: utf-8 -*-
from django import forms
from .models import ArticleImage


class MultiClearableFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


    def value_from_datadict(self, data, files, name):




        if name in files:
            file_list = files.getlist(name)
            if file_list:
                return file_list[0]
        return super().value_from_datadict(data, files, name)


class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=MultiClearableFileInput(attrs={'multiple': True})
    )


    class Meta:
        model = ArticleImage
        fields = '__all__'