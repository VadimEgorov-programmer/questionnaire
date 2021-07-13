from django.urls import path

from .views import *

app_name = 'polls'
urlpatterns = [
    path('login/', login, name='login'),
    path('pollsApp/create/', poll_create, name='poll_create'),
    path('pollsApp/update/<int:poll_id>/', poll_update,
         name='poll_update'),
    path('pollsApp/view/', poll_view, name='poll_view'),
    path('pollsApp/view/active/', active_poll_view,
         name='active_poll_view'),
    path('question/create/', question_create, name='question_create'),
    path('question/update/<int:question_id>/', question_update,
         name='question_update'),
    path('choice/create/', choice_create, name='choice_create'),
    path('choice/update/<int:choice_id>/', choice_update,
         name='choice_update'),
    path('answer/create/', answer_create, name='answer_create'),
    path('answer/view/<int:user_id>/', answer_view,
         name='answer_view'),
    path('answer/update/<int:answer_id>/', answer_update,
         name='answer_update')
]
