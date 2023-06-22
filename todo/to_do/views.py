from django.shortcuts import render,get_object_or_404
from . models import items
from django.db.models import Min
from .serializer import itemserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
        print(pk_list)

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

@api_view(['GET','POST','DELETE'])
def api(request):
    if request.method == "GET":
        item = items.objects.all()
        serializer = itemserializer(item,many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = itemserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
    elif request.method == "DELETE":
        item = items.objects.all()
        item.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
@api_view(['DELETE'])
def delete(request,id):
    pk_list = items.objects.values_list('pk', flat=True)
    n = pk_list[int(id)-1]
    item = get_object_or_404(items,pk = int(n))
    item.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)
