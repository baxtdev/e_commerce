from django.contrib import admin
from django.urls import path,include, re_path
from rest_framework.routers import DefaultRouter
from product.yasg import urlpatterns as doc_url
from .views import RegisterAPI
from django.urls import path
from . views import*
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path

# from ecommerce import product


router = DefaultRouter()

router.register('category', CategoryModelViewSet)
router.register('products',ProducteModelViewSet)
# router.register('atributes',AtributeModelViewSet)
# router.register('photos', PhotoModelViewSet)
router.register('orderitems', OrderItemModelViewSet)
router.register('orders', OrderModelViewSet)

urlpatterns = [
    path('',include(router.urls)),#список api адресов
    path('', include('djoser.urls')),#добавление пользователей и список пользователей
    path('auth/register/', RegisterAPI.as_view(), name='register'),
    path('auth/login/', LoginAPI.as_view(), name='login'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('auth/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    ]

shoppingpatterns = [
    path ('shoping/<int:id>/:atribute/', detail_product, name='product-values'),
    path('shoping_cat/product/<int:id>',detail_category, name='detail-cat' ),
    path('shopping/all/', all_products, name='all-products'),
    path('home/',index,name='home'),
    path('shoping_zakazy/', zakaz, name='zakazy')
    
]

#swagger urls
urlpatterns+=doc_url

#shopping list
urlpatterns+=shoppingpatterns

