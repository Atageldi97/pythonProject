from .models import Category, FirmReklam


def reklam(request):
    return {
        'categories': Category.objects.all(),
        'firms': FirmReklam.objects.all()
    }
