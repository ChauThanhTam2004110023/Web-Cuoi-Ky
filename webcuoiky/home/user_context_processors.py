from .models import *


def loadBaseItems(request):
    categories = Category.objects.all()


    return {
        'categories': categories,
    }
