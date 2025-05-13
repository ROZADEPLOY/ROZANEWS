
const user = window.Telegram.WebApp.initDataUnsafe.user;

function loadTasks() {
  fetch("/api/get_tasks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: user.id })
  })
  .then(res => res.json())
  .then(data => {
    const tasksDiv = document.getElementById("tasks");
    data.forEach(task => {
      const div = document.createElement("div");
      div.innerHTML = `<h3>${task.title} (${task.priority})</h3><p>${task.desc}</p>`;
      tasksDiv.appendChild(div);
    });
  });
}

function uploadReport() {
  const content = document.getElementById("report_content").value;
  fetch("/api/upload_result", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: user.id, result: content })
  }).then(() => alert("Отчёт отправлен"));
}

function checkAlert() {
  fetch("/api/get_alert")
  .then(res => res.json())
  .then(data => {
    document.getElementById("alert_status").innerText = data.active ? "⚠️ Тревога активна!" : "Всё спокойно";
  });
}

window.onload = () => { loadTasks(); checkAlert(); };
