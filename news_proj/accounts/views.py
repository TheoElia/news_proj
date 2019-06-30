from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.views.generic import ListView
from .forms import CustomUserCreationForm
from django.contrib import messages

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

    def post(self,request):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            # Collecting what user entered
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            # Validating what user entered with form_valid function
            user = self.form_valid(form)
            # Saving the user to database
            user.save()
            # msg_plain = render_to_string('welcome_email.txt', {'username':username,'email_token':email_token,
            # 'verification_link':"https://www.pywe.org/accounts/email_verification/{}".format(email_token),
            # 'home_link':"https://www.pywe.org/",'docs_link':"https://documenter.getpostman.com/view/5710655/RzfmE6pN"})

            # msg_html = render_to_string('welcome_email.html', {'username':username, 'email_token':email_token,
            # 'verification_link':"https://www.pywe.org/accounts/email_verification/{}".format(email_token),
            # 'home_link':"https://www.pywe.org/",'docs_link':"https://documenter.getpostman.com/view/5710655/RzfmE6pN"})
            # subject = "Welcome {}".format(username)
            # send_mail(
            # subject,
            # msg_plain,
            # 'pythonwithellie@gmail.com',
            # [email],
            # html_message=msg_html,
            # fail_silently=False,)
            messages.success(request, "Hello there, you have been registered.")
            return redirect('signup')
        else:
            messages.error(request, "There was an error processing your form")
            return redirect('signup')

        args = {'form': form}
        return render(request, self.template_name, args)

    def form_valid(self, form):
        user = form.save(commit=False)
        return user
