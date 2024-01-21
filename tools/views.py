from django.shortcuts import render ,redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator
from datetime import datetime
from django.db.models import Q
from notifications.signals import notify #use for notifiy
from django.contrib.auth.decorators import login_required
# Create your views here.









# index for Extract_data
@login_required
def ExtractData(request):
    user = request.user.Profiles.id
    request_user = Extract_data.objects.filter(user_sender__id__startswith=user)
    requests = Extract_data.objects.all().order_by('-date')
    paginator = Paginator(requests, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'request_user':request_user}
    return render(request,'tools/data_extract/index.html',context)



# Create New Extract Data
@login_required
def ExtractDataCreate(request):
    if request.method == 'POST':
        upload = CreateExtract_data(request.POST,request.FILES)
        if upload.is_valid():
            upload.date = datetime.now()
            upload.save()
            return redirect('extract_data')
    else:
        upload = CreateExtract_data()
    return render(request, 'tools/data_extract/create.html', {'form':upload})     



# details for Extract Data
@login_required
def ExtractDataDetails(request,ExtractData_id):
    ExtractData_id = int(ExtractData_id)
    try:
        ExtractData_sel = Extract_data.objects.get(id = ExtractData_id)
    except Extract_data.DoesNotExist:
        return redirect('extract_data')    
    return render(request, 'tools/data_extract/details.html', {'merge_sel':ExtractData_sel})  





# response for Extract Data from admin only
@login_required
def ExtractDataResponse(request,ExtractData_id):
    ExtractData_id = int(ExtractData_id)        
    try:
        ExtractData_sel = Extract_data.objects.get(id = ExtractData_id)
    except Extract_data.DoesNotExist:
        return redirect('extract_data') 
    extract_form = CreateExtract_data(request.POST or None, request.FILES or None, instance = ExtractData_sel)
    if extract_form.is_valid():
        extract_form.date = ExtractData_sel.date
        ExtractData_sel.refuse_date = datetime.now()
        ExtractData_sel.response_date = datetime.now()
        extract_form.response_message = request.POST['response_message']
        extract_form.refuse_message = request.POST['refuse_message']
        extract_form.response_files = request.FILES.get('response_files','')
        # ExtractData_sel.save()
        extract_form.save()
        return redirect('extract_data')       
    return render(request, 'tools/data_extract/response.html', {'merge_form':extract_form,'merge_sel':ExtractData_sel}) 



# delete extract data requests
@login_required
def ExtractDataDelete(request , ExtractData_id) : 
    ExtractData_id = int(ExtractData_id)   
    try:
        ExtractData_sel = Extract_data.objects.get(id = ExtractData_id)
    except Extract_data.DoesNotExist:
        return redirect('extract_data')
    if request.method == 'POST': 
        ExtractData_sel.delete()
        return redirect('extract_data')
    context = {"item":ExtractData_sel}    
    return render(request, 'tools/data_extract/delete.html', context)



# index for mergeRequest
@login_required
def mergeRequest(request):
    user = request.user.Profiles.id
    request_user = MergeRequest.objects.filter(user_sender__id__startswith=user)
    requests = MergeRequest.objects.all().order_by('-date')
    paginator = Paginator(requests, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'request_user':request_user}
    return render(request,'tools/mergeRequest/index.html',context)


# Create New MergeRequest
@login_required
def mergeRequestCreate(request):
    if request.method == 'POST':
        upload = CreateMergeRequest(request.POST,request.FILES)
        if upload.is_valid():
            upload.date = datetime.now()
            upload.save()
            return redirect('mergeRequest')
    else:
        upload = CreateMergeRequest()
    return render(request, 'tools/mergeRequest/create.html', {'form':upload})     


    
# details for MegreRequest
@login_required
def mergeRequestDetails(request,mergeRequest_id):
    mergeRequest_id = int(mergeRequest_id)
    try:
        merge_sel = MergeRequest.objects.get(id = mergeRequest_id)
    except MergeRequest.DoesNotExist:
        return redirect('mergeRequest')    
    return render(request, 'tools/mergeRequest/details.html', {'merge_sel':merge_sel})  


