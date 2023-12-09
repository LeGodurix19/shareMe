from django.contrib import admin
from django.urls import path
from .views import index, login_view, desc_view, links_view, general_view, create_view, logout_view, delete_link
from dotenv import load_dotenv
import os

load_dotenv()
app_name = os.getenv('PROJECT_NAME')

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('new/', create_view.as_view(), name='create_user'),
    path('logout/', logout_view.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/login/', login_view.as_view(), name='login'),
    path('desc/', desc_view.as_view(), name='desc'),
    path('links/', links_view.as_view(), name='links'),
    path('delete_link/<str:name>', delete_link.as_view(), name='delete_link'),
    path('<slug:slug>/', general_view.as_view(), name='view'),
]
