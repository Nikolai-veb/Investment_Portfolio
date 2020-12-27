from django.contrib import admin
from .models import Countries, Sectors, Stocks, Products, Bonds, ETF


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Sectors)
class SectorsAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "sectors", "current_price", "dividends")
    list_filter = ("name", "country", "sectors",)
    search_fields = ("name", "country", "sectors",)
    prepopulated_fields = {"slug": ("name", "country", "sectors")}


@admin.register(Bonds)
class BondsAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "sectors", "current_price", "coupon")
    list_filter = ("name", "country", "sectors",)
    search_fields = ("name", "country", "sectors",)
    prepopulated_fields = {"slug": ("name", "country", "date_maturity")}


@admin.register(ETF)
class ETFAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "sectors", "current_price", "dividends")
    list_filter = ("name", "country", "sectors",)
    search_fields = ("name", "country", "sectors",)
    prepopulated_fields = {"slug": ("name", "country", "assets_in_circulation")}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "current_price")
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
