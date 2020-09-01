from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

#TemplateView
# generic 뷰를 상속받아 사용한다.
class HomeView(TemplateView):
    # template 이름은 'home.html'으로 한다.
    template_name = 'home.html'

#User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'