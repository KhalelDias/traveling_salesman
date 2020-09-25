from django import forms

from ts.models import Url

CITY_CHOICES = [
    ('Nursultan', 'Нұр-сұлтан'),
    ('Almaty', 'Алматы'),
    ('Shymkent', 'Шымкент'),
    ('Kokshetau', 'Көкшетау'),
    ('Aktobe', 'Ақтөбе'),
    ('Taldykorgan', 'Талдықорған'),
    ('Atyrau', 'Атырау'),
    ('Ust-Kamenagorsk', 'Өскемен'),
    ('Taraz', 'Тараз'),
    ('Uralsk', 'Орал'),
    ('Karaganda', 'Қарағанды'),
    ('Kostanay', 'Қостанай'),
    ('Kyzylorda', 'Қызылорда'),
    ('Aktau', 'Ақтау'),
    ('Pavlodar', 'Павлодар'),
    ('Petropavlovsk', 'Петропавл'),
    ('Turkestan', 'Түркістан'),
    ('Semey', 'Семей'),
]


class CitiesForm(forms.Form):
    dep = forms.CharField(widget=forms.RadioSelect(choices=CITY_CHOICES), label="Выберите город вылета")
    dest = forms.CharField(widget=forms.CheckboxSelectMultiple(choices=CITY_CHOICES), label='Выберите города для визита')

    class Meta:
        exclude = ()


class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['long_url']
        labels = {
            'long_url': 'Введите URL'
        }
