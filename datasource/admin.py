from django.contrib import admin

from .models import Banktrack, Bimpact, Bocc, Custombank, Fairfinance, Gabv, Marketforces, Switchit, Usnic, Wikidata


@admin.register(Banktrack, Bimpact, Bocc, Custombank, Fairfinance, Gabv, Marketforces, Switchit, Usnic, Wikidata)
class DatasourceAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ["name", "website"]
    search_fields = ["name", "website"]
