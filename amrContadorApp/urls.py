from django.urls import path
from .views import profile, adicionarDatosAMR, adicionarDatosMetroContador, detail
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/addMetroContador',
         adicionarDatosMetroContador, name='datosMetro'),
    path('accounts/profile/addDatos', adicionarDatosAMR, name='datosAmr'),
    path('accounts/profile/<int:amrId>/', detail, name='detail'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
