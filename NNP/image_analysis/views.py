from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
import os
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
        file_path = default_storage.save(f'uploads/{image.name}', image)
        file_url = default_storage.url(file_path)
        return JsonResponse({'file_url': file_url})
    return JsonResponse({'error': 'Некорректный запрос.'}, status=400)



@login_required
def analyze(request):
    pass


def get_human_data(image):
    image_data = ''
    human_data = ''
    return image_data, human_data


def get_height(human_data):
    return 1.0
