from django.urls import path, include
from transaction.views import DepositePageView,WithdrawPageView
urlpatterns = [
    path('deposite/',DepositePageView.as_view(),name='deposit_money'),
    path('withdraw/',WithdrawPageView.as_view(),name='withdraw_money'),
]
