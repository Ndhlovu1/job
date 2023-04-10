from django.urls import path, reverse_lazy, include
from . import views
from django.contrib.auth import views as auth_views

#update_session_auth_hash
#123@Qwerty!
urlpatterns = [
    #path('login/',views.User_Login, name = 'login'),
    path('', 
         views.dashboard, 
         name='dashboard'),

     #Password Changes
    path('password_change/', 
         auth_views.PasswordChangeView.as_view(
            template_name='registration/password_change_form.html',
         ),
         name='password_change'
           ),

    path('password_change/done/', 
         auth_views.PasswordChangeDoneView.as_view(), 
         name="password_change_done"),

    path('login/', 
         auth_views.LoginView.as_view(), 
         name='login'),
    
    path('logout/', 
         auth_views.LogoutView.as_view(), 
         name='logout'),

    #RESETTING THE PASSWORD - CREATE A CORRESPONDING TEMPLATE FILE
     path('password_reset/',
          auth_views.PasswordResetView.as_view(),
          name='password_reset'
         ),

     path('password_reset_done',
          auth_views.PasswordResetDoneView.as_view(),
          name='password_reset_done'
         ),

     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

     path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'
         ),

     #User Registration
     path('register/', views.register, name="register"),

     #User Profile Edit
     path('edit-profile/', views.edit_user_profile, name="profileEdit"),

]


"""
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']

"""
