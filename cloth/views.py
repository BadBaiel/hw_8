from django.views.generic import ListView, CreateView
from . import models, forms


class ManListView(ListView):
    queryset = models.ProductCl.objects.filter(tags__name="man's clothes")

    template_name = "man_list.html"

    def get_queryset(self):
        return models.ProductCl.objects.filter(tags__name="man's clothes")


class WomenListView(ListView):
    queryset = models.ProductCl.objects.filter(tags__name="women's clothes")

    template_name = "women_list.html"

    def get_queryset(self):
        return models.ProductCl.objects.filter(tags__name="women's clothes")


class BabyListView(ListView):
    queryset = models.ProductCl.objects.filter(tags__name="baby's clothes")

    template_name = "baby_list.html"

    def get_queryset(self):
        return models.ProductCl.objects.filter(tags__name="baby's clothes")


class SportsWearListView(ListView):
    queryset = models.ProductCl.objects.filter(tags__name="sportswear")

    template_name = "sportswear_list.html"

    def get_queryset(self):
        return models.ProductCl.objects.filter(tags__name="sportswear")


class ClothesListView(ListView):
    queryset = models.ProductCl.objects.filter().order_by('-id')
    template_name = "clothes_list.html"

    def get_queryset(self):
        return models.ProductCl.objects.filter().order_by('-id')


class OrderClCreateView(CreateView):
    template_name = "add-order.html"
    form_class = forms.OrderClForm
    success_url = "/products/"
    queryset = models.OrderCl.objects.all()

    def form_valid(self, form):
        return super(OrderClCreateView, self).form_valid(form=form)