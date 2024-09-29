from django.urls import path
from book.views import home_page_view, register_page_view, member_page_view, login_page_view, error_page_view

urlpatterns = [

    path('register/', register_page_view),
    path('member/', member_page_view),
    path('login/', login_page_view),
    path('error/', error_page_view),
    path('', home_page_view),
]
