"""english_classes_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from api.views import LecturerCreationView, MainSiteView, LecturersListView, LecturerDeleteView
from english_classes_online import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url('', include('api.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainSiteView.as_view(), name='show_lecturers'),
    url('^edit/', LecturersListView.as_view(), name='edit'),
    url('^add_lecturer/', LecturerCreationView.as_view(), name='add_lecturer'),
    url(r'^delete_lecturer/(?P<lecturer_id>(\d)+)/', LecturerDeleteView.as_view(), name='delete_lecturer'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)