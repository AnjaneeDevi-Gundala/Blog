from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm

app_name='myapp'
urlpatterns=[
    path('register/',register,name='register'),
    path('home/',home,name='home'),
    path('',loginview,name='login'),
    path('login/',loginview,name='login'),
    path('logout/',logoutview,name='logout'),
    path('create/',create,name='create'),
    path('retrieve/',retrieve,name='retrieve'),
    path('update<int:id>/',update,name='update'),
    path('delete<int:id>/',delete,name='delete'),
    # path('password-reset/', auth_views.PasswordResetView.as_view(
    #     template_name='registration/password_reset_form.html',
    #     email_template_name='registration/password_reset_email.html',
    #     success_url='/password-reset/done/',
    #     form_class=CustomPasswordResetForm
    # ), name='password_reset'),

    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),

    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    #     template_name='registration/password_reset_confirm.html',success_url='/reset/done/'
    # ), name='password_reset_confirm'),
    
    path(
        'reset/<uidb64>/<token>/',
        CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
]
