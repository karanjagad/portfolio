
# from django.urls import path
# from django.urls import include
# from .views import ContactView

# urlpatterns = [
#     path('home', ContactView.as_view()),
# ]
from django.urls import path
from .views import ContactView

urlpatterns = [
    path('home/', ContactView, name='home'),
]