from django import forms

class SettingsForm(forms.Form):
    THEME_CHOICES = [
        ('light', 'Светлая тема'),
        ('dark', 'Темная тема'),
        ('comic', 'Комикс стиль')
    ]

    LANGUAGE_CHOICES = [
        ('ru', 'Русский'),
        ('en', 'English')
    ]

    theme = forms.ChoiceField(
        choices=THEME_CHOICES,
        label='Тема оформления',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        label='Язык интерфейса',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    font_size = forms.IntegerField(
        label='Размер шрифта',
        min_value=12,
        max_value=24,
        initial=16,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )