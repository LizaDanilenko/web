const todoInput = document.querySelector('.todo__input');
const todoBtn = document.querySelector('.todo__btn');
const todoList = document.querySelector('.todo__list');

todoBtn.addEventListener('click', function () {
    addTask()
})

function addTask() {

    if(todoInput.value === '') {
        alert('Нужно ввести текст')
    } else {
        let li = document.createElement('li')
        li.innerHTML = todoInput.value
        todoList.appendChild(li)
        let span = document.createElement('span')
        span.innerHTML = '\u00d7'
        li.appendChild(span)
    }
    todoInput.value = '';
    saveData()
}

todoList.addEventListener('click', function (e) {

    if (e.target.tagName === 'LI') {
        e.target.classList.toggle('checked')
        saveData()
    } else if (e.target.tagName === 'SPAN') {
        e.target.parentElement.remove()
        saveData()
    }

})

todoInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        addTask()
    }
})

function saveData() {
    localStorage.setItem('data', todoList.innerHTML)
}
function showData() {
    todoList.innerHTML = localStorage.getItem('data')
}

showData();