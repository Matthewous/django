from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    msg = 'hello'
    return HttpResponse (msg)

def recipes(request, plate):

    servings = int(request.GET.get('servings', 1))
    ingr_list = {}    
    for p, i in DATA.items():
        if p == plate:
            for ingr, num in i.items():
                ingr_list[ingr] = num * servings

    return render(request, 'calculator/index.html', context={'recipe':ingr_list})

