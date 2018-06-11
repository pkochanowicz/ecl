from django.conf.urls import url
from api.views import LecturerCreationView, MainSiteView, LecturersListView, LecturerDeleteView
from english_classes_online import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', MainSiteView.as_view(), name='show_lecturers'),
    url('^edit/', LecturersListView.as_view(), name='edit'),
    url('^add_lecturer/', LecturerCreationView.as_view(), name='add_lecturer'),
    url(r'^delete_lecturer/(?P<lecturer_id>(\d)+)/', LecturerDeleteView.as_view(), name='delete_lecturer'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
