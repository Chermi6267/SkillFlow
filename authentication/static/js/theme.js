let switchMode = document.getElementById("switch");
let theme = document.getElementById("theme");

if (localStorage.getItem("selectedTheme")) {
  theme.href = localStorage.getItem("selectedTheme");
}

switchMode.onclick = function () {
  if (theme.getAttribute("href") == "/static/css/dark_theme.css") {
    theme.href = "/static/css/light_theme.css";

    localStorage.setItem("selectedTheme", "/static/css/light_theme.css");
  } else {
    theme.href = "/static/css/dark_theme.css";
    localStorage.setItem("selectedTheme", "/static/css/dark_theme.css");
  }
};
