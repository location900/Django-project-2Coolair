from django.conf.urls import url

from app.views import (
    HomePageView,
    AboutPageView,
    PurchasePageView,
    ServicePageView,
    LoginPageView,
    AdminQuotePageView,
    AdminQuoteDetailPageView,
    AdminWarrantyQuotePageView,
    AdminWarrantyQuoteDetailPageView,
    AdminSettingPageView,
    AdminJobPageView,
)

urlpatterns = [
    url(r"^$", HomePageView.as_view(), name="home"),
    url(r"^purchase$", PurchasePageView.as_view(), name="purchase"),
    url(r"^about$", AboutPageView.as_view(), name="about"),
    url(r"^service$", ServicePageView.as_view(), name="service"),
    url(r"^login$", LoginPageView.as_view(), name="login"),
    url(r"^admin/quote$", AdminQuotePageView.as_view(), name="admin_quote"),
    url(r"^admin/quote_detail$", AdminQuoteDetailPageView.as_view(), name="admin_quote_detail"),
    url(r"^admin/warranty_quote$", AdminWarrantyQuotePageView.as_view(), name="admin_warranty_quote"),
    url(r"^admin/warranty_quote_detail$", AdminWarrantyQuoteDetailPageView.as_view(), name="admin_warranty_quote_detail"),
    url(r"^admin/job$", AdminJobPageView.as_view(), name="admin_job"),
    url(r"^admin/setting$", AdminSettingPageView.as_view(), name="admin_setting"),
]
