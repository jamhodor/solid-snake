from django.urls import path, include
from homepage import views

urlpatterns = [
    path('', views.home, name='home'),
    path('präsentationen', views.presentations, name='presentations'),
    path('redaktion', views.editing, name='editing'),
    path('homepages', views.homepages, name='homepages'),
    path('kontakt', views.contact, name='contact'),
    path('impressum', views.disclaimer, name='disclaimer'),

    # App URLs
    path('blog/', include('blog.urls')),
]