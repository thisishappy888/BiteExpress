from django.shortcuts import render
from main.models import Categories
from main.models import Category
from main.models import Burgers

# Create your views here.
def index(request):

    all_categories = Categories.objects.all()

    all_category = Category.objects.all()

    all_burgers = Burgers.objects.all()

    


    return render(request, 'main/index.html', context={'categories': all_categories,
                                                       'category': all_category,
                                                       'burgers': all_burgers,
                                                       })