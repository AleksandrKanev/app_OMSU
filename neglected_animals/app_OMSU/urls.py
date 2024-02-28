from django.urls import path
from . import views
from django.contrib.auth import views as vi

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', vi.LoginView.as_view(), name='login'),
    path('logout/', vi.LogoutView.as_view(next_page=''), name='logout'),
    path('reports/', views.get_reports, name='reports'),
    path('get_report/<int:report_id>', views.get_report, name='get_report'),
    path('applications/', views.get_applications, name='applications'),
    path('applications/<int:application_id>', views.get_application, name='get_application'),
    path('card_animals/', views.get_card_animals, name='card_animals'),
    path('card_animals/<int:animal_id>', views.get_animal, name='get_animal'),
]
