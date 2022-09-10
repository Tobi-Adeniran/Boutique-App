from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from shop.views import (
    index,
     shop, 
     detail, 
     CheckoutView, 
     add_to_cart,
     remove_from_cart,
     remove_single_item_from_cart,
     OrderSummaryView,
     initiate_payment,
     verify_payment,
     RequestRefundView,
     AddCouponView,
     
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('shop', shop, name='shop'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('detail/<slug>/', detail, name='product-detail'),
    path('initiate-payment/', initiate_payment, name = 'initiate-payment'),
    path('<str:ref>/', verify_payment, name = 'verify-payment'),
    path('accounts/', include('allauth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
