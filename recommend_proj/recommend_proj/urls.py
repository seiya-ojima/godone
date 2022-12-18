
from django.contrib import admin
from django.urls import path
from recommend_app.views import frontpage, evaluationpage, comparepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", frontpage),
    path('evaluation/', evaluationpage, name = "evaluation"),
    path('evaluation/compare/', comparepage, name = "compare")
]