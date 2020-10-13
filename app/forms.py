from django import forms

from app.models import Quote, WarrantyQuote, Job


class QuoteForm(forms.Form):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput)
    name = forms.CharField(max_length=100)
    email = forms.EmailField(label="Email")
    type = forms.ChoiceField(label='Type', required=True, widget=forms.RadioSelect(attrs={'required':'required'}), choices=[('purchase', 'purchase'), ('repair', 'repair'), ('warranty repair', 'warranty repair')])
    remark = forms.CharField(max_length=100, widget=forms.Textarea)


    def clean(self):
        id = self.cleaned_data.get('id')
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        type = self.cleaned_data.get('type')
        remark = self.cleaned_data.get('remark')

        if id:
            quote = Quote.objects.get(id=id)
            quote.name = name
            quote.email = email
            quote.type = type
            quote.remark = remark
        else:
            quote = Quote(name=name, email=email, type=type, remark=remark)
        quote.save()

class ServiceForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput)
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'', 'required':'required'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'', 'required':'required'}))
    phone = forms.IntegerField(label='Phone number', widget=forms.TextInput(attrs={'placeholder':'', 'required':'required'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'', 'required':'required'}))
    product = forms.CharField(label='Make + model number of faulty product', max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'', 'required':'required'}))
    company = forms.CharField(label='Name of installation company', max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'', 'required':'required'}))
    serial = forms.CharField(label='Unit serial number', max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'', 'required':'required'}))
    date = forms.DateField(label='Date of installation', required=True, widget=forms.DateInput(attrs={'placeholder':'', 'required':'required'}))
    under_warranty = forms.ChoiceField(label='Is the product under warranty still?', required=True, widget=forms.RadioSelect(attrs={'required':'required'}), choices=[('1', 'Not sure'), ('2', 'Yes'), ('3', 'No')])
    description = forms.CharField(label='Please describe the issues that you\'re having', max_length=10000, required=True, widget=forms.Textarea(attrs={'placeholder':'', 'required':'required'}))
    def clean(self):
        id = self.cleaned_data.get('id')
        name = self.cleaned_data.get('name')
        address = self.cleaned_data.get('address')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        product = self.cleaned_data.get('product')
        company = self.cleaned_data.get('company')
        serial = self.cleaned_data.get('serial')
        date = self.cleaned_data.get('date')
        under_warranty = self.cleaned_data.get('under_warranty')
        description = self.cleaned_data.get('description')
        if id:
            warranty_quote = WarrantyQuote.objects.get(id=id)
            warranty_quote.name = name
            warranty_quote.address = address
            warranty_quote.phone = phone
            warranty_quote.email = email
            warranty_quote.product = product
            warranty_quote.company = company
            warranty_quote.date = date
            warranty_quote.serial = serial
            warranty_quote.under_warranty = under_warranty
            warranty_quote.description = description
            warranty_quote.email = email
        else:
            warranty_quote = WarrantyQuote(name=name, address=address, phone=phone,
                              email=email, product=product, company=company, date=date,
                              serial=serial, under_warranty=under_warranty, description=description)
        warranty_quote.save()

class JobForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput)
    no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'', 'required':'required'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '', 'required': 'required'}))
    customer_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '', 'required': 'required'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '', 'required': 'required'}))
    date = forms.DateField(required=True, widget=forms.DateInput(attrs={'placeholder':'', 'required':'required'}))
    is_done = forms.ChoiceField(label='Is it done?', required=True, widget=forms.RadioSelect(attrs={'required':'required'}), choices=[('1', 'No'), ('2', 'Yes')])
    is_paid = forms.ChoiceField(label='Is it paid?', required=True, widget=forms.RadioSelect(attrs={'required':'required'}), choices=[('1', 'No'), ('2', 'Yes')])
    def clean(self):
        id = self.cleaned_data.get('id')
        no = self.cleaned_data.get('no')
        name = self.cleaned_data.get('name')
        customer_name = self.cleaned_data.get('customer_name')
        date = self.cleaned_data.get('date')
        address = self.cleaned_data.get('address')
        is_done = self.cleaned_data.get('is_done')
        is_paid = self.cleaned_data.get('is_paid')
        if id:
            job = Job.objects.get(id=id)
            job.name = name
            job.no = no
            job.customer_name = customer_name
            job.address = address
            job.date = date
            job.is_done = is_done
            job.is_paid = is_paid
        else:
            job = Job(name=name, no = no,customer_name = customer_name, address=address,
                              date=date, is_done=is_done, is_paid=is_paid)
        job.save()

class QuoteForm(QuoteForm):
    pass

class ServiceForm(ServiceForm):
    pass

class JobForm(JobForm):
    pass
