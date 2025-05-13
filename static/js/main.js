function checkAccess() {
  const user = window.Telegram.WebApp.initDataUnsafe.user;
  fetch("/api/check_user", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: user.id })
  })
  .then(res => res.json())
  .then(data => {
    if (data.role === "admin") {
      window.location.href = "/admin";
    } else if (data.role === "user") {
      window.location.href = "/user";
    } else {
      alert("У вас нет административных прав");
    }
  });
}