# -*- coding: utf-8 -*-

from django import forms
from django.db.models import Q
from .models import Todo, Firm, Work


class TodoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        qs_base = Firm.objects.filter(show_in_list=True)
        if self.initial and self.initial['firm']:
            self.fields['firm'].queryset = qs_base | Firm.objects.filter(id=self.initial['firm'])
        else:
            self.fields['firm'].queryset = qs_base

    class Meta:
        model = Todo
        fields = ['firm', 'date', 'todo', 'finished']


class WorkForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(WorkForm, self).__init__(*args, **kwargs)
        qs_base = Firm.objects.filter(show_in_list=True)
        if self.initial and self.initial['firm']:
            self.fields['firm'].queryset = qs_base | Firm.objects.filter(id=self.initial['firm'])
        else:
            self.fields['firm'].queryset = qs_base

    class Meta:
        model = Work
        fields = ['firm', 'date', 'item_price', 'items', 'what_brief', 'what_detailed']
