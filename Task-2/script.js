const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");

function addTask() {
    const taskText = taskInput.value.trim();
    if (taskText === "") return;

    const li = document.createElement("li");
    li.innerHTML = `
        <span>${taskText}</span>
        <button onclick="completeTask(this)">Complete</button>
        <button onclick="deleteTask(this)">Delete</button>
    `;
    taskList.appendChild(li);
    taskInput.value = "";
}

function completeTask(button) {
    const taskItem = button.parentElement;
    taskItem.classList.toggle("completed");
}

function deleteTask(button) {
    const taskItem = button.parentElement;
    taskList.removeChild(taskItem);
}

function deleteAllTasks() {
    const taskItems = taskList.querySelectorAll("li");
    taskItems.forEach(taskItem => {
        taskList.removeChild(taskItem);
    });
}

