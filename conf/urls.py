from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from feedbacks import views

app_name = 'feedback_najot_talim'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ru/', include('feedback_najot_talim.urls', namespace='feedback_najot_talim')),
]


urlpatterns += i18n_patterns(
    path('', views.home_page_view, name='home_page'),
    path('offers/', views.offers_view, name='offers'),
    path('submit-offer/', views.problem_view, name='submit-offer'),
    path('comments/', views.comment_view, name='comments'),
    path('404/', views.error_view, name='404'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
