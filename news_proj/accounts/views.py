from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import ListView
from .forms import CustomUserCreationForm

# Create your views here.
def index(request):
    template_name = "accounts/index.html"
    return render(request,template_name)

class CreateUserView(ListView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'

    def get(self, request):
        form = self.form_class
        args = {'form': form,'title':'Register'}
        return render(request,self.template_name,args)

    # def post(self,request):
    #     form = self.form_class(request.POST,request.FILES)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password1']
    #         email = form.cleaned_data['email']
    #         user = self.form_valid(form)
    #         msg_plain = render_to_string('welcome_email.txt', {'username':username,'email_token':email_token,
    #         'verification_link':"https://www.pywe.org/accounts/email_verification/{}".format(email_token),
    #         'home_link':"https://www.pywe.org/",'docs_link':"https://documenter.getpostman.com/view/5710655/RzfmE6pN"})

    #         msg_html = render_to_string('welcome_email.html', {'username':username, 'email_token':email_token,
    #         'verification_link':"https://www.pywe.org/accounts/email_verification/{}".format(email_token),
    #         'home_link':"https://www.pywe.org/",'docs_link':"https://documenter.getpostman.com/view/5710655/RzfmE6pN"})
    #         subject = "Welcome {}".format(username)
    #         send_mail(
    #         subject,
    #         msg_plain,
    #         'pythonwithellie@gmail.com',
    #         [email],
    #         html_message=msg_html,
    #         fail_silently=False,)
    #         messages.success(request, "We have sent you an email, check to verify.")
    #         return redirect('signup')

    #     args = {'form': form}
    #     return render(request, self.template_name, args)
