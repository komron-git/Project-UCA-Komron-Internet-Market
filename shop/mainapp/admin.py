from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from .models import *
from PIL import Image
# from django.utils.safestring import mark_safe

class NotebookAdminForm(ModelForm):


       def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = 'При загрузке изображения с разрешением больше  {}x{} оно будет обрезано!'.format(
                *Product.MAX_RESOLUTION
            )
        




       # def __init__(self, *args, **kwargs):
       #  super().__init__(*args, **kwargs)
       #  self.fields['image'].help_text = mark_safe(
       #      """<span style="color:red;font-size:14px"При загрузке изображения с разрешением больше  {}x{} оно будет обрезано!</span>
       #      """.format(
       #          *Product.MAX_RESOLUTION
       #      )
       #  )

    # def clean_image(self):
    #     image = self.cleaned_data['image']
    #     img = Image.open(image)
    #     min_height, min_width = Product.MIN_RESOLUTION
    #     max_height, max_width = Product.MAX_RESOLUTION
    #     if image.size > Product.MAX_IMAGE_SIZE:
    #         raise ValidationError('Размер изображения не должен привышать 3МБ!')
    #     if img.height < min_height or img.width < min_width:
    #         raise ValidationError('Разрешение изображения меньше минимального!')
    #     if img.height < max_height or img.width < max_width:
    #         raise ValidationError('Разрешение изображения больше максимального!')
    #     return image

class NotebookAdmin(admin.ModelAdmin):

    form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class TVAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='TV'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartwatchAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='Smartwatch'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(TV, TVAdmin)
admin.site.register(Smartwatch, SmartwatchAdmin)