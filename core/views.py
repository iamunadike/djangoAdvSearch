from django.shortcuts import render
from  django.views.decorators.http import require_http_methods
from .models import Category, Journal
from django.utils import six
from django.db.models import Q

# Create your views here.
@require_http_methods(['GET'])
def SimpleForm(request):
    qs = Journal.objects.all()
    categories = Category.objects.all()
    if not 'reviewed' in request.GET:
        qs = qs.filter(reviewed=False)
    else:
        factor = request.GET.get("reviewed") == "on"
        qs = qs.filter(reviewed=factor)
    queries_ = dict(six.iteritems((request.GET)))
    queries = ((k,v) for k,v in dict.items(queries_) if len(v) != 0 and v != None and k is not "reviewed")
    
    while 1:
        try:
            x = queries.__next__()
            if x[0].__contains__("title") and not  x[0].__contains__("author"):
                qs = qs.filter(title__icontains=x[1])
            if x[0].__contains__("title") and x[0].__contains__("author"):
                qs = qs.filter(Q(title__icontains=x[1]) | Q(author__name__icontains=x[1])).distinct()
            if x[0].__contains__('date'):
                y = queries.__next__()
                qs = qs.filter(Q(published__gte=x[1]) & Q(published__lt=y[1]))
            if x[0].startswith('view'):
                z = queries.__next__()
                qs = qs.filter(Q(views__gte=x[1]) & Q(views__lt=z[1]))
            if x[0] == 'category' and x[1] != "Choose...":
                qs = qs.filter(categories__name=x[1])  
        except StopIteration:
            break
    
    return render(request, "form.html", {"qs": qs, "categories": categories, "checker": request.GET.get("reviewed")})