from django.urls import include, path
from rest_framework import routers
from tradingsystem import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'orders', views.OrderViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('order/',views.OrderStock.as_view()),
    path('login/', views.CustomAuthToken.as_view()),
    path('userstocks/',views.ViewTotalStocks.as_view())
]