# response for MergeRequest from admin only
@login_required
def mergeRequestResponse(request,mergeRequest_id):
    mergeRequest_id = int(mergeRequest_id)        
    try:
        merge_sel = MergeRequest.objects.get(id = mergeRequest_id)
    except MergeRequest.DoesNotExist:
        return redirect('mergeRequest') 
    merge_form = CreateMergeRequest(request.POST or None, request.FILES or None, instance = merge_sel)
    if merge_form.is_valid():
        merge_form.date = merge_sel.date
        merge_sel.refuse_date = datetime.now()
        merge_sel.response_date = datetime.now()
        merge_form.response_message = request.POST['response_message']
        merge_form.refuse_message = request.POST['refuse_message']
        merge_sel.save()
        merge_form.save()
        return redirect('mergeRequest')       
    return render(request, 'tools/mergeRequest/response.html', {'merge_form':merge_form,'merge_sel':merge_sel}) 


@login_required
def mergeRequestDelete(request , mergeRequest_id) : 
    mergeRequest_id = int(mergeRequest_id)
    try:
        mergeRequest_sel = MergeRequest.objects.get(id = mergeRequest_id)
    except MergeRequest.DoesNotExist:
        return redirect('mergeRequest')
    if request.method == 'POST': 
        print('delete')  
        mergeRequest_sel.delete()
        return redirect('mergeRequest')
    context = {"item":mergeRequest_sel}    
    return render(request, 'tools/mergeRequest/delete.html', context)



@login_required
# deplymentRequest index
def deploymentRequest(request):
    return render(request,'tools/DeploymentRequest/index.html')   



# deplymentRequest for apps index
@login_required
def deploymentRequestApp(request):
    user = request.user.Profiles.id
    request_user = DeploymentRequest_apps.objects.filter(user_sender__id__startswith=user)
    requests = DeploymentRequest_apps.objects.all().order_by('-date')
    paginator = Paginator(requests, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'request_user':request_user} 
    return render(request,'tools/DeploymentRequest/dashboard/index.html',context)    


# Create New deplymentRequest for apps
@login_required
def deploymentRequestAppCreate(request):
    publish_type = request.GET.get('type')
    if request.method == 'POST':
        upload = CreatedeploymentRequestApp(request.POST)
        if upload.is_valid():
            upload.date = datetime.now()
            upload.save()
            return redirect('deploymentRequestApp')
    else:
        upload = CreatedeploymentRequestApp()
    return render(request, 'tools/DeploymentRequest/dashboard/create.html', {'form':upload}) 



# response for deplymentRequest for apps from admin only
@login_required
def deploymentRequestAppResponse(request,deploymentRequestApp_id):
    deploymentRequestApp_id = int(deploymentRequestApp_id)        
    try:
        deploymentRequestApp_sel = DeploymentRequest_apps.objects.get(id = deploymentRequestApp_id)
    except DeploymentRequest_apps.DoesNotExist:
        return redirect('deploymentRequestApp') 
    deployment_form = CreatedeploymentRequestApp(request.POST or None, instance = deploymentRequestApp_sel)
    if deployment_form.is_valid():
        deployment_form.date = deploymentRequestApp_sel.date
        deploymentRequestApp_sel.refuse_date = datetime.now()
        deploymentRequestApp_sel.response_date = datetime.now()
        deployment_form.response_message = request.POST['response_message']
        deployment_form.refuse_message = request.POST['refuse_message']
        deploymentRequestApp_sel.save()
        deployment_form.save()
        return redirect('deploymentRequestApp')       
    return render(request, 'tools/DeploymentRequest/dashboard/response.html', {'merge_form':deployment_form,'merge_sel':deploymentRequestApp_sel})       




