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

a = {'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    }
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
def home_view(request):
    msg = 'hello'
    return HttpResponse (msg)

def hello(request, name):
    # name = request.GET('name')
    # msg = f'введите блюдо, {name}'
    context = {}
    
    for p, i in DATA.items():
        if p == name:
            for ingr, num in i.items():
                context[ingr] = num

    return render(request, 'calculator/index.html', context)

def ingr_calc(request, plate):

    # context = {}
    # plate_list = {}
    
    # for p, i in DATA.items():
    #     if p == plate:
    #         for ingr, num in i.items():
    #             plate_list[ingr] = num
    #         context[p] = plate_list
    # if context == a:
    #     msg = 'y'
    # else:
    #     print(context)
    #     print('___')
    #     print(a)
    #     msg = 'n'
    msg = f'{plate}'
    # return render(request, 'calculator/index.html', context)
    HttpResponse(msg)
