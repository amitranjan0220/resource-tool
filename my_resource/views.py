from django.shortcuts import render
from django.http import HttpResponse
from . forms import MyResourceForm, CategoryForm
from . models import Category, MyResource
from django.contrib import messages
import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def resource_home(request):
    return render(request,'resource/resource_home.html')

@login_required
def add_resource(request):
    if request.method == 'POST':
        form = MyResourceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resource Added successfully')
    else:
        form = MyResourceForm()
    return render(request,'resource/add_resource.html',{'form':form})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Added successfully')
    else:
        form = CategoryForm()
    return render(request,'resource/add_category.html',{'form':form})

@login_required
def view_resource(request):
    all_resource = Category.objects.all()
    context = {'resource_list':all_resource}
    return render(request,'resource/view_resource.html',context)


@login_required
def all_resource(request, item_id):
    item = Category.objects.get(pk=item_id)
    cat = item.name
    all_item = MyResource.objects.filter(rsc_category=item)
    context = {'item_list': all_item,
                'cat': cat
               }
    return render(request,'resource/all_resource.html',context)


@login_required
def all_item(request):
    items = MyResource.objects.all().order_by('rsc_category')
    context = {"items":items}
    return render(request,'resource/all_item.html',context)

@login_required
def edit_item(request,item_id):
    item = MyResource.objects.get(pk=item_id)
    if request.method == 'POST':
        form = MyResourceForm(instance=item, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully')
    else:
        form = MyResourceForm(instance=item)
    return render(request,'resource/edit_resource.html',{'form':form})


@login_required
def delete_resource(request,item_id):
    item = MyResource.objects.get(pk=item_id)
    item.delete()
    items = MyResource.objects.all().order_by('rsc_category')
    context = {"items":items}
    return render(request,'resource/all_item.html',context)


@login_required
def download_csv(request):
    items = MyResource.objects.all().order_by('rsc_category')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="all_resource_list.csv"'

    writer = csv.writer(response)
    writer.writerow(['Category','Name/Serial No.','Comment','IP'])
    for item in items:
        category = item.rsc_category
        name = item.rsc_name
        comment = item.rsc_comment
        ip = item.rsc_ip
        writer.writerow([category, name, comment, ip])
    return response

    