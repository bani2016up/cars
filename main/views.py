from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from .models import Car


class CarsView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        params = self.request.GET
        query = Q()
        for key, value in params.items():
            if value and key in vars(Car):
                query &= Q(**{key: value})
        return {"cars": Car.objects.filter(query)}
    
def info(request, car_slug):
    car = get_object_or_404(Car, slug=car_slug)
    data = {
        'car_slug': car_slug,
        'car' : car
    }
    return render(request, 'info.html', data)
