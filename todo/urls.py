
from rest_framework.routers import DefaultRouter
from todo.views import TodoViewSet
from django.urls import path,include

router = DefaultRouter()
router.register(r'todo', TodoViewSet, basename='todo')
urlpatterns = [
    path('api/', include(router.urls)),

]
