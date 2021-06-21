from django.shortcuts import render
from django.views import View

from second.models import *


class UnresolvedPaymentsView(View):

    template_name = 'index.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accruals = list(Accrual.objects.all())
        self.accordance = []

    def get(self, request):
        payments = Payment.objects.all()
        payments_without_month_accruals, unresolved_payments = [], []

        for payment in payments:
            early_date_accruals = self._get_early_date_accruals(payment)
            found = False
            for accrual in early_date_accruals:
                if accrual.month == payment.month:
                    self._add_to_accordance(accrual, payment)
                    found = True
                    break
            if not found:
                payments_without_month_accruals.append(payment)
        for payment in payments_without_month_accruals:
            early_date_accruals = self._get_early_date_accruals(payment)
            if early_date_accruals:
                self._add_to_accordance(early_date_accruals[0], payment)
            else:
                unresolved_payments.append(payment)

        context = {
            'accordance': self.accordance,
            'unresolved_payments': unresolved_payments,
        }
        return render(request, 'index.html', context)

    def _get_early_date_accruals(self, payment):
        return [accrual for accrual in self.accruals if accrual.date < payment.date]

    def _add_to_accordance(self, accrual, payment):
        self.accordance.append((accrual, payment))
        index = self.accruals.index(accrual)
        self.accruals.pop(index)







