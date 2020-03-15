from django.contrib import admin
from django.urls import path
from adoptions import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('adoptions/<int:id>/', views.pet_detail, name='pet_detail')
]
urlpatterns += staticfiles_urlpatterns()
