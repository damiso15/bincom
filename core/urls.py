"""core URL Configuration

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
from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('polling-unit-list', views.PollingUnitListView.as_view(), name='polling_unit_list'),
    path('polling-unit-result/<int:pk>', views.polling_unit_detail_view, name='polling_unit_result'),
    path('lga-list', views.LGAListView.as_view(), name='lga_list'),
    path('lga-polling-result/<int:pk>', views.lga_detail_view, name='lga_polling_result'),

]
