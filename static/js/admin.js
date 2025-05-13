
function addUser() {
  const id = document.getElementById("new_id").value;
  const codename = document.getElementById("new_codename").value;
  fetch("/api/add_user", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: id, codename })
  }).then(res => alert("Сотрудник добавлен"));
}

function createTask() {
  const data = {
    user_id: document.getElementById("task_id").value,
    title: document.getElementById("task_title").value,
    desc: document.getElementById("task_desc").value,
    priority: document.getElementById("task_priority").value
  };
  fetch("/api/create_task", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  }).then(res => alert("Задача создана"));
}

function sendAlert() {
  fetch("/api/alert", { method: "POST" }).then(() => alert("Тревога активирована"));
}
