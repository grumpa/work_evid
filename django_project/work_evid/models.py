# coding: utf-8

from django.utils.translation import ugettext as _
from django.db import models
from django.forms import ModelForm
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

    class Meta:
        ordering = ['-date']


class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = ['firm', 'date', 'item_price', 'items', 'what_brief', 'what_detailed']

