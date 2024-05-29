from django.shortcuts import render
from .models import Students
from .forms import RegisterStudentForm

# Create your views here.
class ViewStudents(ListView):
    model = Students
    template_name = "view-students.html"
    context_object_name = "tasks_records"
    
class CreateTask(CreateView):
    model = Students
    form_class = CreateTaskForm
    template_name = "create-task.html"
    success_url = reverse_lazy('TaskList')

class UpdateTask(UpdateView):
    model = Students
    form_class = CreateTaskForm
    template_name = "update-task.html"
    success_url = reverse_lazy('TaskList')

class DetailViewTask(DetailView):
    model = Students
    template_name = "view-task-details.html"
    context_object_name = "task"

def register_student(request):
    if request.method == "GET":
        return render(request, "register-student.html")
    elif request.method == "POST":
        firstname = request.POST.get("firstname")
        phoneno = request.POST.get("phonenovalue")
        emailvalue = request.POST.get("emailvalue")

        student_object = Students(name=firstname, email=emailvalue, phoneno=phoneno)
        student_object.save()
        return HttpResponse("Student Registered Successfully.")
    
def show_students_records(request):
    if request.method == "GET":
        student_records = Students.objects.all()
        return render(request, "show-students-records.html", {"student_records":student_records})
    
def edit_student_record(request, student_id):
    if request.method == "GET":
        student_record = Students.objects.get(id = student_id)
        return render(request, "edit-student-record.html", {"student_record":student_record})
    elif request.method == "POST":
        studentID = request.POST.get("id")
        student_record = Students.objects.get(id = studentID)
        student_record.name = request.POST.get("firstname")
        student_record.phoneno = request.POST.get("phonenovalue")
        student_record.email = request.POST.get("emailvalue")
        student_record.save()
        return render(request, "show-updated-record.html", {"student_record":student_record})
    
def delete_student_record(request, student_id):
    if request.method == "GET":
        student_record = Students.objects.get(id = student_id)
        student_record.delete()
        return HttpResponse("Student Record Deleted Successfully.")