from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import  Teacher



# -------------------------- teacher --------------------------------
@csrf_exempt
def list_teacher(request):
    if request.method != 'GET':
        return JsonResponse({"msg": "invalid Request Method."})
    teacher_obj = Teacher.objects.all().values()
    return JsonResponse({"data": list(teacher_obj)})


def get_teacher(request, teacher_id):
    if request.method != "GET":
        return JsonResponse({"msg": "invalid Request Method."})
    teacher_obj = Teacher.objects.get(id = teacher_id)
    return JsonResponse({"data": {"id":teacher_obj.id,"name":teacher_obj.name, "age":teacher_obj.age,"eamil":teacher_obj.email}})


@csrf_exempt
def create_teacher(request):
    if request.method != 'POST':
        return JsonResponse({"msg": "invalid Request Method."})

    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')
    print(f'{name}::{email}::{age}')
    Teacher.objects.create(name=name, email=email, age=age)
    return JsonResponse({"msg": "Teacher Record Saved."})


@csrf_exempt
def update_teacher(request, teacher_id):
    if request.method != "POST":
        return JsonResponse({"msg": "Invalid Request method"})

    # validation to check teacher
    try:
        teacher = Teacher.objects.get(id=teacher_id)
    except Teacher.DoesNotExist:
        return JsonResponse({"msg": "Teacher with the given ID does not exist."}, status=400)

    if teacher:
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        teacher.name = name
        teacher.email = email
        teacher.age = age
        teacher.save()
        return JsonResponse({"msg": "Teacher Record Updated."})


@csrf_exempt
def delete_teacher(request, teacher_id):
    if request.method != "POST":
        return JsonResponse({"msg": "Invalid Request method"})

    # validation to check teacher
    try:
        teacher = Teacher.objects.get(id=teacher_id)
    except Teacher.DoesNotExist:
        return JsonResponse({"msg": "Teacher with the given ID does not exist."}, status=400)

    if teacher:
        teacher.delete()
        return JsonResponse({"msg": "Teacher Record Deleted."})


# search 
@csrf_exempt
def search_teacher(request):
    search_query = request.GET.get('search')
    
    if not search_query:
        return JsonResponse({'msg':'Enter the Teacher Name to search'})
        
    if search_result := Teacher.objects.filter(name__icontains=str(search_query).strip()):
        print(search_result)
        return JsonResponse({'msg':'Matched Teacher Found', 'data':list(search_result.values())})
        
    return JsonResponse({'msg':'Teacher Data Not Found'})

