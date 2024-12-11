document.addEventListener("DOMContentLoaded", () => {
    const uploadBtn = document.getElementById('uploadBtn');
    const processBtn = document.getElementById('processBtn');
    const imageInput = document.getElementById('imageInput');
    const preview = document.getElementById('preview');
    const errorMsg = document.getElementById('errorMsg');
    const analysisResult = document.getElementById('analysis-result');
    uploadBtn.addEventListener('click', () => imageInput.click());
    imageInput.addEventListener('change', () => {
        const file = imageInput.files[0];
        if (file) {
            const formData = new FormData();
            formData.append('image', file);
            fetch('{% url "upload_image" %}', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}',
                },
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                if (data.file_url) {
                    preview.src = data.file_url;
                    preview.classList.remove('hidden');
                    processBtn.classList.remove('hidden');
                    errorMsg.textContent = '';
                    analysisResult.textContent = 'Нажмите "Обработать изображение" для начала анализа.';
                } else {
                    errorMsg.textContent = data.error || 'Ошибка загрузки файла.';
                }
            })
            .catch(() => {
                errorMsg.textContent = 'Произошла ошибка при загрузке.';
            });
        }
    });
    processBtn.addEventListener('click', () => {
        analysisResult.textContent = 'Обработка изображения началась...';
        // Логика обработки изображения
    });