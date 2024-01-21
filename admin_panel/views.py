from django.shortcuts import render
from base .models import *
from links .models import *
from technical .models import *
from tools .models import *
from django.db.models import Sum
from datetime import timedelta
from django.contrib.auth.decorators import login_required

# Create your views here.




@login_required
def index(request):
    users = Profiles.objects.all().count()
    news = News.objects.all().count()
    news_views_mon = News.objects.filter(date__iso_week_day=1).aggregate(news_view=Sum('news_view'))
    news_views_tue = News.objects.filter(date__iso_week_day=2).aggregate(news_view=Sum('news_view'))
    news_views_wen = News.objects.filter(date__iso_week_day=3).aggregate(news_view=Sum('news_view'))
    news_views_thr = News.objects.filter(date__iso_week_day=4).aggregate(news_view=Sum('news_view'))
    news_views_fri = News.objects.filter(date__iso_week_day=5).aggregate(news_view=Sum('news_view'))
    news_views_sat = News.objects.filter(date__iso_week_day=6).aggregate(news_view=Sum('news_view'))
    news_views_sun = News.objects.filter(date__iso_week_day=7).aggregate(news_view=Sum('news_view'))
    apps = Apps.objects.all().count()
    taps = Taps.objects.all().count()
    faq = Problems.objects.all().count()
    comunity_question = Question.objects.all().count()
    comunity_comment = Answer.objects.all().count()
    messages = ContactUs.objects.all().count()
    merge = MergeRequest.objects.all().count()
    deplyment_app = DeploymentRequest_apps.objects.all().count()
    deplyment_layer = DeploymentRequest_layers.objects.all().count()
    inquiryrequest = InquiryRequest.objects.all().count()
    context={'users':users,'news':news,'apps':apps,'taps':taps,'faq':faq,
    'comunity_question':comunity_question,'comunity_comment':comunity_comment,
    'messages':messages,'merge':merge,'deplyment_app':deplyment_app,
    'deplyment_layer':deplyment_layer,'inquiryrequest':inquiryrequest,
    'news_views_mon':news_views_mon,
    'news_views_tue':news_views_tue,
    'news_views_wen':news_views_wen,
    'news_views_thr':news_views_thr,
    'news_views_fri':news_views_fri,
    'news_views_sat':news_views_sat,
    'news_views_sun':news_views_sun,
    }
    return render(request, 'admin-panel/index.html',context)