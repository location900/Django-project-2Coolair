from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import FormView
from django.views.generic.base import TemplateView

from app.forms import QuoteForm, ServiceForm, JobForm
from app.models import Quote, WarrantyQuote, Job

show_promotion = '1'

class HomePageView(TemplateView):
    template_name = "app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        global show_promotion
        context.update({'show_promotion' : show_promotion})
        return context

class PurchasePageView(FormView):
    template_name = "app/purchase.html"
    form_class = QuoteForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        global show_promotion
        context.update({'show_promotion': show_promotion})
        return context
    def get_success_url(self):
        return '/purchase'

class ServicePageView(FormView):
    template_name = "app/service.html"
    form_class = ServiceForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'company': self.request.GET.get('company', )})
        global show_promotion
        context.update({'show_promotion': show_promotion})
        return context
    def get_success_url(self):
        return '/service'

class AboutPageView(TemplateView):
    template_name = "app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        global show_promotion
        context.update({'show_promotion': show_promotion})
        return context

class LoginPageView(TemplateView):
    template_name = "app/login.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request):
        user = User.objects.filter(username='admin')
        if user is None:
            user = User.objects.create_user(username='admin',
                                        email='admin@admin.com',
                                        password='adminpassword')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('admin_quote')
        return redirect('login')

class LogoutPageView(TemplateView):
    template_name = "app/login.html"
    def get(self, request, **kwargs):
        logout(request)
        return redirect('login')

class AdminQuotePageView(LoginRequiredMixin, TemplateView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = "app/admin_quote.html"
    def get_context_data(self, **kwargs):
        del_id = self.request.GET.get('del_id', )
        if del_id:
            Quote.objects.filter(id=del_id).delete()
        q = Quote.objects.all()
        context = super().get_context_data(**kwargs)
        context.update({'quotes':q})
        return context

class AdminQuoteDetailPageView(LoginRequiredMixin, FormView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = "app/admin_quote_detail.html"
    form_class = QuoteForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_initial(self):
        id = self.request.GET.get('id', )
        if id:
            q = Quote.objects.get(id=id)
            return {'id':q.id, 'name': q.name, 'email':q.email, 'type': q.type, 'remark': q.remark}

    def get_success_url(self):
        return '/admin/quote'

class AdminWarrantyQuoteDetailPageView(LoginRequiredMixin, FormView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = "app/admin_warranty_quote_detail.html"
    form_class = ServiceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_initial(self):
        id = self.request.GET.get('id', )
        if id:
            q = WarrantyQuote.objects.get(id=id)
            return {'id': q.id, 'name': q.name, 'address':q.address, 'phone': q.phone,
                    'email': q.email, 'product': q.product, 'company': q.company,
                    'serial': q.serial, 'date': q.date, 'under_warranty': q.under_warranty, 'description': q.description}

    def get_success_url(self):
        return '/admin/warranty_quote'


class AdminWarrantyQuotePageView(LoginRequiredMixin, TemplateView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = "app/admin_warranty_quote.html"

    def get_context_data(self, **kwargs):
        del_id = self.request.GET.get('del_id', )
        if del_id:
            WarrantyQuote.objects.filter(id=del_id).delete()
        q = WarrantyQuote.objects.all()
        context = super().get_context_data(**kwargs)
        context.update({'quotes': q})
        return context

class AdminJobPageView(LoginRequiredMixin, TemplateView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = "app/admin_job.html"
    def get_context_data(self, **kwargs):
        del_id = self.request.GET.get('del_id', )
        if del_id:
            Job.objects.filter(id=del_id).delete()
        jobs = Job.objects.all()
        context = super().get_context_data(**kwargs)
        context.update({'jobs':jobs})
        return context

class AdminJobDetailPageView(LoginRequiredMixin, FormView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = "app/admin_job_detail.html"
    form_class = JobForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_initial(self):
        id = self.request.GET.get('id', )
        if id:
            q = Job.objects.get(id=id)
            return {'id': q.id, 'name': q.name, 'no': q.no, 'customer_name': q.customer_name, 'address':q.address, 'date': q.date,
                    'is_done': q.is_done, 'is_paid': q.is_paid}

    def get_success_url(self):
        return '/admin/job'


class AdminSettingPageView(LoginRequiredMixin, TemplateView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = "app/admin_setting.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        global show_promotion
        context.update({'show_promotion': show_promotion})
        return context

    def post(self, request):
        s = request.POST['show_promotion']
        print(s)
        global show_promotion
        show_promotion = s
        return redirect('admin_setting')
