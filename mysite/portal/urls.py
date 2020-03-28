from django.urls import path
from . import views
from .context_processors import prof_reviews
from .views import *

urlpatterns = [
    path('', ProfReviewListView.as_view(), name='portal_home'),
    path('', prof_reviews, name='search'),
    path('user/<str:username>', UserProfReviewListView.as_view(), name='user_reviews'),
    path('prof-review/<int:pk>/', ProfReviewDetailView.as_view(), name='prof_review_detail'),
    path('prof-review/new/', ProfReviewCreateView.as_view(), name='prof_review_create'),
    path('prof-review/<int:pk>/update/', ProfReviewUpdateView.as_view(), name='prof_review_update'),
    path('prof-review/<int:pk>/delete/', ProfReviewDeleteView.as_view(), name='prof_review_delete'),
    path('course-review/<int:pk>/', CourseReviewDetailView.as_view(), name='course_review_detail'),
    path('course-review/new/', CourseReviewCreateView.as_view(), name='course_review_create'),
    path('course-review/<int:pk>/update/', CourseReviewUpdateView.as_view(), name='course_review_update'),
    path('course-review/<int:pk>/delete/', CourseReviewDeleteView.as_view(), name='course_review_delete'),
    path('about/', views.about, name='portal_about')
]