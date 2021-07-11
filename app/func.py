from decimal import Decimal
from django.conf import settings
from .models import Reklam


class Functions(object):

    def __int__(self, request):
        pass

    def __iter__(self):
        pass

    def add_reklam(self):
        pass

    def save_reklam(self):
        pass

    def clear_reklam(self):
        pass

    def delete_reklam(self):
        pass

    def filtr_price_lg(self):
        return Reklam.objects.filter('-price')

    def filtr_price_ng(self):
        return Reklam.objects.filter('price')

    def filtr_with_price(self, input, output):
        a = input
        b = output
        j = Reklam.objects.filter(price__gte=a, price__lt=20)
        pass

    def with_new(self):
        return Reklam.objects.filter('-date')

    def with_old(self):
        return Reklam.objects.filter('date')


