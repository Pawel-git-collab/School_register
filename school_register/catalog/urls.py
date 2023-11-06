from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.StudentListView.as_view(), name='student'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('student/create/', views.StudentCreate.as_view(), name='student_create'),
    path('student/update/<int:pk>', views.StudentUpdate.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', views.StudentDelete.as_view(), name='student_delete'),

]
