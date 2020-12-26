from django.db import models
from django.urls import reverse


class Stocks(models.Model):
    """Models stocks"""
    name = models.CharField("Название актива", max_length=250, db_index=True)
    current_price = models.DecimalField("Текущая цена", default=0)
    opening_price = models.DecimalField("Цена открытия", default=0)
    closing_price = models.DecimalField("Цена закрытия", default=0)
    dividends = models.DecimalField("Дивиденты", default=0)
    outstanding_shares = models.DecimalField("Акции в обращении", default=0)
    the_next_report = models.DateField("Дата следующего отчета")
    purchase_price = models.DecimalField("Цена покупки", default=0)
    selling_price = models.DecimalField("Цена продажи", default=0)
    slug = models.SlugField(max_length=300)

    def get_absolute_url(self):
        return reverse('stock_detail', kwargs={"slug": self.slug,})

    class Meta:
        verbose_name = 'Акцыя'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.name
