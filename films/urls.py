from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework import routers
from filmsweb.views import UserView, FilmView

router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'films', FilmView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('filmsweb/', include('filmsweb.urls')),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


