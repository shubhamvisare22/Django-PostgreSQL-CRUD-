from django.urls import path 
from . import student_views, teacher_views,department_views
urlpatterns = [
    # ----------------- Student -------------------
    path ('get-student/<int:stud_id>', student_views.get_student, name='get_student'),
    path ('list-student', student_views.list_student, name='list_student'),
    path ('create-student', student_views.create_student, name='create_student'),
    path ('update-student/<int:stud_id>', student_views.update_student, name='update_student'),
    path ('delete-student/<int:stud_id>', student_views.delete_student, name='delete_student'),
    
    # ----------------- teacher -------------------
    path ('get-teacher/<int:teacher_id>', teacher_views.get_teacher, name='get_teacher'),
    path ('list-teacher', teacher_views.list_teacher, name='list_steacher'),
    path ('create-teacher', teacher_views.create_teacher, name='create_teacher'),
    path ('update-teacher/<int:teacher_id>', teacher_views.update_teacher, name='update_teacher'),
    path ('delete-teacher/<int:teacher_id>', teacher_views.delete_teacher, name='delete_teacher'),
    
    # ----------------- department -------------------
    path ('list-dept', department_views.list_dept, name='list_dept'),
    path ('create-dept', department_views.create_dept, name='create_dept'),
    path ('update-dept/<int:dept_id>', department_views.update_dept, name='update_dept'),
    path ('delete-dept/<int:dept_id>', department_views.delete_dept, name='delete_dept'),
    
    # ------------------- search --------------------- 
    path ('search-dept', department_views.search_dept, name='search_dept'),
    path ('search-student', student_views.search_stud, name='search_stud'),
    path ('search-teacher', teacher_views.search_teacher, name='search_teacher'),
    
]

