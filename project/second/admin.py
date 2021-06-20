from django.contrib import admin

from second.models import *


@admin.register(Accrual)
class AccrualAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
