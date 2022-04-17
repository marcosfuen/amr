from django.db import models
from django.utils.timezone import now
import datetime

# Create your models here.


class AMRContador(models.Model):
    region = models.CharField('Región', max_length=150, blank=True, null=True)
    numeroCuenta = models.IntegerField(
        'Número de cuenta', blank=True, null=True)
    numeroCliente = models.IntegerField(
        'Número de cliente', blank=True, null=True)
    direccionDispositivo = models.CharField(
        'Dirección dispositivo', max_length=600, blank=True, null=True)
    numeroContador = models.CharField(
        'Número contador', max_length=150, blank=True, null=True)
    nombreContador = models.CharField(
        'Nombre contador', max_length=150, blank=True, null=True)
    latitude = models.FloatField('Latitud', blank=True, null=True)
    longitude = models.FloatField('Longitud', blank=True, null=True)
    email = models.EmailField('Correo', max_length=254, blank=True, null=True)
    telefono = models.CharField(
        'Teléfono', max_length=300, blank=True, null=True)

    def __str__(self):
        return self.nombreContador

    def __unicode__(self):
        return

    class Meta:
        db_table = 'g_AMRContador'
        managed = True
        verbose_name = 'AMRContador'
        verbose_name_plural = 'AMRContador'
        unique_together = ['numeroContador', ]


class Datos(models.Model):
    amrContador = models.ForeignKey(
        AMRContador, verbose_name='AMR', on_delete=models.SET_NULL, blank=True, null=True)
    tmpLectura = models.DateTimeField(
        'Tiempo de Lectura', default=now, blank=True, null=True)
    totalImpEnerg = models.FloatField(
        'Total importe de energía activa (kWh)', blank=True, null=True)
    t1ImpEnerg = models.FloatField(
        'T1 importe de energía activa (kWh)', blank=True, null=True)
    t2ImpEnerg = models.FloatField(
        'T2 importe de energía activa (kWh)', blank=True, null=True)
    t3ImpEnerg = models.FloatField(
        'T3 importe de energía activa (kWh)', blank=True, null=True)
    totalExpEnerg = models.FloatField(
        'Total exporte de energía activa (kWh)', blank=True, null=True)
    t1ExpEnerg = models.FloatField(
        'T1 exporte de energía activa (kWh)', blank=True, null=True)
    t2ExpEnerg = models.FloatField(
        'T2 exporte de energía activa (kWh)', blank=True, null=True)
    t3ExpEnerg = models.FloatField(
        'T3 exporte de energía activa (kWh)', blank=True, null=True)
    totalImpReacEnerg = models.FloatField(
        'Total importe de energía reactiva (kvarh)', blank=True, null=True)
    t1ImpMaxDeman = models.FloatField(
        'T1 importe activo maximo demandado (kW)', blank=True, null=True)
    t2ImpMaxDeman = models.FloatField(
        'T2 importe activo maximo demandado (kW)', blank=True, null=True)
    t3ImpMaxDeman = models.FloatField(
        'T3 importe activo maximo demandado (kW)', blank=True, null=True)
    t1ExpMaxDeman = models.FloatField(
        'T1 exporte activo maximo demandado (kW)', blank=True, null=True)
    t2ExpMaxDeman = models.FloatField(
        'T2 exporte activo maximo demandado (kW)', blank=True, null=True)
    t3ExpMaxDeman = models.FloatField(
        'T3 exporte activo maximo demandado (kW)', blank=True, null=True)
    imporActPoder = models.FloatField(
        'Importe activo de poder (kW)', blank=True, null=True)
    exporActPoder = models.FloatField(
        'Exporte activo de poder (kW)', blank=True, null=True)
    factPoder = models.FloatField(
        'Factor de poder', blank=True, null=True)
    faceAVolt = models.FloatField(
        'Face A de voltage (V)', blank=True, null=True)
    faceBVolt = models.FloatField(
        'Face B de voltage (V)', blank=True, null=True)
    faceCVolt = models.FloatField(
        'Face C de voltage (V)', blank=True, null=True)
    faceACurr = models.FloatField(
        'Face A de corriente (A)', blank=True, null=True)
    faceBCurr = models.FloatField(
        'Face B de corriente (A)', blank=True, null=True)
    faceCCurr = models.FloatField(
        'Face C de corriente (A)', blank=True, null=True)

    def __str__(self):
        return self.amrContador.nombreContador

    def __unicode__(self):
        return

    class Meta:
        db_table = 'g_Dato'
        managed = True
        verbose_name = 'Dato'
        verbose_name_plural = 'Datos'