# details for deplymentRequest for apps
@login_required
def deploymentRequestAppDetails(request,deploymentRequestApp_id):
    deploymentRequestApp_id = int(deploymentRequestApp_id)
    try:
        deploymentRequest_sel = DeploymentRequest_apps.objects.get(id = deploymentRequestApp_id)
    except DeploymentRequest_apps.DoesNotExist:
        return redirect('deploymentRequestApp')    
    return render(request, 'tools/DeploymentRequest/dashboard/details.html', {'merge_sel':deploymentRequest_sel})  


# delete  deplymentRequest for apps
@login_required
def deploymentRequestAppDelete(request , deploymentRequestApp_id) : 
    deploymentRequestApp_id = int(deploymentRequestApp_id)
    try:
        deploymentRequest_sel = DeploymentRequest_apps.objects.get(id = deploymentRequestApp_id)
    except DeploymentRequest_apps.DoesNotExist:
        return redirect('deploymentRequestApp')
    if request.method == 'POST': 
        deploymentRequest_sel.delete()
        return redirect('deploymentRequestApp')  
    return render(request, 'tools/DeploymentRequest/dashboard/delete.html')



# ---------------------------------------
# -----------------------------------------
# طلب نشر لاتطبيقات 
# deplymentRequest for apps index
@login_required
def deploymentRequestApp2(request):
    user = request.user.Profiles.id
    request_user = DeploymentRequest_app2.objects.filter(user_sender__id__startswith=user)
    requests = DeploymentRequest_app2.objects.all().order_by('-date')
    paginator = Paginator(requests, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'request_user':request_user} 
    return render(request,'tools/DeploymentRequest/apps/index.html',context)    


# Create New deplymentRequest for apps
@login_required
def deploymentRequestAppCreate2(request):
    publish_type = request.GET.get('type')
    if request.method == 'POST':
        upload = CreatedeploymentRequestApp2(request.POST)
        if upload.is_valid():
            upload.date = datetime.now()
            upload.save()
            return redirect('deploymentRequestApp2')
    else:
        upload = CreatedeploymentRequestApp2()
    return render(request, 'tools/DeploymentRequest/apps/create.html', {'form':upload}) 


# details for deplymentRequest for apps
@login_required
def deploymentRequestAppDetails2(request,deploymentRequestApp_id):
    deploymentRequestApp_id = int(deploymentRequestApp_id)
    try:
        deploymentRequest_sel = DeploymentRequest_app2.objects.get(id = deploymentRequestApp_id)
    except DeploymentRequest_app2.DoesNotExist:
        return redirect('deploymentRequestApp2')    
    return render(request, 'tools/DeploymentRequest/apps/details.html', {'merge_sel':deploymentRequest_sel})  



# response for deplymentRequest for apps from admin only
@login_required
def deploymentRequestAppResponse2(request,deploymentRequestApp_id):
    deploymentRequestApp_id = int(deploymentRequestApp_id)        
    try:
        deploymentRequestApp_sel = DeploymentRequest_app2.objects.get(id = deploymentRequestApp_id)
    except DeploymentRequest_app2.DoesNotExist:
        return redirect('deploymentRequestApp2') 
    deployment_form = CreatedeploymentRequestApp2(request.POST or None, instance = deploymentRequestApp_sel)
    if deployment_form.is_valid():
        deployment_form.date = deploymentRequestApp_sel.date
        deploymentRequestApp_sel.refuse_date = datetime.now()
        deploymentRequestApp_sel.response_date = datetime.now()
        deployment_form.response_message = request.POST['response_message']
        deployment_form.refuse_message = request.POST['refuse_message']
        deploymentRequestApp_sel.save()
        deployment_form.save()
        return redirect('deploymentRequestApp2')       
    return render(request, 'tools/DeploymentRequest/apps/response.html', {'merge_form':deployment_form,'merge_sel':deploymentRequestApp_sel})       


