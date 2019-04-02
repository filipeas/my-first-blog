from django.urls import path
from . import views

# atribuindo views as urls
urlpatterns = [
	path('', views.post_list, name='post_list'),
]