from django.shortcuts import render, redirect 
from django.http import HttpResponseRedirect
from base .models import *
from django.db.models import Q
from .forms import *
from django.urls import resolve
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
#  for ajax data an load more 
from django.http import JsonResponse


# Create your views here.


def Wezarat(request):
    shehta = Taps.objects.all()
    wezarat = Gehat.objects.filter(name__startswith="وزارة")
    links = User_links.objects.all()
    if request.GET.get('search'):  # write your form name here
        question_name = request.GET.get('search')
        questions = Taps.objects.filter(
            Q(gehat_id__id=question_name))
        try:
            return render(request, "links/wezarat.html", {'shehta': shehta, 'wezarat': wezarat, "questions": questions})
        except:
            return render(request, "links/wezarat.html")
    context = {'shehta': shehta, 'wezarat': wezarat, 'links': links}
    return render(request, 'links/wezarat.html', context)


def mohafazat(request):
    shehta = Taps.objects.all()
    mohafazat = Gehat.objects.filter(name__startswith="محافظة")
    user_geha = request.user.Profiles.organization_name_id
    links = User_links.objects.all().distinct('tap_id')
    if request.GET.get('search'):  # write your form name here
        question_name = request.GET.get('search')
        questions = Taps.objects.filter(
            Q(gehat_id__id=question_name))
        try:
            return render(request, "links/mohafazat.html", {'shehta': shehta, 'mohafazat': mohafazat, "questions": questions})
        except:
            return render(request, "links/mohafazat.html")
    one_gov = Taps.objects.filter(
            Q(gehat_id__id=user_geha))
    c = one_gov.count()        
    context = {'shehta': shehta, 'mohafazat': mohafazat, 'links': links,'gov':one_gov,'c':c}
    return render(request, 'links/mohafazat.html', context)


def he2at(request):
    shehta = Taps.objects.all()
    wezarat = Gehat.objects.filter(name__startswith="وزارة")
    mohafazat = Gehat.objects.filter(name__startswith="محافظ")
    he2at = Gehat.objects.exclude(name__startswith="وزارة").exclude(
        name__startswith="محافظ").exclude(name__startswith="المستخدم ال")
    links = User_links.objects.all()
    if request.GET.get('search'):  # write your form name here
        question_name = request.GET.get('search')
        questions = Taps.objects.filter(
            Q(gehat_id__id=question_name))
        try:
            return render(request, "links/he2at.html", {'shehta': shehta, 'wezarat': wezarat, 'mohafazat': mohafazat, "questions": questions, "he2at": he2at})
        except:
            return render(request, "links/he2at.html")

    context = {'shehta': shehta, 'wezarat': wezarat,
               'mohafazat': mohafazat, 'links': links, "he2at": he2at}
    return render(request, 'links/he2at.html', context)


def allDash(request):
    wezarat = Gehat.objects.filter(name__startswith="وزارة")
    mohafazat = Gehat.objects.filter(name__startswith="محافظ")
    he2at = Gehat.objects.exclude(name__startswith="وزارة").exclude(
        name__startswith="محافظ").exclude(name__startswith="المستخدم ال")
    shehta = Taps.objects.all().order_by('-tap_description')
    count = Taps.objects.all().count()
    if request.GET.get('search'):  # write your form name here
        question_name = request.GET.get('search')
        questions = Taps.objects.filter(Q(tap_name__icontains=question_name)) 
        try:
            return render(request, "links/allDash.html", {'shehta': shehta, "questions": questions, 'count': count,'wezarat': wezarat, 'mohafazat': mohafazat, 'he2at': he2at })
        except:
            return render(request, "links/allDash.html")
    if request.GET.get('wezara'):  # write your form name here
        wezara = request.GET.get('wezara')
        wezara_sel = Taps.objects.filter(Q(gehat_id__name__icontains=wezara))    
        try:
            return render(request, "links/allDash.html", {'shehta': shehta, 'count': count, 'wezara_sel': wezara_sel,'wezarat': wezarat, 'mohafazat': mohafazat, 'he2at': he2at})
        except:
            return render(request, "links/allDash.html")
    if request.GET.get('he2a'):  # write your form name here
        he2a = request.GET.get('he2a')
        he2a_sel = Taps.objects.filter(Q(gehat_id__name__icontains=he2a))    
        try:
            return render(request, "links/allDash.html", {'shehta': shehta, 'count': count, 'he2a_sel': he2a_sel,'wezarat': wezarat, 'mohafazat': mohafazat, 'he2at': he2at})
        except:
            return render(request, "links/allDash.html")
    if request.GET.get('mohafza'):  # write your form name here
        mohafza = request.GET.get('mohafza')
        mohafza_sel = Taps.objects.filter(Q(gehat_id__name__icontains=mohafza))    
        try:
            return render(request, "links/allDash.html", {'shehta': shehta, 'count': count, 'mohafza_sel': mohafza_sel,'wezarat': wezarat, 'mohafazat': mohafazat, 'he2at': he2at})
        except:
            return render(request, "links/allDash.html")

    context = {'shehta': shehta, 'count': count,
               'wezarat': wezarat, 'mohafazat': mohafazat, 'he2at': he2at}
    return render(request, 'links/allDash.html', context)





# load more with AJAX:
def loadMore(request):
    total_links = int(request.GET.get('total_item'))
    limit = 2
    link_obj = list(Taps.objects.values()[total_item:total_item+limit])
    data = {
        'links':link_obj
    }
    return JsonResponse(data = data )




# for show categories of taps
def showCategories(request):
    # get all categories 
    tap_category = taps_categories.objects.all()
    # get the count of taps 
    count = Taps.objects.all().count()
    context = {"cat":tap_category,"count":count}
    return render(request, 'links/category.html', context)



