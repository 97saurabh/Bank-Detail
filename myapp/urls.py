from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    
    path('',
        views.SnippetList.as_view(),
        name='snippet-list'),
])
