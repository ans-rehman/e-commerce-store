from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('login/', views.login_view, name='loginlocal'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('signup/', views.signup_view, name='signuplocal'),
    path('home/', views.index, name='home'),  # new
    path("logout/", views.logout_view, name="logout"),
    path('about/',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('shop/',views.shop, name='shop'),
    path('blogs/', views.blogs, name='blogs'),
    path('services/', views.services, name='services'),
    path('categories/', views.categories, name='categories'),
    path('terms/', views.terms ,name='terms'),
    path('privacy/',views.privacy, name='privacy'),
    path('bookings/', views.book, name='book'),
    path('orders/', views.order, name='order'),
]