# delete  deplymentRequest for apps
@login_required
def deploymentRequestAppDelete2(request , deploymentRequestApp_id) : 
    deploymentRequestApp_id = int(deploymentRequestApp_id)
    try:
        deploymentRequest_sel = DeploymentRequest_app2.objects.get(id = deploymentRequestApp_id)
    except DeploymentRequest_app2.DoesNotExist:
        return redirect('deploymentRequestApp2')
    if request.method == 'POST': 
        deploymentRequest_sel.delete()
        return redirect('deploymentRequestApp2')  
    return render(request, 'tools/DeploymentRequest/apps/delete.html')









# deplymentRequest index
@login_required
def deploymentRequestLayer(request):
    user = request.user.Profiles.id
    request_user = DeploymentRequest_layers.objects.filter(user_sender__id__startswith=user)
    requests = DeploymentRequest_layers.objects.all().order_by('-date')
    paginator = Paginator(requests, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'request_user':request_user}
    return render(request,'tools/DeploymentRequest/layers/index.html',context)    

# Create New deplymentRequest for layers
@login_required
def deploymentRequestLayerCreate(request):
    if request.method == 'POST':
        upload = CreatedeploymentRequestLayer(request.POST or None,request.FILES or None)
        if upload.is_valid():
            # upload.date = datetime.now()
            upload.source_img_date = request.POST['source_img_date']
            upload.source_img = request.POST['source_img']
            upload.img_date = request.POST['img_date']
            upload.medany_date = request.POST['medany_date']
            upload.medany_name = request.POST['medany_name']
            upload.save()
            return redirect('deploymentRequestLayer')
    else:
        upload = CreatedeploymentRequestLayer()
    return render(request, 'tools/DeploymentRequest/layers/create.html', {'form':upload}) 

# response for deplymentRequest for layers from admin only
@login_required
def deploymentRequestLayerResponse(request,deploymentRequestLayer_id):
    deploymentRequestLayer_id = int(deploymentRequestLayer_id)        
    try:
        deploymentRequestLayer_sel = DeploymentRequest_layers.objects.get(id = deploymentRequestLayer_id)
    except DeploymentRequest_apps.DoesNotExist:
        return redirect('deploymentRequestLayer') 
    deployment_form = CreatedeploymentRequestLayer(request.POST or None, request.FILES or None,instance = deploymentRequestLayer_sel)
    if deployment_form.is_valid():
        deployment_form.date = deploymentRequestLayer_sel.date
        deploymentRequestLayer_sel.refuse_date = datetime.now()
        deploymentRequestLayer_sel.response_date = datetime.now()
        deployment_form.response_message = request.POST['response_message']
        deployment_form.refuse_message = request.POST['refuse_message']
        deploymentRequestLayer_sel.save()
        deployment_form.save()
        return redirect('deploymentRequestLayer')       
    return render(request, 'tools/DeploymentRequest/layers/response.html', {'merge_form':deployment_form,'merge_sel':deploymentRequestLayer_sel})       




# details for deplymentRequest for layers
@login_required
def deploymentRequestLayerDetails(request,deploymentRequestLayer_id):
    deploymentRequestLayer_id = int(deploymentRequestLayer_id)
    try:
        deploymentRequest_sel = DeploymentRequest_layers.objects.get(id = deploymentRequestLayer_id)
    except DeploymentRequest_layers.DoesNotExist:
        return redirect('deploymentRequestLayer')    
    return render(request, 'tools/DeploymentRequest/layers/details.html', {'merge_sel':deploymentRequest_sel})  


# delete  deplymentRequest for layers
@login_required
def deploymentRequestLayerDelete(request , deploymentRequestLayer_id) : 
    deploymentRequestLayer_id = int(deploymentRequestLayer_id)
    try:
        deploymentRequest_sel = DeploymentRequest_layers.objects.get(id = deploymentRequestLayer_id)
    except DeploymentRequest_apps.DoesNotExist:
        return redirect('deploymentRequestLayer')
    if request.method == 'POST': 
        deploymentRequest_sel.delete()
        return redirect('deploymentRequestLayer')  
    return render(request, 'tools/DeploymentRequest/layers/delete.html')

















