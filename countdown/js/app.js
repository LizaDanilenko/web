const items = document.querySelectorAll(".countdown-item > h4");
const countdownElement = document.querySelector(".countdown");
//дата отсчета

let countdownDate = new Date(2025, 12, 0, 0, 0, 0).getTime();

function getCountdownTime() {
    //получить текущее время
    const now = new Date().getTime();
    //найти разницу
    const distance = countdownDate - now;

    //1с = 1000мс
    //1m = 60c
    //1ч = 60m
    //1д = 24ч

    //создаем переменные в милисекундах
    const oneDay = 24 * 60 * 60 * 1000;
    const oneHours = 60 * 60 * 1000;
    const oneMinutes = 60 * 1000;

    //подсчет для дней часов минут и секунд
    let days = Math.floor(distance / oneDay);
    let hours = Math.floor((distance % oneDay) / oneHours);
    let minutes = Math.floor((distance % oneHours) / oneMinutes);
    let seconds = Math.floor((distance % oneMinutes) / 1000);


    //создаем массив с переменными
    const values = [days, hours, minutes, seconds];
    console.log(values);

    //добаляем значение переменных на страницу
    items.forEach(function (item, index) {
        item.textContent = (values[index]);
    });

    if (distance < 0) {
        clearInterval(countdown);
        countdownElement.innerHTML = "<h4 class='expired'>Время вышло</h4>";
    }
}

//обновление счетчика каждую секунду
let countdown = setInterval(getCountdownTime, 1000);

//инициализация текущего времени

getCountdownTime();

