from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps
from dateutil.relativedelta import relativedelta
from datetime import datetime

Prisoner = apps.get_model("main", "Prisoner")
FIR = apps.get_model("main", "FIR")
Crime = apps.get_model("main", "Crime")
Court = apps.get_model("main", "Court")
Visitor = apps.get_model("main", "Visitor")
Lawyer = apps.get_model("main", "Lawyer")
# Create your views here.

def index(request):
    return render(request, "index.html")


def update_or_add(request):
    return render(request, "main/update_or_add.html")


def prisoner_data(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        address = request.POST["address"]
        mobile = request.POST["mobile"]
        email = request.POST["email"]
        join_date = request.POST["join_date"]
        exit_date = request.POST["exit_date"]
        duration = get_duration(start_date=join_date, end_date=exit_date)
        ward = request.POST["ward"]

        Prisoner.objects.create(
            first_name=fname,
            last_name=lname,
            address=address,
            mobile_numbers=mobile,
            email=email,
            join_date=join_date,
            exit_date=exit_date,
            duration=duration,
            ward=ward
        )

        return redirect('/')
    else:
        return render(request, "main/add_prisoner.html")

def get_duration(start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    delta = relativedelta(end_date, start_date)
    years = delta.years
    months = delta.months
    weeks = delta.days // 7
    days = delta.days % 7
    
    return f"{years}-{months}-{weeks}-{days}"

    
def fir_data(request):
    if request.method == "POST":
        #variables -> html name
        fir_number = request.POST["fir_number"]
        description = request.POST["description"]
        date_of_registration = request.POST["date_of_registration"]
        ps_id_no = request.POST["ps_id_no"]

    FIR.objects.create(
        fir_number=fir_number,
        description=description,
        date_of_registration=date_of_registration,
        ps_id_no=ps_id_no
    )

    return redirect('/')

def crime_data(request):
    if request.method == "POST":
        crime_type = request.POST["crime_type"]
        crime_location = request.POST["crime_location"]
        crime_date = request.POST["crime_date"]
        fir = request.POST["fir"]

    Crime.objects.create(
        crime_type=crime_type,
        crime_location=crime_location,
        crime_date=crime_date,
        fir=fir
    )

def court_data(request):
    if request.method == "POST":
        court_name = request.POST["court_name"]
        court_location = request.POST["court_location"]
    
    Court.objects.create(
        court_name=court_name,
        court_location=court_location
    )
    
def visitor_data(request):
    if request.method == "POST":
        visitor_name = request.POST["visitor_name"]
        relationship = request.POST["relationship"]
        mobile = request.POST["mobile"]
        address = request.POST["address"]

    Visitor.objects.create(
        visitor_name=visitor_name,
        relationship=relationship,
        mobile=mobile,
        address=address
    )


def Lawyer_data(request):
    if request.method == "POST":
        name = request.POST["name"]
        bar_no = request.POST["bar_no"]

    Lawyer.objects.create(
        name=name,
        bar_no=bar_no
    )

def generic(request):
    return render(request, "base.html")

def register(request):
    return render(request, "register.html")