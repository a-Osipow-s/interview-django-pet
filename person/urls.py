"""Person urls"""

from django.urls import path 

from person.views import IndexView, PersonDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='person_list'),
    path('<int:pk>/', PersonDetailView.as_view(), name='person_detail'),
]