from django.shortcuts import render
import pdb
from .models import ImageSeries, PNGImage


def image_series_list(request):
    return render(request, 'image_series_list.html', {
        'all_image_series': ImageSeries.objects.all(),
    })



def view_pngs(request,id):
    try:
        series = ImageSeries.objects.get(pk=id)
        png_images = PNGImage.objects.filter(series=series)
        data = {}
        data['images'] = png_images
        return render(request,'image_series_detail.html',data)

    except ImageSeries.DoesNotExist: 
        return render(request,'image_series_detail.html',data)