# inquiry Request index
@login_required
def inquiryRequest(request):
    user = request.user.Profiles.id
    acceptRequests = InquiryRequest.objects.filter(is_approved=0).count()
    request_count = InquiryRequest.objects.filter(user_reciver__id__startswith=user)
    context = {'acceptRequests':acceptRequests,'request_count':request_count}
    return  render(request, 'tools/inquiryrequest/index.html',context) 


# inquiry Request Create 
@login_required
def inquiryRequestCreate(request):
    if request.method == 'POST':
        upload = CreateInquiryRequest(request.POST,request.FILES)
        if upload.is_valid():
            upload.date = datetime.now()
            upload.save()
            return redirect('inquiryRequest')
    else:
        upload = CreateInquiryRequest()
    return render(request, 'tools/InquiryRequest/create.html', {'form':upload})

# inquiry Request accept requests 
@login_required
def inquiryRequestAcceptRequests(request):
    requests = InquiryRequest.objects.all().order_by('-request_date')
    paginator = Paginator(requests, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'requests':page_obj}
    return render(request , 'tools/inquiryrequest/acceptRequest.html',context)



# inquiry Request Details 
@login_required
def inquiryRequestDetails(request,inquiryRequest_id):
    inquiryRequest_id = int(inquiryRequest_id)
    try:
        inquiryRequest_sel = InquiryRequest.objects.get(id = inquiryRequest_id)
    except InquiryRequest.DoesNotExist:
        return redirect('inquiryRequest')    
    return render(request, 'tools/inquiryrequest/details.html', {'merge_sel':inquiryRequest_sel})  



# response the request from admin then will pass it to the user_reciver
@login_required
def inquiryRequestAccept(request,inquiryRequest_id):
    inquiryRequest_id = int(inquiryRequest_id)        
    try:
        inquiryRequest_sel = InquiryRequest.objects.get(id = inquiryRequest_id)
    except InquiryRequest.DoesNotExist:
        return redirect('inquiryRequest') 
    if request.method == 'POST':   
        inquiryRequest_sel.is_approved =  1 
        inquiryRequest_sel.save() 
        return redirect('inquiryRequest')       
    return render(request, 'tools/inquiryrequest/accept.html', {'merge_sel':inquiryRequest_sel}) 



# refuse request from admin 
@login_required
def inquiryRequestRefuse(request,inquiryRequest_id):
    inquiryRequest_id = int(inquiryRequest_id)        
    try:
        inquiryRequest_sel = InquiryRequest.objects.get(id = inquiryRequest_id)
    except InquiryRequest.DoesNotExist:
        return redirect('inquiryRequest') 
    if request.method == 'POST':   
        inquiryRequest_sel.is_approved =  2
        inquiryRequest_sel.refuse_admin_date =  datetime.now()
        inquiryRequest_sel.refuse_admin_message = request.POST['refuse_admin_message']  
        inquiryRequest_sel.save() 
        return redirect('inquiryRequest')       
    return render(request, 'tools/inquiryrequest/refuse.html', {'merge_sel':inquiryRequest_sel}) 



# inquiry request for recive
@login_required
def inquiryRequestRecive(request):
    user = request.user.Profiles.id
    request_user = InquiryRequest.objects.filter(user_reciver__id__startswith=user).order_by('-request_date')
    requests = InquiryRequest.objects.all().order_by('-request_date')
    paginator = Paginator(requests, 4)
    page_number = request.GET.get('page')
    paginator2 = Paginator(request_user, 4)
    page_obj2 = paginator2.get_page(page_number)
    page_obj = paginator.get_page(page_number)
    context = {'requests':page_obj,'page_obj2':page_obj2}
    return render(request , 'tools/inquiryrequest/recive.html',context)


