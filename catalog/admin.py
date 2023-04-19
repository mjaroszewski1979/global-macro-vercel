# Django imports
from django.contrib import admin

# App imports
from .models import Strategy, Market

class StrategyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class MarketAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Strategy, StrategyAdmin)
admin.site.register(Market, MarketAdmin)
