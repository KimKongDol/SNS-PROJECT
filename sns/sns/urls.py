"""sns URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="main"), #아무것도 입력하지 않았을 때 main앱의 view에서 index함수 호출
    path('place/',views.place , name="place"),
    path('<str:id>', views.message, name="message"),
    path('messageList/', views.messageList, name="messageList"),
    path('writeM/', views.writeM, name="writeM"),
    path('create/',views.create, name="create"),
    path('edit/<str:id>', views.edit , name="edit"),
    path('update/<str:id>', views.update, name="update"),
    path('delete/<str:id>', views.delete, name="delete"),
    path('accounts/',include('allauth.urls')),
    path('users/',include('users.urls')),
    path('<str:blog_id>/create_comment', views.create_comment, name="create_comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
