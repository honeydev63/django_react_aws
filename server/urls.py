from django.contrib import admin
from django.urls import path,include
from spotifysearch.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
        # path('', LoginView.as_view()),
    path('api/', include('spotifysearch.urls')),
]
