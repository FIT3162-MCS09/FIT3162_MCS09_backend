from django.urls import path, include
from .views.file_view import FileUploadView, UserFilesView
from .views.auth_view import (
    PatientSignUpView, 
    DoctorSignUpView, 
    SignInView,
    LogoutView,
    SessionListView
)
from .views.health_view import HealthView
from .views.protected_view import ProfileView  # Assuming you implemented this

# Group URL patterns by feature/functionality
urlpatterns = [
    # Authentication endpoints
    path('auth/', include([
        path('signup/patient/', PatientSignUpView.as_view(), name='signup_patient'),
        path('signup/doctor/', DoctorSignUpView.as_view(), name='signup_doctor'),
        path('signin/', SignInView.as_view(), name='signin'),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('sessions/', SessionListView.as_view(), name='sessions'),
        path('profile/', ProfileView.as_view(), name='profile'),
    ])),
    
    # File management endpoints
    path('files/', include([
        path('upload/', FileUploadView.as_view(), name='file-upload'),
        path('view/', UserFilesView.as_view(), name='user-files'),
    ])),
    
    # System endpoints
    path('system/', include([
        path('health/', HealthView.as_view(), name='health'),
    ])),
]