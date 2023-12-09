document.getElementById("show-password-btn").addEventListener("click", function() {
    var passwordInput = document.getElementById("id_password1");
    var showPasswordBtn = document.getElementById("show-password-btn");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        showPasswordBtn.classList.add("hidden-password");
        showPasswordBtn.classList.remove("show-password");
    } else {
        passwordInput.type = "password";
        showPasswordBtn.classList.add("show-password");
        showPasswordBtn.classList.remove("hidden-password");
    }
});
