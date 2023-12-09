document.addEventListener("DOMContentLoaded", function () {
    var workoutId = document.getElementById("workoutLikeButton").getAttribute('data_workout_id');
    var viewsCount = document.getElementById("views");
    var csrfToken = getCookie("csrftoken");
    var xhr = new XMLHttpRequest();

    xhr.open("POST", "/my_api/views_system/");
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=utf8");
    xhr.setRequestHeader("X-CSRFToken", csrfToken);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status === 200) {
            var data = JSON.parse(xhr.responseText);
            if (!data.viewed) {
                viewsCount.textContent = data.number_of_views;
            }
        }
    };
    xhr.send('workout_id=' + workoutId);
});