# coding: utf-8
"Views pro application work_evid."

from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from work_evid.models import Firm, Work, FirmForm, WorkForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    form = WorkForm() # default
    pk = None
    if request.method == 'POST':
        if request.POST.has_key('action'):
            pk = request.POST['pk']
            work = Work.objects.get(pk=pk)
            if request.POST['action'] == 'edit':
                form = WorkForm(instance=work)
            if request.POST['action'] == 'delete':
                Work.objects.get(pk=pk).delete()
        else:
            pk = request.POST['pk']
            if pk != "None":
                # update
                work = Work.objects.get(pk=pk)
                form = WorkForm(request.POST, instance=work)
            else:
                # new record
                form = WorkForm(request.POST)
            if form.is_valid():
                form.save()
                form = WorkForm()
                pk = None
    works = Work.objects.all()[:16]
    return render(request,
                  'work_evid/index.html',
                  {'form': form,
                   'works': works,
                   'pk': pk,
                   'firms_exist': Firm.objects.exists(),
                   })


@login_required
def firm_edit(request):
    form = FirmForm() # default - empty form
    fpk = None
    if request.method == 'POST':
        if request.POST.has_key('firm_act'):
            fpk = request.POST['firm_pk']
            firm = Firm.objects.get(pk=fpk)
            if request.POST['firm_act'] == 'edit':
                form = FirmForm(instance=firm)
            elif request.POST['firm_act'] == 'delete':
                works = firm.work_set.count()
                if works == 0:
                    Firm.objects.get(pk=fpk).delete()
                else:
                    form = FirmForm()
                    form.errors['__all__'] = form.error_class([_('Cannot delete - works exist (%s).') % (works,)])
                    form.errors['__all__'] += form.error_class([_('Second problem')])
        else:
            pk = request.POST['pk']
            if pk != "None":
                # update
                firm = Firm.objects.get(pk=pk)
                form = FirmForm(request.POST, instance=firm)
            else:
                # new record
                form = FirmForm(request.POST)
            if form.is_valid():
                form.save()
                form = FirmForm()
    firms = Firm.objects.all()
    return render(request,
                  'work_evid/firm_edit.html',
                  { 'form': form, 'fpk':fpk, 'firms': firms })


@login_required
def overviews(request):
    cur_year = timezone.now().year
    if request.method == 'POST':
        sel_year = request.POST['year']
        request.session['sel_year'] = sel_year
        sel_month = request.POST['month']
        request.session['sel_month'] = sel_month
        sel_firm = request.POST['firm']
        request.session['sel_firm'] = sel_firm
        sel_order = request.POST['order']
        request.session['sel_order'] = sel_order
    else:
        if request.session.has_key('sel_year'):
            sel_year = request.session['sel_year']
        else:
            sel_year = timezone.now().year
        if request.session.has_key('sel_month'):
            sel_month = request.session['sel_month']
        else:
            sel_month = timezone.now().month
        if request.session.has_key('sel_firm'):
            sel_firm = request.session['sel_firm']
        else:
            sel_firm = "all"
        if request.session.has_key('sel_order'):
            sel_order = request.session['sel_order']
        else:
            sel_order = "date"
    firms = Firm.objects.all()
    works = Work.objects.order_by(sel_order, 'date')
    if sel_year != 'all':
        sel_year = int(sel_year)
        works = works.filter(date__year=sel_year)
        #firms = firms.filter(work__date__year=sel_year).distinct()
    if sel_month != 'all':
        sel_month = int(sel_month)
        works = works.filter(date__month=sel_month)
        #firms = firms.filter(work__date__month=sel_month).distinct()
    if sel_firm != 'all':
        sel_firm = int(sel_firm)
        firm = Firm.objects.get(pk=sel_firm)
        works = works.filter(firm=firm)
    works_sub = dict()
    for work in works:
        if work.firm.name not in works_sub:
            works_sub[work.firm.name] = 0
        works_sub[work.firm.name] += work.items * work.item_price
    works_total = 0
    for fn in works_sub:
        works_total += works_sub[fn]
    years = list()
    for year in Work.objects.dates('date','year','ASC'):
        years.append(year.year)
    return render(request,
                  'work_evid/overviews.html', {
                    'works': works,
                    'firms': firms,
                    'sel_year': sel_year,
                    'sel_month': sel_month,
                    'sel_firm': sel_firm,
                    'sel_order': sel_order,
                    'months': range(1,13),
                    'years': years,
                    'works_total': works_total,
                    'works_sub': works_sub,
                    })

