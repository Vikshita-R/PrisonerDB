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

def add_prisoner_details(request):
    return render(request, "main/add_prisoner_details.html")

def select_prisoner(request):
    if request.method == "POST":
        name = request.POST["prisoner_name"]
        split = name.split()
        prisoner_id = None
        prisoners = Prisoner.objects.filter(first_name=split[0])
        for prisoner in prisoners:
            if f'{prisoner.first_name} {prisoner.last_name}'.lower() == name.lower():
                prisoner_id = prisoner.id

        return redirect(f"/update/prisoner/{prisoner_id}")
    else:
        return render(request, "main/select_prisoner.html")
    

def prisoner_details_boxes(request, prisoner_id):
    data = {
        "prisoner_id": prisoner_id
    }

    return render(request, "main/prisoner_details_boxes.html", data)


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


def crime_data(request, prisoner_id):
    if request.method == "POST":
        prisoner = Prisoner.objects.get(id=prisoner_id)

        crime_type = request.POST["crime_type"]
        crime_location = request.POST["crime_location"]
        crime_date = request.POST["crime_date"]
        
        fir_number = request.POST["fir_number"]
        fir_description = request.POST["fir_description"]
        fir_date = request.POST["fir_date"]
        ps_id = request.POST["ps_id"]

        fir = FIR.objects.create(
            fir_number=fir_number,
            description=fir_description,
            date_of_registration=fir_date,
            ps_id_no=ps_id
        )

        Crime.objects.create(
            prisoner=prisoner,
            crime_type=crime_type,
            crime_location=crime_location,
            crime_date=crime_date,
            fir=fir
        )

        return redirect("/")
    else:
        data = {
            "prisoner_id": prisoner_id,
        }
        return render(request, "main/add_crime.html", data)

def court_data(request, prisoner_id):
    if request.method == "POST":
        court_name = request.POST["court_name"]
        court_location = request.POST["court_location"]
        prisoner = Prisoner.objects.get(id=prisoner_id)
    
        Court.objects.create(
            court_name=court_name,
            court_location=court_location,
            prisoner=prisoner
        )

        return redirect("/")
    else:
        data = {
            "prisoner_id": prisoner_id
        }
        return render(request, "main/add_court.html", data)
    
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