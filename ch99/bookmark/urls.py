from django.urls import path
# URLconf 에서 뷰를 호출하기 때문에 뷰 모듈의 관련 클래스를 임포트한다.
from bookmark.views import BookmarkLV, BookmarkDV

# 애플리케이션 이름공간을 지정한다.
app_name = 'bookmark'


urlpatterns = [
    # /bookmark/ 로 요청을 처리한 뷰 클래스를 지정한다.
    path('', BookmarkLV.as_view(), name='index'),
    # /bookmark/숫자/ 로 요청을 처리한 뷰 클래스를 지정한다.
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
]