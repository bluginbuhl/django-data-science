from django.urls import path
from .views import HomepageView, chart_select_view, add_purchase_view


app_name = 'products'

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('performance/', chart_select_view, name='dashboard'),
    path('add/', add_purchase_view, name="add-record"),
]
