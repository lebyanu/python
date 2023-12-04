from .models import category, product


def menu_links(request):
    links = category.objects.all()

    return dict(links=links)

