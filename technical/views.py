from django.shortcuts import render, redirect ,HttpResponse
from .models import *
from .forms import  *
from django.core.paginator import Paginator
from django.db.models import Q 
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
# show Message thats is comming from ContactUs
def showMessage(request):
    messages = ContactUs.objects.all()
    paginator = Paginator(messages, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'technical/messages/index.html',{'page_obj':page_obj})

@login_required
# details for message comming from ContactUs
def messageDetails(request,message_id):
    message_id = int(message_id)
    messages = ContactUs.objects.all()
    try:
        message_sel = ContactUs.objects.get(id = message_id)
    except ContactUs.DoesNotExist:
        return redirect('show-message')   
    return render(request, 'technical/messages/details.html', {'message_sel':message_sel})        




@login_required
def view(request):
    if request.method == 'POST':
        upload = ContactUsCreate(request.POST)
        if upload.is_valid():
            portfolio  = upload.save(commit=False)
            portfolio.profile_id = request.user.Profiles
            portfolio.phone = request.user.Profiles.phone
            portfolio.address = request.user.Profiles.organization_address
            portfolio.email = request.POST['email']
            portfolio.message = request.POST['message']
            portfolio.save()
            return redirect('technical')
    else:
        upload = ContactUsCreate()    
    return render(request,'technical/technical.html',{'upload':upload})


def manual(request):
    return render(request,'technical/manualGuide.html')





# answer the question in community
# show all questions and comments
@login_required
def community(request):
    questions = Question.objects.all().order_by('-date')
    answers = Answer.objects.all().order_by('-date')
    if request.GET.get('search'): # write your form name here      
        question_name =  request.GET.get('search')      
        try:
            questions = Question.objects.filter(Q(name__icontains=question_name))
            answers = Answer.objects.filter(Q(name__icontains=question_name))
            return render(request,"technical/sdiCoummunity.html",{"questions":questions,"answers":answers})
        except:
            return render(request,"technical/sdiCoummunity.html",{'questions':questions,"answers":answers})
    if request.method == 'POST':
        upload = AnswerCreate(request.POST)
        if upload.is_valid():
            portfolio  = upload.save(commit=False)
            portfolio.profile_id = request.user.Profiles
            portfolio.question_id = Question.objects.get(id = request.POST.get('question_id'))
            portfolio.save()
            return redirect('community')
    else:
        upload = AnswerCreate()
    context = {'questions':questions ,'answers':answers,'upload_form':upload}
    return render(request,'technical/sdiCoummunity.html',context)





# update comment
@login_required
def update_comment(request, comment_id):
    comment_id = int(comment_id)
    try:
        comment_sel = Answer.objects.get(id = comment_id)
    except Answer.DoesNotExist:
        return redirect('community')
    comment_form = AnswerCreate(request.POST or None, instance = comment_sel)
    if comment_form.is_valid():
        comment_form.save()
        return redirect('community')
    return render(request, 'technical/sdiCoummunity.html', {'upload_form':comment_form})  


# delete comment from question
@login_required
def delete_comment(request, comment_id):
    comment_id = int(comment_id)
    try:
        comment_sel = Answer.objects.get(id = comment_id)
    except Answer.DoesNotExist:
        return redirect('community')
    comment_sel.delete()
    return redirect('community')





# create new question in community
@login_required
def communityUpload(request):
    # upload = CommunityCreate()
    if request.method == 'POST':
        upload = CommunityCreate(request.POST)
        if upload.is_valid():
            portfolio  = upload.save(commit=False)
            portfolio.profile_id = request.user.Profiles
            portfolio.save()
            return redirect('community')
    else:
        upload = CommunityCreate()
    return render(request, 'technical/sdicommunity/add.html', {'upload_form':upload})



# update a question in community
@login_required
def update_Question(request, question_id):
    problem_id = int(question_id)
    try:
        question_sel = Question.objects.get(id = question_id)
    except Question.DoesNotExist:
        return redirect('community')
    question_form = CommunityCreate(request.POST or None, instance = question_sel)
    if question_form.is_valid():
        question_form.save(commit=False)
        question_form.profile_id = request.user.Profiles
        question_form.save()
        return redirect('community')
    return render(request, 'technical/sdicommunity/add.html', {'upload_form':question_form})   


# delete question in community
@login_required
def delete_question(request, question_id):
    question_id = int(question_id)
    try:
        question_sel = Question.objects.get(id = question_id)
    except Question.DoesNotExist:
        return redirect('community')
    question_sel.delete()
    return redirect('community')






#  faq center for questions and answer CRUD operations
@login_required
def faqcenter(request):     
    shehta = Problems.objects.all()  
    if request.GET.get('search'): # write your form name here      
        problem_name =  request.GET.get('search')      
        try:
            shehta = Problems.objects.filter(Q(question__icontains=problem_name),Q(answer__icontains=problem_name))
            return render(request,"technical/faq-center.html",{"shehta":shehta})
        except:
            return render(request,"technical/faq-center.html",{'shehta':shehta})
    else:
        return render(request, 'technical/faq-center.html', {'shehta':shehta})





@login_required
def index(request):
    shehta = Problems.objects.all()
    paginator = Paginator(shehta, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'technical/faq-center/index.html' , {'page_obj':page_obj})


# for insert new question and answer
@login_required
def upload(request):
    upload = ProblemsCreate()
    if request.method == 'POST':
        upload = ProblemsCreate(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""يجب ادخال جميع الحقول المطلوبة <a href = "{{ url : 'index'}}">إعادة التحميل</a>""")
    else:
        return render(request, 'technical/faq-center/add.html', {'upload_form':upload})



# for update question or answer
@login_required
def update_problem(request, problem_id):
    problem_id = int(problem_id)
    try:
        problem_sel = Problems.objects.get(id = problem_id)
    except Problems.DoesNotExist:
        return redirect('index')
    problem_form = ProblemsCreate(request.POST or None, instance = problem_sel)
    if problem_form.is_valid():
       problem_form.save()
       return redirect('index')
    return render(request, 'technical/faq-center/add.html', {'upload_form':problem_form})   




# for delete problems
@login_required
def delete_problem(request, problem_id):
    problem_id = int(problem_id)
    try:
        problem_sel = Problems.objects.get(id = problem_id)
    except Problems.DoesNotExist:
        return redirect('index')
    if request.method == 'POST': 
        problem_sel.delete()
        return redirect('index')    
    return render(request, 'technical/faq-center/delete.html',{'user_sel':problem_sel})          



