// Массив путей к изображениям
const images = [
  'images/img1.jpg',
  'images/img2.jpg',
  'images/img3.jpg',
  'images/img4.jpg',
  'images/img5.jpg'
];

// Текущий индекс изображения (начинается с 0)
let currentIndex = 0;

// Получаем элементы DOM
const imgElement = document.getElementById('slider-image');     // тег <img>
const counterElement = document.getElementById('image-counter'); // счётчик
const nextBtn = document.getElementById('next-btn');            // кнопка "Вперёд"
const prevBtn = document.getElementById('prev-btn');            // кнопка "Назад"

/**
 * Функция обновления слайдера:
 * - меняет картинку
 * - обновляет текст счётчика
 */
function updateSlider() {
  imgElement.src = images[currentIndex]; // устанавливаем src изображения
  counterElement.textContent = `Изображение ${currentIndex + 1} из ${images.length}`;
}

/**
 * Обработчик кнопки "Вперёд"
 * При достижении последнего изображения начинается сначала
 */
nextBtn.addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % images.length; // зацикливание вперёд
  updateSlider();
});

/**
 * Обработчик кнопки "Назад"
 * При достижении начала переходит к последнему изображению
 */
prevBtn.addEventListener('click', () => {
  currentIndex = (currentIndex - 1 + images.length) % images.length; // зацикливание назад
  updateSlider();
});

// Первая инициализация слайдера при загрузке страницы
updateSlider();
