# coding: utf-8

from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone


class Firm(models.Model):
    "Simple firm database."
    name = models.CharField(max_length=60, verbose_name=_('firm name'))
    periode = models.IntegerField(default=1,
                                  verbose_name=_('periode [months]'),
                                  help_text=_('How often we make an invoice.'))
    from_date = models.DateField(default=timezone.now, verbose_name=_('from date'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    show_in_list = models.BooleanField(default=True, verbose_name=_('show in list'))

    def get_absolute_url(self):
        return reverse('work_evid:firm_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name']
        verbose_name = _('firm')

    def __unicode__(self):
        return self.name


class Work(models.Model):
    "Work evidence model."
    firm = models.ForeignKey(Firm, verbose_name=_('firm'))
    date = models.DateField(default=timezone.now, verbose_name=_('work date'))
    item_price = models.DecimalField(max_digits=15,
                                     decimal_places=2,
                                     verbose_name=_('price for item'))
    items = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                default=1,
                                verbose_name=_('ammount of items'))
    what_brief = models.CharField(max_length=80, verbose_name=_('what (briefly)'))
    what_detailed = models.TextField(blank=True, verbose_name=_('describe detailed'))

    @property
    def full_price(self):
        "Returns item price multiplied by ammount."
        return self.items * self.item_price

    #full_price = property(_get_full_price)

    def get_absolute_url(self):
        return reverse('work_evid:work_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-date']


class Todo(models.Model):
    firm = models.ForeignKey(Firm, verbose_name=_('firm'))
    date = models.DateField(default=timezone.now, verbose_name=_('created'))
    todo = models.TextField(blank=True, verbose_name=_('todo'))
    finished = models.BooleanField(default=False, verbose_name=_('finished'))

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.date, self.firm[:12], self.todo[:40])

    def get_absolute_url(self):
        return reverse('work_evid:todo_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['finished', '-date']
