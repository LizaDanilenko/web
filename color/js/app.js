const button =document.getElementById("btn");
const color = document.querySelector(".color");
const colorInput = document.getElementById("colorInput");


button.addEventListener("click", () =>{
    let hexColor = colorInput.value;
    const hexRegex = /^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/;
    if (hexRegex.test(hexColor)) {
        document.body.style.backgroundColor = hexColor;
        color.textContent = hexColor;
    } else {
        alert('Пожалуйста введите корректное значение');
    }
});

colorInput.addEventListener("keypress", function(e) {
    if (e.key === 'Enter') {
        button.click();
    }
});

