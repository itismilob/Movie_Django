"""
URL configuration for Movie project.

The `urlpatterns` list routes URLs to pybo. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function pybo
    1. Add an import:  from my_app import pybo
    2. Add a URL to urlpatterns:  path('', pybo.home, name='home')
Class-based pybo
    1. Add an import:  from other_app.pybo import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pybo import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