# for show sub of categories  of taps
def showCategories_sub(request, cat_id):
    # get all taps with filter by ID
    category_sub =  taps_categories_sub.objects.filter(tabs_category_id=cat_id)
    tap_category = taps_categories.objects.get(id=cat_id)
    # get the count of taps 
    # get the count of taps 
    count = Taps.objects.all().count()
    context = {"cat":category_sub,"count":count,"cat_name":tap_category}
    return render(request, 'links/subcatgories.html', context)




# for show taps related with categories_sub 
def categoryList(request, cat_id):
    # get all taps with filter by ID
    taps_list =  Taps.objects.filter(taps_categories_sub_id=cat_id)
    # get the count of taps 
    count = taps_list.count()


    context = {'shehta': taps_list, 'count': count}
    return render(request, 'links/categoryList.html', context)



# list all taps for admin panel
def listTaps(request):
    users = Taps.objects.all().order_by('-id')
    paginator = Paginator(users, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.GET.get('search'):  # write your form name here
        user_name = request.GET.get('search')
        try:
            page_obj = Taps.objects.filter(
                Q(gehat_id__name__icontains=user_name) | Q(tap_name__icontains=user_name))
            return render(request, "links/taps/index.html", {"page_obj1": page_obj})
        except:
            return render(request, "links/taps/index.html", {"page_obj": page_obj})
    context = {'page_obj': page_obj}
    return render(request, 'links/taps/index.html', context)


# add new tap from admin panel
def addTap(request):
    form = TapCreate()
    if request.method == 'POST':
        form = TapCreate(request.POST)
        if form.is_valid():
            s = request.POST.get('gehat_id')
            n = form.save()
            print(n.id)
            organization_name = Profiles.objects.filter(
                organization_name__id=s)
            for each in organization_name:
                user_links = User_links(user_id=each, tap_id=n)
                user_links.save()
            return redirect('listTaps')
    else:
        form = TapCreate()

    context = {'form': form}
    return render(request, 'links/taps/addTap.html', context)


# update an exiting tap from admin panel
def updateTap(request, tap_id):
    tap_id = int(tap_id)
    try:
        tap_sel = Taps.objects.get(id=tap_id)
    except Taps.DoesNotExist:
        return redirect('listTaps')
    taps_form = TapCreate(request.POST or None,
                          request.FILES or None, instance=tap_sel)
    if taps_form.is_valid():
        s = request.POST.get('gehat_id')
        n = taps_form.save()
        print(n.id)
        organization_name = Profiles.objects.filter(organization_name__id=s)
        for each in organization_name:
            print(each.id)
            user_links = User_links(user_id=each, tap_id=n)
            user_links.save()
        return redirect('listTaps')
    return render(request, 'links/taps/addTap.html', {'form': taps_form})


# delete tap from admin panel for admin
def deleteTap(request, tap_id):
    tap_id = int(tap_id)
    try:
        tap_sel = Taps.objects.get(id=tap_id)
    except Taps.DoesNotExist:
        return redirect('listTaps')
    tap_sel.delete()
    return redirect('listTaps')


def addUserLinks(request):
    profiles = Profiles.objects.filter(gehat_id)
    taps = Taps.objects.filter(gehat_id)
    form = UserLinksCreate()

    User_links.objects.create(
        'insert into public.user_links (profile_id, tap_id) select public.taps.id, public.profiles.id from  public.profiles ,public.tapswhere  public.taps.gehat_id = public.profiles.gehat_id;')
    if request.method == 'POST':
        form = UserLinksCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = UserLinksCreate()

    context = {'form': form}
    return render(request, 'links/user_links.html', context)


# news

def index(request):
    news = News.objects.all().order_by('-news_view')
    news_last = News.objects.all().order_by('-date')
    paginator = Paginator(news_last, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    #
    #

    context = {'news': news, 'page_obj': page_obj}
    return render(request, 'news/index.html', context)


#  details for news
def details(request, news_id):
    news_id = int(news_id)
    news = News.objects.all().order_by('-news_view')
    try:
        news_sel = News.objects.get(id=news_id)
        news_sel.news_view = news_sel.news_view+1
        news_sel.save()
    except News.DoesNotExist:
        return redirect('news-index')
        #

    #
    return render(request, 'news/details.html', {'news_sel': news_sel, 'news': news})


# list all news for admin
def newscontrol(request):
    news_last = News.objects.all().order_by('-date__time')
    paginator = Paginator(news_last, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news/newscontrol.html', {'page_obj': page_obj})


# update news for admin
def updateNews(request, news_id):
    news_id = int(news_id)
    try:
        news_sel = News.objects.get(id=news_id)
    except News.DoesNotExist:
        return redirect('newscontrol')
    news_form = createNews(request.POST or None, instance=news_sel)
    if news_form.is_valid():
        news_form.save()
        return redirect('newscontrol')
    return render(request, 'news/createNews.html', {'form': news_form, 'news_sel': news_sel})


# delete news form admin
def delete_news(request, news_id):
    news_id = int(news_id)
    try:
        news_sel = News.objects.get(id=news_id)
    except News.DoesNotExist:
        return redirect('newscontrol')
    if request.method == 'POST':
        news_sel.delete()
        return redirect('newscontrol')
    return render(request, 'news/delete.html', {'user_sel': news_sel})


# create new news
def createNewss(request):
    if request.method == 'POST':
        upload = createNews(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('news-index')
    else:
        upload = createNews()
    return render(request, 'news/createnews.html', {'form': upload})
