"""aidanmcdonagh URL Configuration

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
from .views import ListTodoView, AddTodoView, UpdateTodoView, DeleteTodoView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', ListTodoView.as_view()),
    path('add/', AddTodoView.as_view(), name='todo-add'),
    path('<int:pk>/', UpdateTodoView.as_view(), name='todo-update'),
    path('<int:pk>/delete/', DeleteTodoView.as_view(), name='todo-delete'),
    path('admin/', admin.site.urls),
]
