from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView

from app.forms import QuoteForm, ServiceForm, SettingForm
from app.models import Quote, WarrantyQuote

class HomePageView(TemplateView):
    template_name = "app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PurchasePageView(FormView):
    template_name = "app/purchase.html"
    form_class = QuoteForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def get_success_url(self):
        return '/purchase'

class ServicePageView(FormView):
    template_name = "app/service.html"
    form_class = ServiceForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def get_success_url(self):
        return '/service'

class AboutPageView(TemplateView):
    template_name = "app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LoginPageView(TemplateView):
    template_name = "app/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AdminQuotePageView(TemplateView):
    template_name = "app/admin_quote.html"
    def get_context_data(self, **kwargs):
        del_id = self.request.GET.get('del_id')
        if del_id:
            Quote.objects.filter(id=del_id).delete()
        q = Quote.objects.all()
        context = super().get_context_data(**kwargs)
        context.update({'quotes':q})
        return context

class AdminQuoteDetailPageView(FormView):
    template_name = "app/admin_quote_detail.html"
    form_class = QuoteForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_initial(self):
        id = self.request.GET.get('id')
        if id:
            q = Quote.objects.get(id=id)
            return {'id':q.id, 'name': q.name, 'email':q.email}

    def get_success_url(self):
        return '/admin/quote'

class AdminWarrantyQuoteDetailPageView(FormView):
    template_name = "app/admin_warranty_quote_detail.html"
    form_class = ServiceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_initial(self):
        id = self.request.GET.get('id')
        if id:
            q = WarrantyQuote.objects.get(id=id)
            return {'id': q.id, 'name': q.name, 'address':q.address, 'phone': q.phone,
                    'email': q.email, 'product': q.product, 'company': q.company,
                    'serial': q.serial, 'date': q.date, 'under_warranty': q.under_warranty, 'description': q.description}

    def get_success_url(self):
        return '/admin/warranty_quote'


class AdminWarrantyQuotePageView(TemplateView):
    template_name = "app/admin_warranty_quote.html"

    def get_context_data(self, **kwargs):
        del_id = self.request.GET.get('del_id')
        if del_id:
            WarrantyQuote.objects.filter(id=del_id).delete()
        q = WarrantyQuote.objects.all()
        context = super().get_context_data(**kwargs)
        context.update({'quotes': q})
        return context

class AdminJobPageView(TemplateView):
    template_name = "app/admin_job.html"
    def get_context_data(self, **kwargs):
        del_id = self.request.GET.get('del_id')
        if del_id:
            Quote.objects.filter(id=del_id).delete()
        q = Quote.objects.all()
        context = super().get_context_data(**kwargs)
        context.update({'quotes':q})
        return context


class AdminSettingPageView(FormView):
    template_name = "app/admin_setting.html"
    form_class = SettingForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_initial(self):
        return {'show_ad' : 1}

    def get_success_url(self):
        return '/admin/setting'