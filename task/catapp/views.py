from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Catmodel

# rest-framework
from rest_framework.decorators import api_view



# Create your views here.

# View data
@api_view(['GET'])
def index(request):
    data = Catmodel.objects.all()
    context = {
            "data":data
    }
    return render(request,'index.html',context)

# Add new cat 
@api_view(['POST'])
def add_cat(request):
    data=request.POST
    name = data['catname']
    breed = data['catbreed']
    desc = data['catdesc']
    image = request.FILES['catimage']
    cat = Catmodel.objects.create(cat_name=name,cat_breed=breed,cat_desc=desc,cat_image=image)
    if cat:
        cat.save()
        messages.success(request, 'New cat add successfully')
        return redirect('/')
    return render(request,'index.html')

# fetching data
@api_view(['GET'])
def edit_blog(request,cat_id):
    cat=Catmodel.objects.filter(cat_id=cat_id)
    context = {
        "data":cat
    }
    return render(request,'edit.html',context)

# Details view 
@api_view(['GET'])
def view(request,cat_id):
    cat=Catmodel.objects.filter(cat_id=cat_id)
    context = {
        "data":cat
    }
    return render(request,'view.html',context)

# Update information
@api_view(['POST'])
def update_cat(request,cat_id):
    cat = Catmodel.objects.get(cat_id=cat_id)
    cat_name = request.POST['catname']
    cat_breed = request.POST['catbreed']
    cat_desc = request.POST['catdesc']
    cat_image = request.FILES['catimage']
    if cat_name:
        cat.cat_name = cat_name
    if cat_breed:
        cat.cat_breed = cat_breed
    if cat_desc:
        cat.cat_desc = cat_desc
    if cat_image:
        cat.cat_image = cat_image
    cat.save()
    messages.success(request, 'Data updated successfully')
    return redirect('/')

# Delete cat
@api_view(['GET'])
def delete_cat(request,cat_id):
    try:
        data=Catmodel.objects.get(cat_id=cat_id).delete()
        messages.error(request, 'Data Deleted sucessfully')
        return redirect('/')
    except:
        messages.error(request, 'Error please try again')
        return redirect('/')


    

     