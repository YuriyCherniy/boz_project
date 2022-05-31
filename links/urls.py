from django.urls import path

from links.views import LinkListCreate

urlpatterns = [
    path('', LinkListCreate.as_view())
]