# # lms_app/urls.py

# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('register/', views.register, name='register'),
#     path('otp-verify/', views.otp_verify, name='otp_verify'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     path('profile/', views.profile, name='profile'),
#     path('update-profile/', views.update_profile, name='update_profile'),
#     path('change-password/', views.change_password, name='change_password'),
#     path('delete-account/', views.delete_account, name='delete_account'),

#     # Password reset URLs
#     path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
#     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]



from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('otp-verify/', views.otp_verify, name='otp_verify'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('delete-account/', views.delete_account, name='delete_account'),

    # Add the dashboard URL
    path('dashboard/', views.dashboard, name='dashboard'),

    # Password reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