# response for inquiry request from user_reciver 
@login_required
def inquiryRequestResponse(request, inquiryRequest_id):
    inquiryRequest_id = int(inquiryRequest_id)        
    try:
        inquiryRequest_sel = InquiryRequest.objects.get(id = inquiryRequest_id)
    except InquiryRequest.DoesNotExist:
        return redirect('inquiryRequest') 
    if request.method == 'POST':
        if  request.POST['refuse_message'] =='' :
            inquiryRequest_sel.is_approved =  3
            inquiryRequest_sel.response_message =  request.POST['response_message']
            inquiryRequest_sel.response_date =  datetime.now()
            inquiryRequest_sel.response_file =  request.FILES['response_file']
            inquiryRequest_sel.response_url =  request.POST['response_url']
            inquiryRequest_sel.save() 
            return redirect('inquiryRequest') 
        else:
            inquiryRequest_sel.is_approved =  4
            inquiryRequest_sel.refuse_message =  request.POST['refuse_message']
            inquiryRequest_sel.refuse_date =  datetime.now()
            inquiryRequest_sel.save() 
            return redirect('inquiryRequest')       
    return render(request, 'tools/inquiryrequest/response.html', {'merge_sel':inquiryRequest_sel}) 

# inquiry request for send
@login_required
def inquiryRequestSend(request):
    user = request.user.Profiles.id
    request_user = InquiryRequest.objects.filter(user_sender__id__startswith=user).order_by('-request_date')
    requests = InquiryRequest.objects.all().order_by('-request_date')
    paginator = Paginator(requests, 4)
    page_number = request.GET.get('page')
    paginator2 = Paginator(request_user, 4)
    page_obj2 = paginator2.get_page(page_number)
    page_obj = paginator.get_page(page_number)
    context = {'requests':page_obj,'page_obj2':page_obj2}
    return render(request , 'tools/inquiryrequest/send.html',context)
    




# inquiry request arcieve
@login_required
def inquiryRequestArcieve(request):
    user = request.user.Profiles.id
    request_user = InquiryRequest.objects.filter(Q(user_sender__id__startswith = user) | Q(user_reciver__id__startswith = user)).order_by('-request_date')
    requests = InquiryRequest.objects.all().order_by('-request_date')
    paginator = Paginator(requests, 4)
    page_number = request.GET.get('page')
    paginator2 = Paginator(request_user, 4)
    page_obj2 = paginator2.get_page(page_number)
    page_obj = paginator.get_page(page_number)
    context = {'requests':page_obj,'page_obj2':page_obj2}
    return render(request , 'tools/inquiryrequest/archieve.html',context)

# inquiry request delete 
@login_required
def inquiryRequestDelete(request , inquiryRequest_id) : 
    inquiryRequest_id = int(inquiryRequest_id)
    try:
        inquiryRequest_sel = InquiryRequest.objects.get(id = inquiryRequest_id)
    except InquiryRequest.DoesNotExist:
        return redirect('inquiryRequest')
    if request.method == 'POST': 
        inquiryRequest_sel.delete()
        return redirect('inquiryRequest')  
    return render(request, 'tools/inquiryRequest/delete.html')













# this use for load dropdown menu in country >> state >> city
@login_required
def load_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'tools/inquiryrequest/state_options.html', {'states': states})

@login_required
def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'tools/inquiryrequest/city_options.html', {'cities': cities})






# my layers function
def myLayer(request):
    all_layer = DeploymentRequest_layers.objects.all()
    paginator = Paginator(all_layer, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, 'tools/layers/mylayer.html',context )



#layer Deatils 
def layerDetails(request,layer_id):
    layer_id = int(layer_id)
    try:
        layer_id_sel = DeploymentRequest_layers.objects.get(id = layer_id)
    except InquiryRequest.DoesNotExist:
        return redirect('my_layer')    
    return render(request, 'tools/layers/layerDetails.html', {'layer_sel':layer_id_sel})  

              