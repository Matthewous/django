from pprint import pprint

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
    }
}

plate = 'pasta'

def ingr_calc(plate):

    context = {}
    plate_list = {}
    
    for p, i in DATA.items():
        if p == plate:
            for ingr, num in i.items():
                plate_list[ingr] = num
            context[p] = plate_list
    pprint(context)
    return context

            
if __name__ == '__main__':
    ingr_calc('omlet')

