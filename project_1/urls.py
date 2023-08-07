"""
URL configuration for project_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home.views import *
from vegeee.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home ),
    path('login/', login_page ),
    path('register/', register_page ),
    path('render/', templateRend ),
    path('render-recipe/', recipeform ),
    path('render-table/', recipeTable ),
    path('delete-recipe/<id>/', deleteRecipe ),
    path('update-recipe/<id>/', updateRecipe ),


    path('admin/', admin.site.urls),
]


if settings.DEBUG:
     urlpatterns += static( settings.MEDIA_URL, 
                                    document_root= settings.MEDIA_ROOT)
     

urlpatterns += staticfiles_urlpatterns()