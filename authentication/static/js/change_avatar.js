// Отслеживаем событие нажатия на кнопку "Выбрать файл"
document.getElementById('chooseFileBtn').addEventListener('click', function () {
    // Имитируем клик по скрытому input типа "file"
    document.getElementById('id_avatar').click();
});