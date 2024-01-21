from django.shortcuts import render, HttpResponse
import psycopg2
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Create your views here.







#  get the seragid from x and y 
@api_view(['GET'])
def my_query(request):
    x =request.GET.get('x')
    y =request.GET.get('y')
    # seragid = request.GET.get('seragid')
    conn = psycopg2.connect(database="05_74k_basemap", user="postgres", password="postgres", host="10.100.100.185", port="5432")
    # Query the database and retrieve the data
    cur = conn.cursor()
    # cur.execute("select ST_SetSRID(ST_MakePoint(%s, %s), 4326)", (x, y))
    cur.execute("SELECT * FROM public.building_3857_map WHERE ST_Contains(public.building_3857_map.geom, ST_SetSRID(ST_MakePoint(ST_X(ST_Transform(ST_SetSRID(ST_MakePoint("+x+", "+y+"), 4326), 3857)), ST_Y(ST_Transform(ST_SetSRID(ST_MakePoint("+x+", "+y+"), 4326), 3857))), 3857))")
    data = cur.fetchall()
    res = {     
    "id":data[0][0],
    "seragid" :data[0][9],
    "gov":data[0][10],
    "sec":data[0][11],
    "ssec":data[0][12],
    
    }
    return JsonResponse(res, safe=False)







# send data to 
# @login_required
@csrf_exempt
def Send_Data(request):
    try:
        if request.method == 'POST':
            json_data = request.body.decode('utf-8')
            data = json.loads(json_data)
            id_basemap =data.get('id_basemap','')
            code_id = data.get('id_code','')
            id_geha =data.get('id_geha','')
            conn = psycopg2.connect(database="05_74k_basemap", user="postgres", password="postgres", host="10.100.100.185", port="5432")
        #     # Query the database and retrieve the data
            cur = conn.cursor()
            time = datetime.datetime.now()
            x = "insert into public.code_gehat (id_geha,id_building_basemap,code_geha,date) values ("+ str(id_geha)+","+ str(id_basemap) +","+ str(code_id)+",'"+ str(time)+"');"
            cur.execute(x)
            conn.commit()
            res = {
                "message" :"Data send sucessfuly.",
            }
            return JsonResponse(res, safe=False)
    except Exception as e:
        return HttpResponse(e)    



#  return data depend on geom and get all building in this geom
@api_view(['GET'])
def response_csv(request):
    coordinate =request.GET.get('geom')
    conn = psycopg2.connect(database="05_74k_basemap", user="postgres", password="postgres", host="10.100.100.185", port="5432")
    # Query the database and retrieve the data
    cur = conn.cursor()
    # cur.execute("select ST_SetSRID(ST_MakePoint(%s, %s), 4326)", (x, y))
    q ="select seragid , x ,y  from public.building_3857_map where ST_intersects(geom,(SELECT ST_   000 mGeoJSON('"+coordinate+"'),3857) AS geom))"

    cur.execute(q)
    data = cur.fetchall()
    return JsonResponse(data, safe=False)




#  return data depend on user and get all data from this user
@api_view(['GET'])
def export_csv(request):
    user_id =request.GET.get('user_id')
    conn = psycopg2.connect(database="05_74k_basemap", user="postgres", password="postgres", host="10.100.100.185", port="5432")
    # Query the database and retrieve the data
    cur = conn.cursor()
    # cur.execute("select ST_SetSRID(ST_MakePoint(%s, %s), 4326)", (x, y))
    q ="select seragid,code_geha,x_nsdi,y_nsdi,date from public.finalgehate where id_geha ="+user_id +";"
    cur.execute(q)
    data = cur.fetchall()
    return JsonResponse(data, safe=False)





#  return data depend on user and serag ID to that code is aleraady exists
@api_view(['GET'])
def check_serag(request):
    user_id =request.GET.get('user_id')
    id_basemap = request.GET.get('id_basemap')
    conn = psycopg2.connect(database="05_74k_basemap", user="postgres", password="postgres", host="10.100.100.185", port="5432")
    # Query the database and retrieve the data
    cur = conn.cursor()
    q ="select code_geha from public.code_gehat where id_geha =" + str(user_id) + " and id_building_basemap="+ str(id_basemap)+";"
    cur.execute(q)
    data = cur.fetchall()
    return JsonResponse(data, safe=False)


@login_required
def inquiry(request):
    return render(request,'inquiry_app.html') 


@login_required
def MergeApp(request):
    user_id = request.user.Profiles.id
    context={'user_id' :user_id}
    return render(request,'merge_app.html',context) 

