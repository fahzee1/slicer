from django.contrib import admin

from .models import ImageSeries, PNGImage



@admin.register(ImageSeries)
class ImageSeriesAdmin(admin.ModelAdmin):
    readonly_fields = ('voxel_file', 'patient_id', 'study_uid', 'series_uid')


@admin.register(PNGImage)
class PNGAdmin(admin.ModelAdmin):
    readonly_fields = ('png_file',)
