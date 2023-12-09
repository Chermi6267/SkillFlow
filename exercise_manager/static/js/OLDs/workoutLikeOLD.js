document.addEventListener("DOMContentLoaded", function () {
    var likeButton = document.getElementById("workoutLikeButton");

    likeButton.addEventListener("click", function (e) {
        e.preventDefault();
 
        var workoutId = likeButton.getAttribute('data_workout_id');
        var csrfToken = getCookie("csrftoken");
        var likesCount = document.getElementById("workoutLikes");
        var xhr = new XMLHttpRequest();
        var image = likeButton.getElementsByTagName('img')[0];


        xhr.open("POST", "/my_api/like_system/");
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=utf8");
        xhr.setRequestHeader("X-CSRFToken", csrfToken);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var data = JSON.parse(xhr.responseText);
                if (data.liked) {
                    image.src = "/static/svg/liked.svg";
                } else {
                    image.src = "/static/svg/like.svg";
                }
                likesCount.textContent = data.updated_likes_count;
            }
        };
        xhr.send('workout_id=' + workoutId);
    });
});