from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import (CreateView, UpdateView)
from django.db.models import Sum


from .forms import (
    GiornalieroForm, DettagliFormSet, ImageFormSet
)
from .models import (
    Image,
    Dettagli,
    Giornaliero
)


class GiornalieroInline():
    form_class = GiornalieroForm
    model = Giornaliero
    template_name = "statistiche/giornaliero_aggiorna_crea.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('statistiche:list_giornaliero')


    def formset_dettagli_valid(self, formset):
        dettagli = formset.save(commit=False)  
        for obj in formset.deleted_objects:
            obj.delete() 
        for dettaglio in dettagli:
            dettaglio.giornaliero = self.object
            dettaglio.save() #In questo punto salviamo i dati finali ed usciamo dalla maschera di inserimento 


    def formset_images_valid(self, formset):
        images = formset.save(commit=False)  
        for obj in formset.deleted_objects:
            obj.delete()
        for image in images:
            image.product = self.object
            image.save()
                


class GiornalieroCreate(GiornalieroInline, CreateView): 

    def get_context_data(self, **kwargs):
        ctx = super(GiornalieroCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'dettagli': DettagliFormSet(prefix='dettagli'),
                'images': ImageFormSet(prefix='images'),
            }
        else:
            return {
                'dettagli': DettagliFormSet(self.request.POST or None, self.request.FILES or None, prefix='dettagli'),
                'images': ImageFormSet(self.request.POST or None, self.request.FILES or None, prefix='images'),
            }


class GiornalieroUpdate(GiornalieroInline, UpdateView):
    
    def get_context_data(self, **kwargs):
        ctx = super(GiornalieroUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'dettagli': DettagliFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='dettagli'),
            'images': ImageFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='images'),
        }
    

def delete_image(request, pk):
    try:
        image = Image.objects.get(id=pk)
    except Image.DoesNotExist:
        messages.success(request, 'Object Does not exit')
        return redirect('statistiche:update_giornaliero', pk=image.giornaliero.id)

    image.delete()
    messages.success(request, 'Image deleted successfully')
    return redirect('statistiche:update_giornaliero', pk=image.giornaliero.id)


def delete_dettaglio(request, pk):
    try:
        dettagli = Dettagli.objects.get(id=pk)
    except Dettagli.DoesNotExist:
        messages.success(request, 'Object Does not exit')
        return redirect('statistiche:update_giornaliero', pk=dettagli.giornaliero.id)

    dettagli.delete()
    messages.success(request,'Variant deleted successfully')
    return redirect('statistiche:update_giornaliero', pk=dettagli.giornaliero.id)


class GiornalieroList(ListView):
    model = Giornaliero
    template_name = "statistiche/list_giornaliero.html"
    context_object_name = "statistiche"

