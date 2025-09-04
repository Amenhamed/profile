from django.urls import path # type: ignore
from . import views
urlpatterns = [
    path('',views.home , name='home'),
    path('update/<int:id>',views.update , name='update'),
    path('delate/<int:id>',views.delate , name='delate'),
]
