from django.urls import path

from job import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.Logout, name='logout'),

    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('view_applicants/', views.view_applicants, name='view_applicants'),
    path('view_recruiters/', views.view_recruiters, name='view_recruiters'),
    path('delete_applicant/<str:pk>/', views.delete_applicant, name='delete_applicant'),
    path('delete_recruiter/<str:pk>/', views.delete_recruiter, name='delete_recruiter'),
    path('recruiter_pending/', views.recruiter_pending, name='recruiter_pending'),
    path('recruiter_accepted/', views.recruiter_accepted, name='recruiter_accepted'),
    path('recruiter_rejected/', views.recruiter_rejected, name='recruiter_rejected'),
    path('change_status/<str:pk>/', views.change_status, name='change_status'),
    path('admin_change_password/', views.admin_change_password, name='admin_change_password'),

    path('applicant_home/', views.applicant_home, name='applicant_home'),
    path('applicant_login/', views.applicant_login, name='applicant_login'),
    path('applicant_signup/', views.applicant_signup, name='applicant_signup'),
    path('applicant_change_password/', views.applicant_change_password, name='applicant_change_password'),

    path('recruiter_home/', views.recruiter_home, name='recruiter_home'),
    path('recruiter_login/', views.recruiter_login, name='recruiter_login'),
    path('recruiter_signup/', views.recruiter_signup, name='recruiter_signup'),
    path('recruiter_change_password/', views.recruiter_change_password, name='recruiter_change_password'),
    path('add_job/', views.add_job, name='add_job'),
    path('edit_job/<str:pk>/', views.edit_job, name='edit_job'),
    path('delete_job/<str:pk>/', views.delete_job, name='delete_job'),
    path('job_list/', views.job_list, name='job_list'),
]
