
from.models import *
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "home.html")


@csrf_protect
def add_district(request):
    if request.method == 'POST':
        district_name = request.POST.get('district_name')
        upozilla_names = request.POST.getlist('upozilla_names[]')

        # Check if the district name already exists
        if District.objects.filter(name=district_name).exists():
            print("District with this name already exists")
            return render(request, 'add_district.html')  

        if district_name:
            district = District.objects.create(name=district_name)

            for upozilla_name in upozilla_names:
                if upozilla_name:
                    Upozilla.objects.create(name=upozilla_name, district=district)

            return redirect(home)  # Redirect to a success page after submission

    return render(request, 'add_district.html')

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import District, Upozilla, UnionWard
from django.contrib import messages

@csrf_protect
def add_union_ward(request):
    if request.method == 'POST':
        district_id = request.POST.get('district_id')
        upozilla_id = request.POST.get('upozilla_id')
        union_names = request.POST.getlist('union_names[]')

        if district_id and upozilla_id:
            for union_name in union_names:
                if union_name:
                    UnionWard.objects.create(
                        name=union_name,
                        district_id=district_id,
                        upozilla_id=upozilla_id
                    )
            return redirect(home)  
        
    districts = District.objects.all()
    return render(request, 'add_union_ward.html', {'districts': districts})

def get_upozillas(request, district_id):
    upozillas = Upozilla.objects.filter(district_id=district_id)
    data = {'upozillas': [{'id': u.id, 'name': u.name} for u in upozillas]}
    return JsonResponse(data)
