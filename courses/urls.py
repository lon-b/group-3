from django.urls import path
from .views import CourseList, CourseDetail,PriceFilteredCourseList

urlpatterns = [
    path('api/items/', CourseList.as_view(), name='course-list'),
    path('api/items/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('api/items/filtered/', PriceFilteredCourseList.as_view(), name='price-filtered-course-list'),

]
