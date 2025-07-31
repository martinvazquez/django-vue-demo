# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from cats import views

# development only
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'cats', views.CatViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    path('', include('core.urls')), 
    path('admin/', admin.site.urls),
#]

# development only
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
