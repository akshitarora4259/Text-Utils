"""textutils URL Configuration

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

# django starts executing by going to urls.py 
# there it sees that homepage is renderred by views.py
# and whatever is returned by views.py it is rendered on the website

from django.contrib import admin
from django.urls import path
from . import views

#code for video 6
# urlpatterns = [

#     # first argument is the end-point
#     # function to be run when endpoint is specified
#     # name of the path

#     path('admin/', admin.site.urls),
#     path('',views.index,name='index'),
#     path('about',views.about,name='about')
# ]


# code for video 7
urlpatterns = [

    # first argument is the end-point
    # function to be run when endpoint is specified
    # name of the path

    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('analyze', views.analyze, name='analyze'),
]