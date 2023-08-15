from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Teacher
from django.db.models import Q


# ---------------- Student ----------------------------
@csrf_exempt
def list_student(request):
    if request.method != 'GET':
        return JsonResponse({"msg": "invalid Request Method."})

    stud_obj = Student.objects.all().values()
    return JsonResponse({"data": list(stud_obj)})


def get_student(request, stud_id):
    if request.method != "GET":
        return JsonResponse({"msg": "invalid Request Method."})
    
    stud_obj = Student.objects.get(id=stud_id)
    return JsonResponse({"data": {"id":stud_obj.id,"name":stud_obj.name, "age":stud_obj.age,"eamil":stud_obj.email, "class_teacher":stud_obj.class_teacher.name}})


@csrf_exempt
def create_student(request):
    if request.method != 'POST':
        return JsonResponse({"msg": "invalid Request Method."})

    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')
    class_teacher_name = request.POST.get('class_teacher')

    # Teacher is Foreign key
    try:
        # teacher name will be case insensetive
        class_teacher = Teacher.objects.get(Q(name__iexact=class_teacher_name))
    except Teacher.DoesNotExist:
        return JsonResponse({"msg": "Teacher with the given name does not exist."}, status=400)

    print(f'{name}<--->{email}<--->{age}<--->{class_teacher}')
    Student.objects.create(name=name, email=email,
                           age=age, class_teacher=class_teacher)
    return JsonResponse({"msg": "Student Record Saved."})


@csrf_exempt
def update_student(request, stud_id):
    if request.method != "POST":
        return JsonResponse({"msg": "Invalid Request method"})
    
    # student validation
    try:
        stud_obj = Student.objects.get(id=stud_id)
    except Student.DoesNotExist:
        return JsonResponse({"msg": "Student with the given ID does not exist."}, status=400)
        

    if stud_obj:
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        class_teacher_name = request.POST.get('class_teacher')

        
        # Teacher validation
        try:
            class_teacher = Teacher.objects.get(
                Q(name__iexact=class_teacher_name))
        except Teacher.DoesNotExist:
            return JsonResponse({"msg": "Teacher with the given name does not exist."}, status=400)

        stud_obj.name = name
        stud_obj.email = email
        stud_obj.age = age
        stud_obj.class_teacher = class_teacher
        stud_obj.save()
        return JsonResponse({"msg": "Student Record Updated."})


@csrf_exempt
def delete_student(request, stud_id):
    if request.method != "POST":
        return JsonResponse({"msg": "Invalid Request method"})

    try:
        stud_obj = Student.objects.get(id=stud_id)
    except Student.DoesNotExist:
        return JsonResponse({"msg": "Student with the given ID does not exist."}, status=400)

    if stud_obj:
        stud_obj.delete()
        return JsonResponse({"msg": "Student Record deleted."})

# search 
@csrf_exempt
def search_stud(request):
    search_query = request.GET.get('search')
    
    if not search_query:
        return JsonResponse({'msg':'Enter the Student Name to search'})
        
    if search_result := Student.objects.filter(name__icontains=str(search_query).strip()):
        print(search_result)
        return JsonResponse({'msg':'Matched Student Found', 'data':list(search_result.values())})
        
    return JsonResponse({'msg':'Student Data Not Found'})

