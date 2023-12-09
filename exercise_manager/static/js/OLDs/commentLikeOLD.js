document.addEventListener("DOMContentLoaded", function () {
    var likeButtons = document.getElementsByClassName('commentLikeButton')

    for (let likeButton of likeButtons) {
        likeButton.addEventListener("click", function () {
            commentLike(likeButton)
        });
    };
});

function commentLike(likeButton) {
    var image = likeButton.getElementsByTagName('img')[0];
    var commentId = likeButton.getAttribute('data_comment_id');
    var csrfToken = getCookie("csrftoken");
    var likesCount = document.getElementById(commentId);
    var xhr = new XMLHttpRequest();

    xhr.open("POST", "/my_api/comment_system/");
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
    xhr.send('comment_id=' + commentId + '&type=like');
};