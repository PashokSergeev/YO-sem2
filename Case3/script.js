const images = [
  'images/img1.jpg',
  'images/img2.jpg',
  'images/img3.jpg',
  'images/img4.jpg',
  'images/img5.jpg'
];

let currentIndex = 0;

const imgElement = document.getElementById('slider-image');
const counterElement = document.getElementById('image-counter');
const nextBtn = document.getElementById('next-btn');
const prevBtn = document.getElementById('prev-btn');

function updateSlider() {
  imgElement.src = images[currentIndex];
  counterElement.textContent = `Изображение ${currentIndex + 1} из ${images.length}`;
}

nextBtn.addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % images.length; // Зацикливание вперед
  updateSlider();
});

prevBtn.addEventListener('click', () => {
  currentIndex = (currentIndex - 1 + images.length) % images.length; // Зацикливание назад
  updateSlider();
});

updateSlider(); // Инициализация при загрузке
