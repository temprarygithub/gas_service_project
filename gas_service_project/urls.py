"""gas_service_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('service/', include('gas_service_app.urls')),
# ]

#---------------------------------------------------------------------------

from django.urls import path
from gas_app import views

urlpatterns = [
    path('gas/', views.gas , name="gas"),
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_status, name='track_status'),
    path('add_support/', views.add_support, name='add_support'),
    path('manage_support_reps/', views.manage_support_reps, name='manage_support_reps'),
]
