document.addEventListener("DOMContentLoaded", function () {
    var textInput = document.forms.comment_form.text;
    var cancelSaveElement = document.querySelector('.cansel-save')
    var cancelButtonElement = cancelSaveElement.querySelector('.comment-cansel');

    textInput.addEventListener("focus", function () {
        cancelSaveElement.style.display = "block";
    });

    cancelButtonElement.addEventListener("click", function () {
        cancelSaveElement.style.display = "none";
    });

    document.forms.comment_form.onsubmit = function (e) {
        e.preventDefault();
        var text = textInput.value;

        if (text == '') {
            textInput.classList.add('shake');
            setTimeout(function () {
                textInput.classList.remove('shake');
            }, 500);
        } else {
            var csrfToken = getCookie("csrftoken");
            var workoutId = document.getElementById("workoutLikeButton").getAttribute('data_workout_id');
            console.log(workoutId)
            var xhr = new XMLHttpRequest();

            xhr.open('POST', '/my_api/comment_system/');
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=utf8");
            xhr.setRequestHeader("X-CSRFToken", csrfToken);
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    document.forms.comment_form.text.value = '';
                    var commentData = JSON.parse(this.response);
                    var comments = document.getElementById('all_comments');

                    var commentDiv = document.createElement("div");
                    commentDiv.className = "comment";

                    commentDiv.innerHTML = `
                        <div class="comment-autor-crAt">
                            <h1 class="comment-author">${commentData.comment_author}</h1>
                            <h1 class="comment-date">${commentData.comment_time}</h1>
                        </div>
                        <div class="comment-text">
                            ${commentData.comment_text}
                        </div>
                        <div class="comment-like">
                            <h1 id="${commentData.comment_id}" class="like-count">
                                ${commentData.likes_count}
                            </h1>
                            <button class="commentLikeButton" data_comment_id="${commentData.comment_id}">
                                <img class="" src="/static/svg/like.svg" alt="Likes">
                            </button>
                        </div>
                    `;
 
                    comments.insertBefore(commentDiv, comments.firstChild);

                    var likeButton = document.querySelector('[data_comment_id="' + commentData.comment_id + '"]')
                    likeButton.addEventListener('click', function () {
                        commentLike(likeButton);
                    });
                }
            };
            xhr.send('comment=' + text + '&workout_id=' + workoutId + '&type=create');
        }
    }
});