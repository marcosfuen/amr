import json
import pytz
from django.utils import timezone
from datetime import datetime
from os.path import getatime, getctime

from django.contrib.auth.decorators import login_required
from django.db.models import Count, F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from pandas.tseries.offsets import Minute

from .forms import AMRContadorForm, DatosForm
from .models import AMRContador, Datos

# Create your views here.


@login_required(login_url='/')
def profile(request):
    allAmr = AMRContador.objects.all()
    allAmr1 = AMRContador.objects.all()
    from datetime import datetime
    today = datetime.today()
    # date1 = datetime(year=today.year, month=today.month,
    #                  day=today.day, hour=4, minute=0)
    date1 = datetime(year=today.year, month=today.month, day=today.day, hour=0, minute=0)
    ultimaLectura = Datos.objects.filter(
        tmpLectura=date1).values_list('amrContador__nombreContador', 'totalImpEnerg')
    print(ultimaLectura)
    allMetroPorDia = Datos.objects.filter(
        tmpLectura=date1).values_list('amrContador__nombreContador', flat=True)
    allImportMetroPorDia = Datos.objects.filter(
        tmpLectura=date1).annotate(name=F('amrContador__nombreContador'), data=F('totalImpEnerg')).values('name', 'data')
    for a in allAmr:
        result = Datos.objects.filter(
            amrContador__nombreContador=a).values_list('totalImpEnerg', flat=True).order_by('tmpLectura')
    data1 = []
    dataAll = []
    import datetime
    today1 = datetime.date.today()
    first = today1.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)
    start_date = datetime.date(lastMonth.year, lastMonth.month, 1)
    end_date = datetime.date(lastMonth.year, lastMonth.month, lastMonth.day)
    new_end = end_date + datetime.timedelta(days=1)
    tiempoLectura = []
    lolo = []
    for c in allImportMetroPorDia:
        data1.append({'name': c['name'], 'data': [c['data']]})
    from datetime import datetime
    print(Datos.objects.filter(
        amrContador__nombreContador=a).filter(tmpLectura__range=(start_date, new_end)).values_list('totalImpEnerg', flat=True).order_by('tmpLectura').count())
    print(Datos.objects.filter(amrContador__nombreContador=a).filter(tmpLectura__range=(
        start_date, new_end)).values_list('tmpLectura', flat=True).order_by('tmpLectura').count())
    for a in allAmr:
        dataAll.append({'name': str(a), 'data': list(Datos.objects.filter(
            amrContador__nombreContador=a).filter(tmpLectura__range=(start_date, new_end)).values_list('totalImpEnerg', flat=True).order_by('tmpLectura'))})
        # tiempoLectura.append(Datos.objects.filter(
        #     amrContador__nombreContador=a).filter(tmpLectura__range=(start_date, end_date)).values_list('tmpLectura', flat=True).order_by('tmpLectura'))
        for i in list(Datos.objects.filter(amrContador__nombreContador=a).filter(tmpLectura__range=(start_date, new_end)).values_list('tmpLectura', flat=True).order_by('tmpLectura')):
            # print(timezone.localtime(i))
            lolo.append(datetime.strftime(
                timezone.localtime(i), '%Y-%m-%d %H:%M:%S'))
            # lolo.append(datetime.strftime(i, '%Y-%m-%d %T'))
    for a1 in allAmr1:
        print(a1.latitude, a1.longitude)
    context = {
        'allAmr': allAmr,
        'allAmr1': allAmr1,
        'allMetroPorDia': allMetroPorDia,
        'data1': data1,
        'dataAll': dataAll,
        'tiempoLectura': tiempoLectura,
        'lolo': lolo,
        'ultimaLectura': ultimaLectura

    }
    # lolo = json.dumps(list(allImportMetroPorDia))
    # print(allImportMetroPorDia)
    return render(request, 'profile.html', context)


@ login_required(login_url='/')
def adicionarDatosAMR(request):
    okMensaje = ''
    form = DatosForm()
    if request.method == 'POST':
        form = DatosForm(request.POST)
        if form.is_valid():
            newDatoAmr = form.save()
            okMensaje = 'Se adicionarón los datos correctamente.'
            # return redirect('../')
            # return HttpResponseRedirect(reverse('gEnergetica:datosAmr'))
    else:
        form = DatosForm()
    context = {
        'form': form,
        'okMensaje': okMensaje,
    }
    return render(request, 'datosAmr.html', context)


@ login_required(login_url='/')
def adicionarDatosMetroContador(request):
    okMensaje = ''
    form = AMRContadorForm()
    if request.method == 'POST':
        form = AMRContadorForm(request.POST)
        if form.is_valid():
            newAmr = form.save()
            okMensaje = 'Se adicionarón los datos correctamente.'
            # return redirect('../')
            # return HttpResponseRedirect(reverse('gEnergetica:datosAmr'))
    else:
        form = AMRContadorForm()
    context = {
        'form': form,
        'okMensaje': okMensaje,
    }
    return render(request, 'datoMetroContador.html', context)


def detail(request, amrId):
    amr = get_object_or_404(AMRContador, id=amrId)
    details = Datos.objects.filter(amrContador__nombreContador=amr).values_list(
        'totalImpEnerg', flat=True).order_by('totalImpEnerg')
    # filtro semanal total de energia
    # filtro mensual total de energia
    # filtro de un dia espesifico
    # filtro por los tres transformadores de energia activa (kwh)
    transImpEnerg = []
    transExpEnerg = []
    today = datetime.today()
    dateFilter = datetime(year=today.year, month=today.month,
                          day=today.day, hour=0, minute=0)
    transImpDato = Datos.objects.filter(amrContador__nombreContador=amr).filter(tmpLectura=dateFilter).values_list(
        't1ImpEnerg', 't2ImpEnerg', 't3ImpEnerg').order_by('totalImpEnerg')
    transExpDato = Datos.objects.filter(amrContador__nombreContador=amr).filter(tmpLectura=dateFilter).values_list(
        't1ImpMaxDeman', 't2ImpMaxDeman', 't3ImpMaxDeman').order_by('totalImpEnerg')
    details1 = Datos.objects.filter(amrContador__nombreContador=amr).filter(tmpLectura=dateFilter).values_list(
        'totalImpEnerg', flat=True).order_by('totalImpEnerg').first()
    for tran in transImpDato:
        for i in Datos.objects.filter(amrContador__nombreContador=amr).filter(tmpLectura=dateFilter).values_list('tmpLectura', flat=True).order_by('totalImpEnerg'):
            transImpEnerg.append({'name': datetime.strftime(
                timezone.localtime(i), '%Y-%m-%d %H:%M:%S'), 'data': list(tran)})
    for tranExp in transExpDato:
        for i in Datos.objects.filter(amrContador__nombreContador=amr).filter(tmpLectura=dateFilter).values_list('tmpLectura', flat=True).order_by('totalImpEnerg'):
            transExpEnerg.append({'name': datetime.strftime(
                timezone.localtime(i), '%Y-%m-%d %H:%M:%S'), 'data': list(tranExp)})
    # fin filtro por los tres transformadores de energia activa (kwh)
    context = {
        'amr': amr,
        'details': details,
        'details1': details1,
        'transImpEnerg': transImpEnerg,
        'transExpEnerg': transExpEnerg,
    }

    return render(request, 'cocina_universidad/details.html', context)
