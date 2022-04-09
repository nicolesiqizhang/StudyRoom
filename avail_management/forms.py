import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class NewOrderForm(forms.Form):
    start_date = forms.DateField(widget = forms.SelectDateWidget)
    end_date = forms.DateField(widget = forms.SelectDateWidget)
    customer_name = forms.CharField(label='Customer name', max_length=64)
    staff_name = forms.CharField(label='Staff name', max_length=64)

    # The naming must match the field name, otherwise it would fail.
    def clean_end_date(self):
        data = self.cleaned_data['end_date']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - end in past'))
        return data
