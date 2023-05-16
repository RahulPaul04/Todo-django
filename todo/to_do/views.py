from django.shortcuts import render
from . models import items

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            it = items(name=name)
            try:
                it.save()
            except Exception as e:
                print(f"Error saving item: {e}")
    item = items.objects.all()
    return render(request,"index.html",{"items":item})