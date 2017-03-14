import io
import zipfile
import pdb
from PIL import Image
import numpy as np
from django.db import models
from django.utils.safestring import mark_safe
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import InMemoryUploadedFile

from slicer.dicom_import import dicom_datasets_from_zip, combine_slices

class PNGImage(models.Model):
    png_file = models.ImageField(upload_to="slices/")
    series = models.ForeignKey('ImageSeries',default='')

    def __str__(self):
        return "Image - {}".format(self.png_file.name)


    class Meta:
        verbose_name_plural = 'Images'



class ImageSeries(models.Model):
    dicom_archive = models.FileField(upload_to="dicom/")
    voxel_file = models.FileField(upload_to="voxels/")
    patient_id = models.CharField(max_length=64, null=True)
    study_uid = models.CharField(max_length=64)
    series_uid = models.CharField(max_length=64)

    def __str__(self):
        return 'series-{}'.format(self.series_uid)

    @property
    def voxels(self):
        with self.voxel_file as f:
            voxel_array = np.load(f)
        return voxel_array

    def png_count(self):
        return PNGImage.objects.filter(series=self).count()

    def generate_pngs_from_voxels(self, voxels):
        for k, v in enumerate(voxels.T):
            im = Image.fromarray(v).convert('RGB')
            image_io = io.BytesIO()
            im.save(image_io, format='PNG')
            name = 'slice-{}.png'.format(k)
            image_file = InMemoryUploadedFile(image_io, None, name, 'image/png',512, None)

            png = PNGImage()
            png.png_file = image_file
            png.series = self
            png.save()



    def save(self, *args, **kwargs):
        with zipfile.ZipFile(self.dicom_archive, 'r') as f:
            dicom_datasets = dicom_datasets_from_zip(f)


        voxels, _ = combine_slices(dicom_datasets)
        content_file = ContentFile(b'')  # empty zero byte file
        np.save(content_file, voxels)
        self.voxel_file.save(name='voxels', content=content_file, save=False)
        self.patient_id = dicom_datasets[0].PatientID
        self.study_uid = dicom_datasets[0].StudyInstanceUID
        self.series_uid = dicom_datasets[0].SeriesInstanceUID

        super(ImageSeries, self).save(*args, **kwargs)
        
        if not self.png_count():
            self.generate_pngs_from_voxels(voxels)

    class Meta:
        verbose_name_plural = 'Image Series'
