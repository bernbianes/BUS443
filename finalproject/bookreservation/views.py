from django.shortcuts import render
from django.http import HttpResponse
from bookreservation.models import Studentdetails, Bookdetails, Bookreservation 
from django.db import connection
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

@login_required
def home(request): 
    return render(request,"bookreservation/dashboard.html")


# Create your views here.
@login_required
def student_info(request):
    data = Studentdetails.objects.all().order_by("studentid")
    paginator = Paginator(data, 10)
    page = request.GET.get("page")
    page_data = paginator.get_page(page)
    context ={"studentdata": page_data}
    return render(request, "bookreservation/studentinfo.html", context)

@login_required
def book_info(request):
    data = Bookdetails.objects.all().order_by("-numberoftimescheckedout")
    paginator = Paginator(data, 10)
    page = request.GET.get("page")
    page_data = paginator.get_page(page)
    context ={"bookdata": page_data}
    return render(request, "bookreservation/bookinfo.html", context)

@login_required
def book_reservation(request):
    student_data = Studentdetails.objects.all()
    # Only includes books that are not checked out 
    book_data = Bookdetails.objects.filter(currentlycheckedout="No")
    reservation_data = Bookreservation.objects.all()

    context = {"student": student_data, "book": book_data, "reservation": reservation_data}

    return render(request,"bookreservation/reserve.html", context)

def save_reservation(request):
    if("studentid" in request.GET and "bookid" in request.GET):
        studentid = request.GET.get("studentid")
        bookid = request.GET.get("bookid")
        
        student = Studentdetails.objects.filter(studentid=studentid).first()
        book = Bookdetails.objects.filter(bookid=bookid).first()

        # Prevents Students from reserving more than 4 books 
        student_reservation_count = Bookreservation.objects.filter(studentid=studentid).count()
        if student_reservation_count >=4:
            return HttpResponse("toomany")
        
        # Prevents two students from reserving the same book 
        book_reserved = Bookreservation.objects.filter(bookid=bookid).exists()
        if book_reserved:
            return HttpResponse("taken")
        
        # Confirms reservation and adds it to the table
        reservation = Bookreservation(
            studentid = studentid, 
            studentname=f"{student.firstname} {student.lastname}", 
            bookid=bookid, 
            bookname = book.bookname)
        # Saves the reservation into the book reservation table
        reservation.save()

        book.currentlycheckedout = "Yes"
        book.numberoftimescheckedout += 1
        book.save()

        return HttpResponse("success")
    return HttpResponse("error")

@login_required
def dashboard(request):
    totalstudents = Studentdetails.objects.count()

    with connection.cursor() as cursor: 
        cursor.execute("SELECT AVG(gpa) FROM bookreservation_studentdetails")
        result = cursor.fetchone()

    averagegpa = result[0]

    freshmancount = Studentdetails.objects.filter(year="Freshman").count()
    sophomorecount = Studentdetails.objects.filter(year="Sophomore").count()
    juniorcount = Studentdetails.objects.filter(year="Junior").count()
    seniorcount = Studentdetails.objects.filter(year="Senior").count()

    context = {"total": totalstudents, "average": round(averagegpa, 2), "freshman": freshmancount, "sophomore": sophomorecount, "junior": juniorcount, "senior": seniorcount}
    
    return render(request, "bookreservation/dashboard.html", context)


