from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveIndexView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post

# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    # 객체 리스트에 대한 컨텍스트 변수명을 posts 로 지정한다.
    context_object_name = 'posts'
    # 한 페이지에 보여주는 객체 리스트의 숫자는 2이다.페이지 기능이 활성화되면 객체 리스트 하단에 페이지를 이동할 수 있는 버튼을 만들 수 있다.
    paginate_by = 2

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    # True면, 객체의 리스틀 만들어서 템플릿에 넘겨준다. False면, 디폴트.
    make_object_list = True

class PostMAV(MonthArchiveIndexView):
    model = Post
    date_field = 'modify_dt'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'