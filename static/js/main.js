function checkAccess() {
    const tg = window.Telegram.WebApp;
    fetch("/check_user", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: tg.initDataUnsafe.user.id })
    }).then(res => {
        if (res.ok) return res.json();
        else throw new Error("Access denied");
    }).then(data => {
        if (data.role === "admin") window.location.href = "/admin";
        else if (data.role === "staff") window.location.href = "/staff";
        else alert("Нет доступа");
    }).catch(() => alert("Ошибка доступа"));
}
