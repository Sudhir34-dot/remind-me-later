from django.urls import path
from .views import ReminderCreateView, ReminderListView

urlpatterns = [
    path('create/', ReminderCreateView.as_view(), name='create-reminder'),
    path('', ReminderListView.as_view()),  
]
