from django.urls import path
from django.contrib import admin
from paymentProcessor import views as core_views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('createPayment/', core_views.OrderAPIView.as_view()),  # New endpoint
    path('getPaymentStatus/', core_views.GetPaymentStatusView.as_view()),  # New endpoint
]
