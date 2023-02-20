from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links) 

def categories(request): 
    return {
        'categories' : Category.objects.all()
    }

"""
def menu_links():
    return {'links': Category.objects.values()}
"""