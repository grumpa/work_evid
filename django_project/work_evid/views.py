# coding: utf-8
"Views pro application work_evid."

from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from work_evid.models import Firm, Work, Todo
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import TodoForm, WorkForm


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


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
        'work_evid/overviews.html',
        {
            'works': works,
            'firms': firms,
            'sel_year': sel_year,
            'sel_month': sel_month,
            'sel_firm': sel_firm,
            'sel_order': sel_order,
            'months': list(range(1, 13)),
            'years': years,
            'works_total': works_total,
            'works_sub': works_sub,
        })


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


class WorkList(LoginRequiredMixin, ListView):
    model = Work

    def get_queryset(self):
        return super(WorkList, self).get_queryset().filter()[:25]


class WorkDetail(LoginRequiredMixin, DetailView):
    model = Work


class WorkCreate(LoginRequiredMixin, CreateView):
    model = Work
    form_class = WorkForm


class WorkUpdate(LoginRequiredMixin, UpdateView):
    model = Work
    form_class = WorkForm


class WorkDelete(LoginRequiredMixin, DeleteView):
    model = Work
    success_url = reverse_lazy('work_evid:work_list')


class FirmList(LoginRequiredMixin, ListView):
    model = Firm


class FirmCreate(LoginRequiredMixin, CreateView):
    model = Firm
    fields = ['name', 'periode', 'from_date', 'description', 'show_in_list']


class FirmDetail(LoginRequiredMixin, DetailView):
    model = Firm


class FirmUpdate(LoginRequiredMixin, UpdateView):
    model = Firm
    fields = ['name', 'periode', 'from_date', 'description', 'show_in_list']


class FirmDelete(LoginRequiredMixin, DeleteView):
    model = Firm
    success_url = reverse_lazy('work_evid:firm_list')


class TodoList(LoginRequiredMixin, ListView):
    model = Todo

    def get_queryset(self):
        """
        If url without firm_id return all Todos, else filter required firm.
        """
        if "firm" in self.kwargs:
            return Todo.objects.filter(firm_id=int(self.kwargs['firm']))
        else:
            return super(TodoList, self).get_queryset()

    def get_context_data(self):
        context = super(TodoList, self).get_context_data()
        context['firms'] = Firm.objects.all()
        if "firm" in self.kwargs:
            context['firm_selected'] = int(self.kwargs['firm'])
        else:
            context['firm_selected'] = 'ALL'
        return context


class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    required_css_class = 'required'


class TodoDetail(LoginRequiredMixin, DetailView):
    model = Todo


class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    required_css_class = 'required'


class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('work_evid:todo_list')
