from django.urls import path
from .views import HomepageView, chart_select_view


app_name = 'products'

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('performance/', chart_select_view, name='dashboard'),
]
