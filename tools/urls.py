from django.urls import path , include
from tools import views


urlpatterns = [
    # طبقاتى 
    path('my_layer/', views.myLayer,name="my_layer" ),
    path('my_layer/<int:layer_id>', views.layerDetails,name="layerDetails" ),
     # طلب استخراج البيانات
    path('extract/', views.ExtractData,name="extract_data" ),
    path('extract/create', views.ExtractDataCreate,name="extract_data-create" ),
    path('extract/details/<int:ExtractData_id>', views.ExtractDataDetails,name="extract_data-details" ),
    path('extract/response/<int:ExtractData_id>', views.ExtractDataResponse,name="extract_data-response" ),
    path('extract/delete/<int:ExtractData_id>', views.ExtractDataDelete,name="extract_data-delete" ),
     # طلب الدمج
    path('merge/', views.mergeRequest,name="mergeRequest" ),
    path('merge/create', views.mergeRequestCreate,name="mergeRequest-create" ),
    path('merge/details/<int:mergeRequest_id>', views.mergeRequestDetails,name="mergeRequest-details" ),
    path('merge/response/<int:mergeRequest_id>', views.mergeRequestResponse,name="mergeRequest-response" ),
    path('merge/delete/<int:mergeRequest_id>', views.mergeRequestDelete,name="mergeRequest-delete" ),
   # طلب النشر
    path('depolyment/', views.deploymentRequest,name="deploymentRequest" ),
    #طلب نشر مؤشرات الاداء
    path('depolyment/apps/index', views.deploymentRequestApp,name="deploymentRequestApp" ),
    path('depolyment/apps/create', views.deploymentRequestAppCreate,name="deploymentRequestApp-create" ),
    path('depolyment/apps/details/<int:deploymentRequestApp_id>', views.deploymentRequestAppDetails,name="deploymentRequestApp-details" ),
    path('depolyment/apps/response/<int:deploymentRequestApp_id>', views.deploymentRequestAppResponse,name="deploymentRequestApp-response" ),
    path('depolyment/apps/delete/<int:deploymentRequestApp_id>', views.deploymentRequestAppDelete,name="deploymentRequestApp-delete" ),
    #طلب نشر التطبيقات
    path('depolyment/apps2/index', views.deploymentRequestApp2,name="deploymentRequestApp2" ),
    path('depolyment/apps2/create', views.deploymentRequestAppCreate2,name="deploymentRequestApp-create2" ),
    path('depolyment/apps2/details/<int:deploymentRequestApp_id>', views.deploymentRequestAppDetails2,name="deploymentRequestApp-details2" ),
    path('depolyment/apps2/response/<int:deploymentRequestApp_id>', views.deploymentRequestAppResponse2,name="deploymentRequestApp-response2" ),
    path('depolyment/apps2/delete/<int:deploymentRequestApp_id>', views.deploymentRequestAppDelete2,name="deploymentRequestApp-delete2" ),
    # طلب نشر الطبقات
    path('depolyment/layers/index', views.deploymentRequestLayer,name="deploymentRequestLayer" ),
    path('depolyment/layers/create', views.deploymentRequestLayerCreate,name="deploymentRequestLayer-create" ),
    path('depolyment/layers/details/<int:deploymentRequestLayer_id>', views.deploymentRequestLayerDetails,name="deploymentRequestLayer-details" ),
    path('depolyment/layers/response/<int:deploymentRequestLayer_id>', views.deploymentRequestLayerResponse,name="deploymentRequestLayer-response" ),
    path('depolyment/layers/delete/<int:deploymentRequestLayer_id>', views.deploymentRequestLayerDelete,name="deploymentRequestLayer-delete" ),
    #طلب الاستعلام
    path('inquiryrequest', views.inquiryRequest,name="inquiryRequest" ),
    path('inquiryrequest/create', views.inquiryRequestCreate,name="inquiryRequestCreate" ),
    path('inquiryrequest/acceptRequests', views.inquiryRequestAcceptRequests,name="inquiryRequestAcceptRequests" ),  # قبول الطلبات
    path('inquiryrequest/details/<int:inquiryRequest_id>', views.inquiryRequestDetails,name="inquiryRequestDetails" ), # تفاصيل الطلبات
    path('inquiryrequest/accept/<int:inquiryRequest_id>', views.inquiryRequestAccept,name="inquiryRequestAccept" ), # accept form admin
    path('inquiryrequest/refuse/<int:inquiryRequest_id>', views.inquiryRequestRefuse,name="inquiryRequestRefuse" ), #refuse from admin
    path('inquiryrequest/recive', views.inquiryRequestRecive,name="inquiryRequestRecive" ), #refuse from admin
    path('inquiryrequest/response/<int:inquiryRequest_id>', views.inquiryRequestResponse,name="inquiryRequestResponse" ), #refuse from admin
    path('inquiryrequest/send', views.inquiryRequestSend,name="inquiryRequestSend" ), #refuse from admin
    path('inquiryrequest/archieve', views.inquiryRequestArcieve,name="inquiryRequestArcieve" ), #refuse from admin
    path('inquiryrequest/delete/<int:inquiryRequest_id>', views.inquiryRequestDelete,name="inquiryRequestDelete" ), #delete Inquiry request from admin
    # تحميل المحافظات والمراكز والشياخات
    path('ajax/load-states/', views.load_states, name='ajax_load_states'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

]