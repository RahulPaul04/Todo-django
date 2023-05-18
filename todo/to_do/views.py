from django.shortcuts import render,get_object_or_404
from . models import items
from django.db.models import Min

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        print(request.POST)
        if name:
            print("here")
            it = items(name=name)
            try:
                it.save()
            except Exception as e:
                print(f"Error saving item: {e}")

        pk_list = items.objects.values_list('pk', flat=True)

        nu = request.POST.get('action')
        if nu:
            n = pk_list[int(nu)-1]
            print(n)
            it = get_object_or_404(items,pk = int(n))
            it.delete()
            
        

        if "delete" in request.POST:
            items.objects.all().delete()
        count = items.objects.count()
        
        
    item = items.objects.all()
    return render(request,"index.html",{"items":item})