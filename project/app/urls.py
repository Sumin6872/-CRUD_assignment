from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',views.home, name="home"),
  path('detail/<int:post_id>',views.detail, name="detail"),
  path('create/',views.create, name="create"),
  path('detail/<int:post_id>/update/',views.update, name="update"),
  path('detail/<int:post_id>/delete/',views.delete, name="delete"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)