from django.contrib import admin
from django.utils.html import format_html
from .models import UploadedImage

@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_tag', 'processed_image_tag', 'uploaded_at', 'analysis_result_display')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

    def processed_image_tag(self, obj):
        if obj.processed_image:
            return format_html('<img src="{}" width="100" />', obj.processed_image.url)
        return "-"
    processed_image_tag.short_description = 'Processed Image'

    def analysis_result_display(self, obj):
        if obj.analysis_result:
            # Отображаем часть результата анализа в виде строки
            return format_html('<pre>{}</pre>', obj.analysis_result)
        return "-"
    analysis_result_display.short_description = 'Analysis Result'