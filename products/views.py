from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product, Comment
from .forms import CommentForm


class ProductListView(generic.ListView):
    model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/products.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    context_object_name = 'commentform'

    def form_valid(self, form):
        # turn into to a model of comment
        comment = form.save(commit=False)

        # add the user
        comment.author = self.request.user

        # add the product number
        pk = int(self.kwargs['pk'])
        product = get_object_or_404(Product, pk=pk)
        comment.product = product

        return super().form_valid(form)
