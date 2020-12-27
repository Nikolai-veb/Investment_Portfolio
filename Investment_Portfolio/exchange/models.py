from django.db import models
from django.urls import reverse


class Countries(models.Model):
    """Models Countries"""
    name = models.CharField("Название страны", max_length=250)
    slug = models.SlugField(max_length=300, db_index=True)

    def get_absolute_url(self):
        return reverse('country_detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class Sectors(models.Model):
    """Models Sectors"""
    name = models.CharField("Название сектора", max_length=250)
    slug = models.SlugField(max_length=300, db_index=True)

    def get_absolute_url(self):
        return reverse('sector_detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Сектор'
        verbose_name_plural = 'Сктора'

    def __str__(self):
        return self.name


class Stocks(models.Model):
    """Models stocks"""
    name = models.CharField("Название актива", max_length=250, db_index=True)
    country = models.ForeignKey(Countries, verbose_name='Страна', on_delete=models.CASCADE)
    sectors = models.ForeignKey(Sectors, verbose_name='Сектор', on_delete=models.CASCADE)
    current_price = models.DecimalField("Текущая цена", default=0, max_digits=19, decimal_places=10)
    opening_price = models.DecimalField("Цена открытия", default=0, max_digits=19, decimal_places=10)
    closing_price = models.DecimalField("Цена закрытия", default=0, max_digits=19, decimal_places=10)
    dividends = models.DecimalField("Дивиденты", default=0, max_digits=10, decimal_places=3)
    outstanding_shares = models.DecimalField("Акции в обращении", default=0, max_digits=19, decimal_places=10)
    the_next_report = models.DateField("Дата следующего отчета")
    purchase_price = models.DecimalField("Цена покупки", default=0, max_digits=19, decimal_places=10)
    selling_price = models.DecimalField("Цена продажи", default=0, max_digits=19, decimal_places=10)
    slug = models.SlugField(max_length=300, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('stock_detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Акцыя'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.name


class Bonds(models.Model):
    """Models Bonds"""
    name = models.CharField("Название актива", max_length=250, db_index=True)
    country = models.ForeignKey(Countries, verbose_name='Страна', on_delete=models.CASCADE)
    sectors = models.ForeignKey(Sectors, verbose_name='Сектор', on_delete=models.CASCADE)
    current_price = models.DecimalField("Текущая цена", default=0, max_digits=19, decimal_places=10)
    opening_price = models.DecimalField("Цена открытия", default=0, max_digits=19, decimal_places=10)
    closing_price = models.DecimalField("Цена закрытия", default=0, max_digits=19, decimal_places=10)
    coupon = models.DecimalField("Купон", default=0, max_digits=10, decimal_places=3)
    bonds_in_circulation = models.DecimalField("Облигаций в обращении", default=0, max_digits=19, decimal_places=10)
    date_maturity = models.DateField("Дата погашения")
    purchase_price = models.DecimalField("Цена покупки", default=0, max_digits=19, decimal_places=10)
    selling_price = models.DecimalField("Цена продажи", default=0, max_digits=19, decimal_places=10)
    slug = models.SlugField(max_length=300, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('bonds_detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Облигацыя'
        verbose_name_plural = 'Облигации'

    def __str__(self):
        return self.name


class ETF(models.Model):
    """Models Etf"""
    name = models.CharField("Название актива", max_length=250, db_index=True)
    country = models.ForeignKey(Countries, verbose_name='Страна', on_delete=models.CASCADE)
    sectors = models.ForeignKey(Sectors, verbose_name='Сектор', on_delete=models.CASCADE)
    current_price = models.DecimalField("Текущая цена", default=0, max_digits=19, decimal_places=10)
    opening_price = models.DecimalField("Цена открытия", default=0, max_digits=19, decimal_places=10)
    closing_price = models.DecimalField("Цена закрытия", default=0, max_digits=19, decimal_places=10)
    dividends = models.DecimalField("Дивиденты", default=0, max_digits=10, decimal_places=3)
    assets_in_circulation = models.DecimalField("Активов в обращении", default=0, max_digits=19, decimal_places=10)
    asset_class = models.CharField("Класс актива", max_length=300)
    purchase_price = models.DecimalField("Цена покупки", default=0, max_digits=19, decimal_places=10)
    selling_price = models.DecimalField("Цена продажи", default=0, max_digits=19, decimal_places=10)
    slug = models.SlugField(max_length=300, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('etf_detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'ETF'
        verbose_name_plural = 'ETF'

    def __str__(self):
        return self.name


class Products(models.Model):
    """Models Etf"""
    name = models.CharField("Название актива", max_length=250, db_index=True)
    current_price = models.DecimalField("Текущая цена", default=0, max_digits=19, decimal_places=10)
    opening_price = models.DecimalField("Цена открытия", default=0, max_digits=19, decimal_places=10)
    closing_price = models.DecimalField("Цена закрытия", default=0, max_digits=19, decimal_places=10)
    assets_in_circulation = models.DecimalField("Активов в обращении", default=0, max_digits=25, decimal_places=10)
    purchase_price = models.DecimalField("Цена покупки", default=0, max_digits=19, decimal_places=10)
    selling_price = models.DecimalField("Цена продажи", default=0, max_digits=19, decimal_places=10)
    slug = models.SlugField(max_length=300, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
