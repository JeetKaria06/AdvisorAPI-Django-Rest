from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/advisor', views.add_advisor, name='add-advisor'),
    path('user/register', views.register_user, name='register-user'),
    path('user/login', views.login_user, name='login-user'),
    path('user/<id>/advisor', views.getlist_advisor, name='list-advisor'),
    path('user/<user_id>/advisor/booking', views.get_calls, name='get-calls'),
    path('user/<user_id>/advisor/<advisor_id>', views.book_advisor, name='book-advisor'),
]