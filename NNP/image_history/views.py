from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from image_analysis.models import UploadedImage


@login_required
def image_history(request):
    # Получаем все изображения пользователя
    images = UploadedImage.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'image_history/image_history.html', {'images': images})


@login_required
def delete_image(request, image_id):
    try:
        # Получаем изображение
        image = UploadedImage.objects.get(id=image_id, user=request.user)

        # Удаляем изображение
        image.image.delete(save=False)  # Удалить оригинальное изображение
        if image.processed_image:
            image.processed_image.delete(save=False)  # Удалить обработанное изображение

        image.delete()  # Удаляем запись в базе данных

        return redirect('image_history')
    except UploadedImage.DoesNotExist:
        raise Http404("Изображение не найдено.")
