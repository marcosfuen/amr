from django import forms
from django.contrib.auth.models import User
from django.forms.fields import ChoiceField
from django.forms.widgets import DateTimeInput, RadioSelect, Select, TextInput, Textarea, EmailInput, Textarea, URLInput, NumberInput
from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import AMRContador, Datos


class AMRContadorForm(forms.ModelForm):
    class Meta:
        model = AMRContador
        fields = ['region', 'numeroCuenta',
                  'numeroCliente', 'direccionDispositivo',
                  'numeroContador', 'nombreContador', 'latitude', 'longitude',
                  'email', 'telefono'
                  ]
        widgets = {
            'region': TextInput(attrs={'class': 'form-control', 'placeholder': 'Region'}),
            'numeroCuenta': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Número de cuenta'}),
            'numeroCliente': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Número de cliente'}),
            'direccionDispositivo': Textarea(attrs={'class': 'form-control', 'placeholder': 'Dirección del metro'}),
            'numeroContador': TextInput(attrs={'class': 'form-control', 'placeholder': 'Número del metro'}),
            'nombreContador': TextInput(attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Nombre del metro'}),
            'latitude': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Latitude'}),
            'longitude': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Longitude'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'telefono': TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),


        }


class DatosForm(forms.ModelForm):

    class Meta:
        model = Datos
        # fields = '__all__'
        fields = ['amrContador', 'tmpLectura',
                  'totalImpEnerg', 't1ImpEnerg', 't2ImpEnerg',
                  't3ImpEnerg', 'totalExpEnerg', 't1ExpEnerg',
                  't2ExpEnerg', 't3ExpEnerg', 'totalImpReacEnerg',
                  't1ImpMaxDeman', 't2ImpMaxDeman', 't3ImpMaxDeman',
                  't1ExpMaxDeman', 't2ExpMaxDeman', 't3ExpMaxDeman',
                  'imporActPoder', 'exporActPoder', 'factPoder',
                  'faceAVolt', 'faceBVolt', 'faceCVolt', 'faceACurr',
                  'faceBCurr', 'faceCCurr'
                  ]
        widgets = {
            'amrContador': Select(attrs={'class': 'chosen', 'placeholder': 'Seleccione un metro contador'}, choices=(AMRContador.objects.none())),
            'totalImpEnerg': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total importe de energía activa (kWh)'}),
            't1ImpEnerg': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'T1 importe de energía activa (kWh)'}),
            't2ImpEnerg': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'T2 importe de energía activa (kWh)'}),
            't3ImpEnerg': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'T3 importe de energía activa (kWh)'}),
            'totalExpEnerg': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Total exporte de energía activa (kWh)'}),
            't1ExpEnerg': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'T1 exporte de energía activa (kWh)'}),
            't2ExpEnerg': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'T2 exporte de energía activa (kWh)'}),
            't3ExpEnerg': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'T3 exporte de energía activa (kWh)'}),
            'totalImpReacEnerg': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Total importe de energía reactiva (kvarh)'}),
            't1ImpMaxDeman': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'T1 importe activo maximo demandado (kW)'}),
            't2ImpMaxDeman': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'T2 importe activo maximo demandado (kW)'}),
            't3ImpMaxDeman': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'T3 importe activo maximo demandado (kW)'}),
            't1ExpMaxDeman': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'T1 exporte activo maximo demandado (kW)'}),
            't2ExpMaxDeman': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'T2 exporte activo maximo demandado (kW)'}),
            't3ExpMaxDeman': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'T3 exporte activo maximo demandado (kW)'}),
            'imporActPoder': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Importe activo de poder (kW)'}),
            'exporActPoder': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Exporte activo de poder (kW)'}),
            'factPoder': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Factor de poder'}),
            'faceAVolt': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Face A de voltage (V)'}),
            'faceBVolt': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Face B de voltage (V)'}),
            'faceCVolt': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Face C de voltage (V)'}),
            'faceACurr': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Face A de corriente (A)'}),
            'faceBCurr': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Face B de corriente (A)'}),
            'faceCCurr': NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Face C de corriente (A)'}),

            # 'tmpLectura': DateTimeInput(attrs={
            #     'class': 'form-control',
            #     'id': 'datetimepicker1',
            #     'placeholder': 'Fecha/Hora Inicio'
            # }, format='%Y-%m-%d %H:%M:%S'),
            # 'endDate': DateTimeInput(attrs={
            #     'class': 'form-control',
            #     'id': 'datetimepicker2',
            #     'placeholder': 'Fecha/Hora Fin'
            # }, format='%Y-%m-%d %H:%M:%S'),
            # 'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono (Opcional)'}),

            # 'url': URLInput(attrs={'class': 'form-control', 'placeholder': 'Url de la video (Opcional)'}),

        }
