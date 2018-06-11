from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from rest_framework import generics
from django.core.files.storage import FileSystemStorage

from api.forms import LecturerCreationForm
from api.models import Lecturer
from api.serializers import LecturerSerializer


class LecturerListCreate(generics.ListCreateAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
# Create your views here.


class MainSiteView(View):

    def get(self, request):
        lecturers = Lecturer.objects.all()
        return render(request, "main_site.html", {"lecturers": lecturers})


class LecturerCreationView(View):
    @method_decorator(login_required)
    def get(self, request):
        lecturer_form = LecturerCreationForm
        return render(request, 'add_lecturer.html', {'lecturer_form': lecturer_form})

    @method_decorator(login_required)
    def post(self, request):
        lecturer_form = LecturerCreationForm(request.POST, request.FILES)
        if lecturer_form.is_valid():
            name = lecturer_form.cleaned_data['name']
            biography = lecturer_form.cleaned_data['biography']
            try:
                if request.FILES['picture']:
                    new_lecturer = Lecturer.objects.create(
                        name=name,
                        biography=biography,
                        picture=request.FILES['picture'])
                    new_lecturer.save()
            except KeyError:
                new_lecturer = Lecturer.objects.create(
                    name=name,
                    biography=biography)
                new_lecturer.save()
            return redirect("/edit/")
        else:
            error_message=str("Wrong data. The lecturer hasn't been created.")
            return render(request, 'add_lecturer.html', {'lecturer_form': lecturer_form,
                                                         'error_message': error_message})


class LecturersListView(View):
    @method_decorator(login_required)
    def get(self, request):
        lecturers = Lecturer.objects.all()
        return render(request, "edit_list.html", {"lecturers": lecturers})


class LecturerDeleteView(View):
    @method_decorator(login_required)
    def get(self, request, lecturer_id):
        lecturer_to_delete = Lecturer.objects.get(pk=lecturer_id)
        lecturer_to_delete.delete()
        return redirect("/edit/")
