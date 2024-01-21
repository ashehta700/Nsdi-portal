from django.shortcuts import render , HttpResponse
from django.contrib.auth import authenticate, login 
from django.contrib import auth 
from django.shortcuts import redirect
from .models import *
from links .models import *
from .forms import ExtendedUserCreationForm , UserProfileForm
from links .forms import *
from django.contrib import messages # import message from django
from django.core.paginator import Paginator
from django.db.models import Q 
from BruteBuster.models import FailedAttempt ,BB_BLOCK_INTERVAL
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.decorators import login_required




# home page
def view(request):
    news = News.objects.all().order_by('-date')

    context = {'news':news}
    return render(request,'home.html',context)

@login_required
# apps page
def apps(request):
    user_geha_id = request.user.Profiles.organization_name

    search = Apps.objects.all().distinct('name')

    apps_cat = Apps.objects.filter(organization_name=user_geha_id)

    name = None

    if 'search_name' in request.GET:
        name = request.GET['search_name']

        if name:
            search = search.filter(Q(name__icontains=name) | Q(description__icontains=name))

    context = {'apps': search, 'apps_cat': apps_cat, 'search_term': name}

    if not search.exists():
        context['no_results'] = True

    return render(request, 'apps.html', context)

# Cat_apps page
def cat_apps(request):
    user_geha_id = request.user.Profiles.organization_name
    cat_App = Apps_category.objects.all().distinct('catoName')
    apps_cat = Apps.objects.filter(organization_name=user_geha_id)
    context= {'cat_apps':cat_App,'apps_cat':apps_cat}
    return render(request,'Cat_Apps.html',context)


def cat_apps_sub(request, id):
    category = Apps_category.objects.get(id=id)
    # get all categories with filter by ID
    category_sub = Apps_category_Sub.objects.filter(Apps_category=id)
    

    context = {"cat": category_sub , "category" : category}

    return render(request, 'subcatgoriesApps.html', context)



def cat_sub(request , id):

    category = Apps_category_Sub.objects.get(id=id)
    # get all categories with filter by ID
    category_sub = Apps.objects.filter(Apps_category_Sub=id)
    

    context = {"cat": category_sub , "category" : category}

    return render(request,'Cat_Sub.html',context)



    








# index for control apps
@login_required
def appsIndex(request):
    apps = Apps.objects.all().order_by('-date')
    paginator = Paginator(apps, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request,'apps/index.html',context)


# add new App in apps page
@login_required
def appsCreate(request):
    if request.method == 'POST':
        upload = createApp(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('apps-index')
    else:
        upload = createApp()
    return render(request, 'apps/create.html', {'form':upload})     


# update app from admin 
@login_required
def updateApp(request , app_id):
    app_id = int(app_id)
    try:
        app_sel = Apps.objects.get(id = app_id)
    except Apps.DoesNotExist:
        return redirect('apps-index')
    apps_form = createApp(request.POST or None, instance = app_sel)
    if apps_form.is_valid():
        apps_form.save()
        return redirect('apps-index')
    return render(request, 'apps/create.html', {'form':apps_form})     

# delete app from admin 
@login_required
def deleteApp(request,app_id):
    app_id = int(app_id)
    try:
        apps_sel = Apps.objects.get(id = app_id)
    except Apps.DoesNotExist:
        return redirect('apps-index') 
    if request.method == 'POST': 
        apps_sel.delete()
        return redirect('apps-index')    
    return render(request, 'apps/delete.html',{'user_sel':apps_sel})   

# check the user and password 

def login(request):
    
    if request.method == "POST":
        check_if_user_exists = User.objects.filter(username=request.POST['username']).exists()
        if check_if_user_exists:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            
                       
            if user is not None:
                auth.login(request, user)
                return redirect('base')
            else:
                # this user is not valid, he provided wrong password, show some error message
                ip=request.META.get('REMOTE_ADDR')
                failed = FailedAttempt.objects.get(username__icontains = request.POST['username'],IP__icontains = ip)
                if  failed.too_many_failures() == True:
                    return render(request,'login.html',{'error':"لقد تخطيت عدد المحاولات الخاطئة برجاء المحاولة مره اخرى بعد" +str(datetime.now().minute - (failed.timestamp.minute - BB_BLOCK_INTERVAL)  )+ "  دقائق"} )
                else :     
                    return render(request,'login.html',{'error':"أسم المستخدم صحيح ولكن خطأ بكلمة المرور </br> لديك عدد "+ str(3-failed.failures)+" محاولات "} )
                
        else:
            # there is no such entry with this username in the table
            return render(request,'login.html',{'error':"لا يوجد أسم مستخدم بهذا الأسم"} )
    else:    
        return render(request,'login.html')



# register new user and Profiles for this user
@login_required
def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form =UserProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            username = form.cleaned_data.get('username')    
            password = form.cleaned_data.get('password1')  
            profile.tenant_link = request.POST.get('tenant_link')
            profile.app_link = request.POST.get('app_link')
            n = profile.save()
            s = request.POST.get('organization_name')
            taps = Taps.objects.filter(gehat_id__id__icontains = s)
            for each in taps:
                print(each.id)
                user_links = User_links(user_id=profile,tap_id=each)
                user_links.save()            
            user = authenticate(username=username,password=password)
            return redirect('login')  
    else:
        form = ExtendedUserCreationForm() 
        profile_form = UserProfileForm()  

    context = {'form':form , 'profile_form':profile_form}  
    return render(request , 'users/createuser.html',context)    



# update user 
@login_required
def updateProfiles(request,profiles_id):
    profiles_id = int(profiles_id)
    try:
        user_sel = Profiles.objects.get(id = profiles_id)
    except Profiles.DoesNotExist:
        return redirect('users/user_profile.html')
    user_form = UserProfileForm(request.POST or None, request.FILES or None, instance = user_sel)
    if user_form.is_valid():
        user_form.save()
        messages.success(request , f'تم تعديل بياناتك بنجاح !')

        return render(request, 'users/user_profile.html', {'profile_form':user_form})
    return render(request, 'users/user_profile.html', {'profile_form':user_form})      




# list users for admin panel pagge
@login_required
def ListUsers(request):
    users = Profiles.objects.all()
    paginator = Paginator(users, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.GET.get('search'): # write your form name here      
        user_name =  request.GET.get('search')      
        try:
            page_obj = Profiles.objects.filter(Q(organization_name__name__icontains=user_name)|Q(name__icontains=user_name)|Q(user__username__icontains=user_name))
            return render(request,"users/index.html",{"page_obj":page_obj})
        except:
            return render(request,"users/index.html",{"page_obj":page_obj})
    context= {'page_obj':page_obj}
    return render(request,'users/index.html',context)


# update user from admin panel 
@login_required
def UpdateUser(request,user_id):
    user_id = int(user_id)
    try:
        user_sel = Profiles.objects.get(id = user_id)
    except Profiles.DoesNotExist:
        return redirect('ListUsers')
    users_form = UserProfileForm(request.POST or None, request.FILES or None, instance = user_sel)
    if users_form.is_valid():
        users_form.save()
        return redirect('ListUsers')
    return render(request, 'users/updateuser.html', {'profile_form':users_form})

@login_required
def deleteUser(request,user_id):
    user_id = int(user_id)
    try:
        user_sel = Profiles.objects.get(id = user_id)
    except Profiles.DoesNotExist:
        return redirect('ListUsers')
    if request.method == 'POST': 
        u = User.objects.get(username = user_sel.user.username)
        user_sel.delete()
        u.delete()
        return redirect('ListUsers')    
    return render(request, 'users/delete.html',{'user_sel':user_sel})           
          

