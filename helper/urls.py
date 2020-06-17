"""helper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from helper.applicationHR.api import CustomObtainAuthToken, UserList, UserDetail, CardsCreate, EmployeesDetailCardId,registratioUser_view, EmployeesCreate,SummaryList, CardsList,EmployeesDetailView, EmployeesList, PersonnellList# UserAuthenticaation,
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/users_list/$', UserList.as_view(), name='user_list'),
    url(r'^api/users_list/(?P<phone>\d+)/$', UserDetail.as_view(), name='user_list'),

    url(r'^api/personnel/$', PersonnellList.as_view(), name='personal_list'),

    url(r'^api/cards/$', CardsList.as_view(), name='cards_list'),
    url(r'^api/cards_create/$', CardsCreate.as_view(), name='cards_create'),
#db2forIndia.sqlite3
    url(r'^api/employees/$', EmployeesList.as_view(), name='employeesList_list'),
    url(r'^api/empl_detail/(?P<pk>\d+)/$', EmployeesDetailView.as_view(), name='employees_detail'),
    url(r'^api/empl_detail2', EmployeesDetailCardId.as_view(), name='EmployeesDetailPosition'),
    path('api/list', EmployeesDetailCardId.as_view(), name="list"),
    url(r'^api/empl_create/', EmployeesCreate.as_view(), name='empl_create'),


    path('api/register/', registratioUser_view, name='register'),
    path('api/login/', CustomObtainAuthToken.as_view(), name="login"),
]
