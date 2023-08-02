from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.utils.text import slugify

from urllib import request

from .models import Image


class ImageDownloadForm(forms.ModelForm):
    """Форма загрузки картинки"""

    class Meta:
        model = Image
        fields = ("url", "title", "description")
        widgets = {"url": forms.HiddenInput}

    def clean_url(self):
        url: str = self.cleaned_data["url"]
        extension = url.rsplit(".", 1)[1].lower()
        if extension not in ("jpg", "jpeg", "png"):
            raise ValidationError("This url contained not allowed extension format of the picture")
        return url

    def save(self, commit=True):
        image = super(ImageDownloadForm, self).save(commit=False)
        image_url: str = self.cleaned_data["url"]
        image_name = f"{slugify(image.title)}.{image_url.rsplit('.', 1)[1].lower()}"

        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)

        if commit:
            image.save()
        return image
