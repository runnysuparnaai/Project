from django.shortcuts import render
from rest_framework import viewsets         
from .serializers import m_vaccination_centerSerializer  
from .serializers import m_vaccination_center_historySerializer
from .models import m_vaccination_center
from .models import m_vaccination_center_history
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer 
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import datetime
from rest_framework.decorators import api_view

class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type']='application/json'
        super(JSONResponse,self).__init__(content,**kwargs)


@api_view(['GET'])
def apiOverview(request):
    vaccination_url={

       'vaccenters/new_vac_centers',
       'vaccenters/update_vac_centers/<str:code>',
       'vaccenters/vac_centre_approvals/<int:workflow_seq_no>/<str:user_id>/',
       'vaccenters/<str:code>',
       'vaccenters_zip_code/<str:zip_code>',
       'vaccenters_key_level_2/<str:key_level2_jurisdiction_code>',   
       'vaccenters_key_level_1/<str:key_level1_jurisdiction_code>',
       'vaccenters_ou_code/<str:ou_code>',
       'vaccenters_admin_code/<str:admin_code>', 
    } 
  
    return Response(vaccination_url)

@csrf_exempt
def m_vaccination_center_list(request):
    if request.method == 'GET':
        vacc_center_api = m_vaccination_center.objects.all()
        vaccination_center_serializer = m_vaccination_centerSerializer(vacc_center_api, many=True)
        return JsonResponse(vaccination_center_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
 
    elif request.method == 'POST':
        vacc_center_api = JSONParser().parse(request)
        vaccination_center_serializer = m_vaccination_centerSerializer(data=vacc_center_api)
        if vaccination_center_serializer.is_valid():
            vaccination_center_serializer.save() 
            return JsonResponse(vaccination_center_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(vaccination_center_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@csrf_exempt
def m_vaccination_center_code(request,code):
    try:
        vacc_center_api=m_vaccination_center.objects.filter(code=code)
       
    except m_vaccination_center.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        vaccination_center_serializer =m_vaccination_centerSerializer(vacc_center_api,many=True)
        return JsonResponse(vaccination_center_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
 
    elif request.method == 'PUT':
        vacc_center_data = JSONParser().parse(request)
        vacc_center_serializer = m_api_implementationSerializer(vacc_center_api,data=vacc_center_data)
        if vacc_center_serializer.is_valid():
            vacc_center_serializer.save() 
            return JsonResponse(vacc_center_serializer.data) 
        return JsonResponse(vacc_center_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        vacc_center_api.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)  

@csrf_exempt
def m_vaccination_center_zip_code(request,zip_code):
    try:
        vacc_center_api=m_vaccination_center.objects.filter(zip_code=zip_code)
       
    except m_vaccination_center.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        vaccination_center_serializer =m_vaccination_centerSerializer(vacc_center_api,many=True)
        return JsonResponse(vaccination_center_serializer.data, safe=False)
              
@csrf_exempt
def m_vaccination_center_key_level2(request,key_level2_jurisdiction_code):
    try:
        vacc_center_api=m_vaccination_center.objects.filter(key_level2_jurisdiction_code=key_level2_jurisdiction_code)
       
    except m_vaccination_center.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        vaccination_center_serializer =m_vaccination_centerSerializer(vacc_center_api,many=True)
        return JsonResponse(vaccination_center_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
 
@csrf_exempt
def m_vaccination_center_key_level1(request,key_level1_jurisdiction_code):
    try:
        vacc_center_api=m_vaccination_center.objects.filter(key_level1_jurisdiction_code=key_level1_jurisdiction_code)
       
    except m_vaccination_center.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        vaccination_center_serializer =m_vaccination_centerSerializer(vacc_center_api,many=True)
        return JsonResponse(vaccination_center_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
 
@csrf_exempt
def m_vaccination_center_ou_code(request,ou_code):
    try:
        vacc_center_api=m_vaccination_center.objects.filter(ou_code=ou_code)
       
    except m_vaccination_center.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        vaccination_center_serializer =m_vaccination_centerSerializer(vacc_center_api,many=True)
        return JsonResponse(vaccination_center_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

@csrf_exempt
def m_vaccination_center_admin_code(request,admin_code):
    try:
        vacc_center_api=m_vaccination_center.objects.filter(admin_code=admin_code)
       
    except m_vaccination_center.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        vaccination_center_serializer =m_vaccination_centerSerializer(vacc_center_api,many=True)
        return JsonResponse(vaccination_center_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

@csrf_exempt
def vaccination_center_approval(request,workflow_seq_no,user_id):
    try:
        vacc_center_api=m_vaccination_center.objects.filter(workflow_seq_no=workflow_seq_no,user_id=user_id)
       
    except m_vaccination_center.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        vaccination_center_serializer =m_vaccination_centerSerializer(vacc_center_api,many=True)
        return JsonResponse(vaccination_center_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

@csrf_exempt
def update_vac_center_status(request,code):
    try:
        print(timezone.now())  
        vacc_center_api=m_vaccination_center.objects.get(code=code,active_from__lte=timezone.now())
        #print(vacc_center_api)
       # print((m_vaccination_center.objects.filter(code=record_key,active_from__lte=timezone.now())).query)
    except m_vaccination_center.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
       # print(vacc_center_api.query)
        vaccination_center_serializer =m_vaccination_centerSerializer(vacc_center_api)
        return JsonResponse(vaccination_center_serializer.data,status=status.HTTP_200_OK)        

    elif request.method == 'PUT':
        vacc_data = JSONParser().parse(request)
        vacc_serializer = m_vaccination_centerSerializer(vacc_center_api,data=vacc_data)
        vacc_his_serializer=m_vaccination_center_historySerializer(vacc_center_api,data=vacc_data)
        if vacc_serializer.is_valid():
            vacc_serializer.save() 
            if vacc_his_serializer.is_valid():
                vacc_his_serializer.save()
                return JsonResponse(vacc_his_serializer.data,status=status.HTTP_200_OK)

            return JsonResponse(vacc_serializer.data,status=status.HTTP_200_OK) 
        return JsonResponse(vacc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
def m_vaccination_center_history_list(request):
    if request.method == 'GET':
        vac_center_histry_data = m_vaccination_center_history.objects.all()
        vacc_center_history_serializer = m_vaccination_center_historySerializer(vac_center_histry_data, many=True)
        return JsonResponse(vacc_center_history_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
 
    elif request.method == 'POST':
        vac_center_histry_data = JSONParser().parse(request)
        vacc_center_history_serializer = m_vaccination_center_historySerializer(data=vac_center_histry_data)
        if vacc_center_history_serializer.is_valid():
            vacc_center_history_serializer.save() 
            return JsonResponse(vacc_center_history_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(vacc_center_history_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@csrf_exempt
def m_vaccination_center_history_detail(request,code):
    try:
        vac_history_data=m_vaccination_center_history.objects.filter(code=code)
       
    except m_vaccination_center_history.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        vacc_history_serializer =m_vaccination_center_historySerializer(vac_history_data,many=True)
        return JsonResponse(vacc_history_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
 
    elif request.method == 'PUT':
        vac_history_api = JSONParser().parse(request)
        vacc_history_serializer = m_api_implementationSerializer(vac_history_data,data=vac_history_api)
        if vacc_history_serializer.is_valid():
            vacc_history_serializer.save() 
            return JsonResponse(vacc_history_serializer.data) 
        return JsonResponse(vacc_history_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        vac_history_data.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)            

        