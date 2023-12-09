var textInput = document.forms.comment_form.text;
var cancelSaveElement = document.querySelector('.cansel-save')
var cancelButtonElement = cancelSaveElement.querySelector('.comment-cansel');

textInput.addEventListener("focus", function () {
    cancelSaveElement.style.display = "block";
});

cancelButtonElement.addEventListener("click", function () {
    cancelSaveElement.style.display = "none";
});


const commentSocket = new WebSocket(
    'wss://'
    + window.location.host
    + '/ws/comment_chat/'
    + workout_id
    + '/'
);

commentSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if ('message' in data) {
        var comments = document.getElementById('all_comments');
        var commentDiv = document.createElement("div");
        commentDiv.className = "comment";

        commentDiv.innerHTML = `
                        <div class="comment-autor-crAt">
                            <h1 class="comment-author">${data['name']}</h1>
                            <h1 class="comment-date">now</h1>
                        </div>
                        <div class="comment-text">
                            ${data['message']}
                        </div>
                        <div class="comment-like">
                            <h1 id="${data['id']}" class="like-count">
                                0
                            </h1>
                            <button class="commentLikeButton" data_comment_id="${data['id']}">
                                <img class="" src="/static/svg/like.svg" alt="Likes">
                            </button>
                        </div>
                    `;
        comments.insertBefore(commentDiv, comments.firstChild);
        var likeButton = document.querySelector('[data_comment_id="' + data['id'] + '"]')
        commentLikeWB(likeButton)

    } else if ('liked' in data) {
        likes = document.getElementById(data['comment_id'])
        like_image = document.querySelector('[data_comment_id="' + data['comment_id'] + '"]')
        like_image = like_image.getElementsByTagName('img')[0]
        likes.textContent = data['likes_count']
        if (data['liked']) {
            like_image.src = "/static/svg/liked.svg";
        } else {
            like_image.src = "/static/svg/like.svg";
        };
    };
};

commentSocket.onclose = function (e) {
    console.error('Comment socket closed unexpectedly');
};

document.getElementById('comment-submit').onclick = sendComment;
document.getElementById('comment_form').addEventListener('keydown', function (e) {
    if (e.keyCode === 13) {
        e.preventDefault();
        document.getElementById('comment-submit').click();
    }
})

function sendComment() {
    const messageInputDom = document.getElementById('comment-input');
    if (messageInputDom.value == '') {
        textInput.classList.add('shake');
        setTimeout(function () {
            textInput.classList.remove('shake');
        }, 500)
    } else {
        const message = messageInputDom.value;
        commentSocket.send(JSON.stringify({
            'message': message,
            'author': author_id,
            'type': 'create',
        }));
        messageInputDom.value = '';
    }
};

var likeButtons = document.getElementsByClassName('commentLikeButton')
for (let likeButton of likeButtons) {
    commentLikeWB(likeButton)
};

function commentLikeWB(likeButton) {
    likeButton.addEventListener("click", function () {
        commentSocket.send(JSON.stringify({
            'comment_id': parseInt(likeButton.getAttribute('data_comment_id')),
            'type': 'like',
        }));
    });
}