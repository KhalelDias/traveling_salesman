from django import forms

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
    ('Petropavl', 'Петропавл'),
    ('Turkestan', 'Түркістан'),
    ('Semey', 'Семей'),
]


class CitiesForm(forms.Form):
    dep = forms.CharField(widget=forms.RadioSelect(choices=CITY_CHOICES), label="Выберите город отлета")
    dest = forms.CharField(widget=forms.CheckboxSelectMultiple(choices=CITY_CHOICES), label='Выберите города для визита')

    class Meta:
        exclude = ()
