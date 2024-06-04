from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import MaterialForm
from blog.models import Material


class MaterialCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Представление добавления статьи"""

    model = Material
    fields = ('title', 'body', 'preview',)
    success_url = reverse_lazy('blog:list')
    permission_required = "blog.add_material"

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class MaterialUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Представление редактирования статьи"""

    model = Material
    form_class = MaterialForm
    permission_required = "blog.change_material"

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class MaterialListView(ListView):
    """Представление отображения списка статей"""

    model = Material

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(is_published=True)
    #
    #     return queryset


class MaterialDetailView(DetailView):
    model = Material

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class MaterialDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Представление удаления статьи"""

    model = Material
    success_url = reverse_lazy('blog:list')
    permission_required = "blog.delete_material"
