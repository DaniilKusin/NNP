from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
import os
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UploadedImage
from .hpe_opencv.get_human_data import get_image_points
from .height_calulate.predict_height import predict_height
import cv2
import numpy as np
from django.conf import settings

def get_analysis_page(request):
    return render(request, 'image_analysis/home.html')


@login_required
def upload_image(request):
    if request.method == "POST" and request.FILES.get('image'):
        image = request.FILES['image']
        if image.content_type != 'image/jpeg':
            return JsonResponse({'error': 'Файл должен быть формата JPEG.'}, status=400)
        if image.size > 2 * 1024 * 1024:
            return JsonResponse({'error': 'Размер файла не должен превышать 2 МБ.'}, status=400)

        uploaded_image = UploadedImage.objects.create(user=request.user, image=image)
        return JsonResponse({'file_url': uploaded_image.image.url})

    return JsonResponse({'error': 'Некорректный запрос.'}, status=400)



@login_required
def analyze(request):
    try:
        # Получаем последнее изображение пользователя
        uploaded_image = UploadedImage.objects.filter(user=request.user).latest('uploaded_at')
        image_path = uploaded_image.image.path

        # Загружаем изображение с диска
        image = cv2.imread(image_path)
        if image is None:
            return JsonResponse({'error': 'Не удалось загрузить изображение.'}, status=500)

        # Обработка изображения с помощью нейросети
        detected_points, processed_frame = get_image_points(image)
        height = int(predict_height(detected_points))
        # Сохраняем обработанное изображение
        processed_image_path = os.path.join(settings.MEDIA_ROOT, 'processed',
                                            f'processed_{os.path.basename(image_path)}')
        cv2.imwrite(processed_image_path, processed_frame)

        # Обновляем запись в базе данных
        uploaded_image.processed_image = os.path.join('processed', f'processed_{os.path.basename(image_path)}')
        uploaded_image.analysis_result = height  # Сохраняем результаты обработки
        uploaded_image.save()

        return JsonResponse({
            'processed_image_url': uploaded_image.processed_image.url,
            'analysis_result': height
        })

    except UploadedImage.DoesNotExist:
        return JsonResponse({'error': 'Нет загруженных изображений для анализа.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)



def get_human_data(image):
    image_data = ''
    human_data = ''
    return image_data, human_data


def get_height(human_data):
    return 1.0
