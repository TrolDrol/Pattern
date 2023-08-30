from django.urls import path
from .views import index, top_sellers, advertisment_post, advertisment_datail

urlpatterns = [
    path('', index, name='main-page'),
    path('top_sellers', top_sellers, name='top_sellers'),
    path('advertisment-post/', advertisment_post, name='adv-post'),
    path('advertisment/<int:pk>', advertisment_datail, name='adv-datail'),
]