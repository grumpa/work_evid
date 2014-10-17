# coding: utf-8
"Views pro application work_evid."

from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from work_evid.models import Firm, Work, WorkForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


@login_required
def index(request):
    "Manages work records."
    form = WorkForm()  # default
    pk = None
    if request.method == 'POST':
        if 'action' in request.POST:
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
def overviews(request):
    "Data overview with filtering possibility."
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
        if 'sel_year' in request.session:
            sel_year = request.session['sel_year']
        else:
            sel_year = timezone.now().year
        if 'sel_month' in request.session:
            sel_month = request.session['sel_month']
        else:
            sel_month = timezone.now().month
        if 'sel_firm' in request.session:
            sel_firm = request.session['sel_firm']
        else:
            sel_firm = "all"
        if 'sel_order' in request.session:
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
    for year in Work.objects.dates('date', 'year', 'ASC'):
        years.append(year.year)
    return render(
        request,
        'work_evid/overviews.html', {
            'works': works,
            'firms': firms,
            'sel_year': sel_year,
            'sel_month': sel_month,
            'sel_firm': sel_firm,
            'sel_order': sel_order,
            'months': range(1, 13),
            'years': years,
            'works_total': works_total,
            'works_sub': works_sub,
            }
        )


def delete_work(request):
    """Delete work items seleceted in 'overview' view."""

    if request.method == 'POST':
        if 'confirmed' in request.POST:
            # if confirmed by user in delete_work.html, delete
            if request.POST['confirmed'] == '1':
                Work.objects.filter(pk__in=request.session['wks']).delete()
                #message - deleted nn items
            else:
                # message - not deleting
                pass
            request.session['wks'] = None
            return redirect('work_evid:overviews')
        else:
            if 'work_del' in request.POST:
                wks = request.POST.getlist('work_del')
                works = Work.objects.filter(pk__in=wks)
                request.session['wks'] = wks
                return render(request, 'work_evid/delete_work.html', {'works': works, 'wks': wks})
            else:
                # want to delete, but nothing selected
                # message - you selected nothing
                return redirect('work_evid:overviews')
    else:
        # impossible
        return redirect('work_evid:overviews')


class FirmList(LoginRequiredMixin, ListView):
    model = Firm


class FirmCreate(LoginRequiredMixin, CreateView):
    model = Firm


class FirmDetail(LoginRequiredMixin, DetailView):
    model = Firm


class FirmUpdate(LoginRequiredMixin, UpdateView):
    model = Firm


class FirmDelete(LoginRequiredMixin, DeleteView):
    model = Firm
    success_url = reverse_lazy('work_evid:firm_list')
