from django.views.generic import TemplateView

#TemplateView
# generic 뷰를 상속받아 사용한다.
class HomeView(TemplateView):
    # template 이름은 'home.html'으로 한다.
    template_name = 'home.html'