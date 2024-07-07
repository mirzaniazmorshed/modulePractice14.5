from django import forms  
from django.forms.widgets import NumberInput
import datetime
class ContactForm(forms.Form):
    first_name = forms.CharField(
        initial="Mirza Niaz Morshed"
    )
    name = forms.CharField(
        max_length=20,
        min_length=10
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'rows':4}),
        required=False
    )
    email = forms.EmailField(
        label="Please enter your email..."
    )
    agree = forms.BooleanField(
        initial=True
    )
    date = forms.DateField(
        widget=NumberInput(attrs={'type':'date'}),
        initial=datetime.date.today
    )
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=['1980','1981','1982']))
    Amount = forms.DecimalField()
    favorite_color = forms.ChoiceField(
        choices=[
            ('blue','Blue'),
            ('green','Green'),
            ('black','Black')
        ]
    )
    favorite_languge = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[
            ('js','JavaScript'),
            ('php','PHP'),
            ('py','Python')
        ]
    )

    favorite_fruites = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[('banana','Banana'),('apple','Apple'),('mango','Mango')],)