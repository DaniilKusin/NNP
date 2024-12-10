document.addEventListener('DOMContentLoaded', () => {
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
            if (file.type !== 'image/jpeg') {
                errorMsg.textContent = 'Файл должен быть формата JPEG.';
                return;
            }
            if (file.size > 2 * 1024 * 1024) {
                errorMsg.textContent = 'Размер файла не должен превышать 2 МБ.';
                return;
            }

            const reader = new FileReader();
            reader.onload = (e) => {
                preview.src = e.target.result;
                preview.classList.remove('hidden');
                processBtn.classList.remove('hidden');
                errorMsg.textContent = '';
                analysisResult.textContent = 'Нажмите "Обработать изображение" для начала анализа.';
            };
            reader.readAsDataURL(file);
        }
    });

    processBtn.addEventListener('click', () => {
        analysisResult.textContent = 'Обработка изображения началась...';
        // Логика обработки изображения
    });
});
