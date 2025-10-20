from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.hashers import check_password
from . import models, forms



class RegisterView(generic.FormView):
    template_name = 'users/register.html'
    form_class = forms.WorkerProfileForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class AuthLoginView(generic.FormView):
    template_name = 'users/login.html'
    form_class = forms.LoginForm
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        workers = models.WorkerProfile.objects.filter(username=username)

        if not workers.exists():
            return self.form_invalid(form)

        worker = workers.first()
        if check_password(password, worker.password):
            self.request.session['worker_id'] = worker.id
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form, error='Неверное имя пользователя или пароль'))



class AuthLogoutView(generic.View):
    def get(self, request, *args, **kwargs):
        request.session.flush()
        return redirect('users:login')



class ProfileView(generic.TemplateView):
    template_name = 'users/profile.html'

    def dispatch(self, request, *args, **kwargs):
        worker_id = request.session.get('worker_id')
        if not worker_id:
            return redirect('users:login')

        try:
            self.worker = models.WorkerProfile.objects.get(id=worker_id)
        except models.WorkerProfile.DoesNotExist:
            request.session.flush()
            return redirect('users:login')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['worker'] = self.worker
        return context
