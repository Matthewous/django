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


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
def home_view(request):
    msg = 'введите блюдо'
    return HttpResponse (msg)


def ingr_calc(request):
    plate = request.GET('plate')
    context = {}
    plate_list = {}
    
    for p, i in DATA.items():
        if p == plate:
            for ingr, num in i.items():
                plate_list[ingr] = num
            context[p] = plate_list

    # return render(request, 'calculator/index.html', context)
    HttpResponse(context)