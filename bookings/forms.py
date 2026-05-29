from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

        def clean(self):
            cleaned_date = super().clean()
            start = cleaned_date.get('start_time')
            end = cleaned_date.get('end_time')

            if start > end:
                if end < start:
                    raise forms.ValidationError('Время окончания должно быть позже начала!')
                if (end.hour - start.hour) < 1:
                    raise forms.ValidationError('Минимальное бронирование — 1 час!')

            return cleaned_date