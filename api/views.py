from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from .models import user, activity_periods
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def fetchData_api(request):
    output = {'ok':False, 'members' : []}
    try:
        all_user_data = user.objects.all()
        for each_user in all_user_data:
            activity_period = activity_periods.objects.filter(user_id=each_user)
            activity_list = list(activity_period.values('start_time','end_time'))
            output['members'].append(dict(id=each_user.id , real_name=each_user.real_name, tz=each_user.tz, activity_periods=activity_list))
        output['ok'] = True
        return JsonResponse(output ,  safe=False)
    except Exception as e:
        print(e)
        return JsonResponse(output ,  safe=False, status=500)

def index(request):
    data = user.objects.all()
    return render(request, 'index.html', {'data':data})

@csrf_exempt
def datainsertion(request):
    try:
        if request.method == 'POST':
            name_selected = request.POST['name_selected']
            if name_selected == 'new':
                name = request.POST['name']
                id = request.POST['id']
                time_zone = request.POST['time_zone']
                connection_user = user()
                connection_user.id= id
                connection_user.real_name= name
                connection_user.tz= time_zone
                try:
                    connection_user.save()
                    return JsonResponse({"status":"success"}, status=200)
                except Exception as e:
                    return JsonResponse({"status":"error"} , status=500)    
            else:
                id = request.POST['id']
                start_time = request.POST['start_time']
                end_time = request.POST['end_time']
                user_instance = user.objects.get(id = id)
                connection_activity = activity_periods()
                connection_activity.user_id= user_instance
                connection_activity.start_time= start_time
                connection_activity.end_time= end_time
                try:
                    connection_activity.save()
                    return JsonResponse({"status":"success"} , status=200)
                except Exception as e:
                    return JsonResponse({"status":"error"} , status=500)
    except Exception as e:
        print(e)
        return JsonResponse({"message":"Unable to complete your request."} ,  safe=False, status=500)


        
        
    