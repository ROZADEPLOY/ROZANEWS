const user = window.Telegram.WebApp.initDataUnsafe.user;

function addUser() {
  const id = document.getElementById("newUserId").value;
  const codename = document.getElementById("newUserCodename").value;
  fetch("/api/add_user", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ user_id: id, codename })
  }).then(() => alert("Сотрудник добавлен"));
}

function createTask() {
  const task = {
    user_id: parseInt(document.getElementById("taskUserId").value),
    title: document.getElementById("taskTitle").value,
    desc: document.getElementById("taskDesc").value,
    priority: document.getElementById("taskPriority").value
  };
  fetch("/api/create_task", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(task)
  }).then(() => alert("Задача создана"));
}

function sendAlert() {
  fetch("/api/alert", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ active: true })
  }).then(() => alert("Тревога отправлена"));
}

function loadTasks() {
  fetch("/api/get_tasks", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ user_id: user.id })
  })
  .then(res => res.json())
  .then(tasks => {
    const list = document.getElementById("taskList");
    list.innerHTML = "";
    tasks.forEach(t => {
      const li = document.createElement("li");
      li.innerText = `${t.title} (${t.priority}): ${t.desc}`;
      list.appendChild(li);
    });
  });
}

window.onload = loadTasks;