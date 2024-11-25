from django.urls import path
from homepage.views import ProdutoSaldodoView

urlpatterns = [
    path('', ProdutoSaldodoView.as_view(), name='homepage'),
]
