from django.urls import path
from cbv.views import (
    SchoolListView,
    SchoolDetailView,
    StudentListView,
    SchoolCreateView,
    SchoolUpdateView,
SchoolDeleteView)

app_name = 'cbv'

urlpatterns = [
    path('', SchoolListView.as_view(), name='list'),
    path('students/', StudentListView.as_view(), name='students'),
    path('create/', SchoolCreateView.as_view(), name='create'),
    path('<pk>/update', SchoolUpdateView.as_view(), name='update'),
    path('<pk>/delete', SchoolDeleteView.as_view(), name='delete'),
    path('<pk>/', SchoolDetailView.as_view(), name='detail'),
]
