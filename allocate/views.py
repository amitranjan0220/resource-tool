from django.shortcuts import render
from my_resource.models import Category, MyResource
from django.contrib.auth.models import User
from .models import AllocateResource
from django.contrib import messages
from .forms import  UserSearchForm, ResourceSearchForm 
from django.contrib.auth.decorators import login_required 

@login_required
def allocate_home(request):
    return render(request, 'allocate/allocate_home.html')

@login_required
def allocate_view(request):
    return render(request, 'allocate/allocate_view.html')


@login_required
def allocate_resource(request):
    cat = Category.objects.all()
    return render(request, 'allocate/allocate_resource_home.html',{'cat':cat})


@login_required
def select_resource(request,pk):
    users = User.objects.all()
    cat = Category.objects.get(pk=pk)
    ress = MyResource.objects.filter(rsc_category=cat)
    none_user = User.objects.get(username='None')
    context = {
        'ress' : ress,
        'users': users,
        'none_user': none_user    
        }
    if request.method == "POST":
        cat = Category.objects.get(pk=pk)
        ress = MyResource.objects.filter(rsc_category=cat)
        try:
            for res in ress:
                user_id = request.POST.get(res.rsc_name)
                comment = request.POST.get('comment_'+ res.rsc_name)
                user = User.objects.get(pk=user_id)
                if (res.rsc_status == 'Unassigned') and (none_user.id != int(user_id)):
                    AllocateResource.objects.create(user=user,resource=res,comment=comment)
                    res.rsc_status = 'Assigned'
                    res.save()
                    messages.success(request, ("Resource assigned Successfully {}").format(res)) 
                else:
                    pass         
        except:
            messages.success(request, 'Please fill form correctly')
            
    return render(request, 'allocate/allocate_resource.html',context)

@login_required
def search_by_user(request):
    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            print(user.id)
            all_list = AllocateResource.objects.filter(user=user)
            context = {'list':all_list}
            return render(request, 'allocate/final_allocate.html',context)

    else:
        form = UserSearchForm()
    return render(request, 'allocate/search_by_user.html',{'form':form})


@login_required
def search_by_resource(request):
    if request.method == 'POST':
        form = ResourceSearchForm(request.POST)
        if form.is_valid():
            cat = form.cleaned_data['category']
            res = form.cleaned_data['resource']
            all_list = AllocateResource.objects.filter(resource=res)
            context = {'list':all_list}
            return render(request, 'allocate/final_allocate.html',context)

    else:
        form = ResourceSearchForm()
    return render(request, 'allocate/search_by_resource.html',{'form':form})


@login_required
def load_resources(request):
    category = request.GET.get('category')
    cat = Category.objects.get(pk=category)
    resources = MyResource.objects.filter(rsc_category=cat)
    return render(request, 'allocate/resource_dropdown.html',{'resources':resources})