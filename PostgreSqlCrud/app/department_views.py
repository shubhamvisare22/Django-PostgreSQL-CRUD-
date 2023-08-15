from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Department


# -------------------------- Department --------------------------------
@csrf_exempt
def list_dept(request):
    if request.method != 'GET':
        return JsonResponse({"msg": "invalid Request Method."})
    dept_obj = Department.objects.all().values().order_by('id')
    return JsonResponse({"data": list(dept_obj)})


@csrf_exempt
def create_dept(request):
    if request.method != 'POST':
        return JsonResponse({"msg": "invalid Request Method."})
    
    name = request.POST.get('name')
    if not name:
        return JsonResponse({"msg": "Enter the Department"})
    
    Department.objects.create(name=name)
    return JsonResponse({"msg": "Department Record Saved."})
    
    


@csrf_exempt
def update_dept(request, dept_id):
    if request.method != "POST":
        return JsonResponse({"msg": "Invalid Request method"})

    # validation to check Department
    try:
        dept = Department.objects.get(id=dept_id)
    except Department.DoesNotExist:
        return JsonResponse({"msg": "Department with the given ID does not exist."}, status=400)

    name = request.POST.get('name')
    if not name:
        return JsonResponse({"msg": "Please enter department Name"},status= 400 )
    
    if dept:
        dept.name = name
        dept.save()
        return JsonResponse({"msg": "Department Record Updated."})
        



@csrf_exempt
def delete_dept(request, dept_id):
    if request.method != "POST":
        return JsonResponse({"msg": "Invalid Request method"})

    # validation to check Department
    try:
        dept = Department.objects.get(id=dept_id)
    except Department.DoesNotExist:
        return JsonResponse({"msg": "Department with the given ID does not exist."}, status=400)

    if dept:
        dept.delete()
        return JsonResponse({"msg": "Department Record Deleted."})


@csrf_exempt
def search_dept(request):
    search_query = request.GET.get('search')
    
    if not search_query:
        return JsonResponse({'msg':'Enter the Department Name to search'})
        
    if search_result := Department.objects.filter(name__icontains=str(search_query).strip()):
        print(search_result)
        return JsonResponse({'msg':'Matched Department Found', 'data':list(search_result.values())})
        
    return JsonResponse({'msg':'No Match Found'})
    
    
    
    
