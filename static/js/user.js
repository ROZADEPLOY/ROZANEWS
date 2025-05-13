const user = window.Telegram.WebApp.initDataUnsafe.user;

function loadMyTasks() {
  fetch("/api/get_tasks", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ user_id: user.id })
  })
  .then(res => res.json())
  .then(tasks => {
    const list = document.getElementById("myTasks");
    list.innerHTML = "";
    tasks.forEach(t => {
      const li = document.createElement("li");
      li.innerText = `${t.title} (${t.priority}): ${t.desc}`;
      list.appendChild(li);
    });
  });
}

function checkAlert() {
  fetch("/api/get_alert", {
    method: "POST"
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("alertStatus").innerText = data.active ? "⚠️ Тревога активна!" : "Спокойно";
  });
}

function sendReport() {
  const content = document.getElementById("reportContent").value;
  fetch("/api/upload_result", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ user_id: user.id, result: content })
  }).then(() => alert("Отчёт отправлен"));
}

window.onload = () => {
  loadMyTasks();
  checkAlert();
};