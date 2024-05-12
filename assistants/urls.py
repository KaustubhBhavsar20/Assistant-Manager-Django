from django.urls import path
from assistants import views

urlpatterns = [
    path('assistant/', views.create_assistant),
    path('assistant/<int:assistant_id>/', views.assistant_detail),
]
