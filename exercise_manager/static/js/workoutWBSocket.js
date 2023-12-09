const workout_id = JSON.parse(document.getElementById('workout_id').textContent);
const author_id = JSON.parse(document.getElementById('user_id').textContent);

const workoutSocket = new WebSocket(
    'wss://'
    + window.location.host
    + '/ws/workout_chat/'
    + workout_id
    + '/'
);

workoutSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if ('liked' in data) {
        document.getElementById('workoutLikes').textContent = data['likes_count']
        like_image = document.querySelector('[data_workout_id="' + data['workout_id'] + '"]')
        like_image = like_image.getElementsByTagName('img')[0]
        if (data['liked']) {
            like_image.src = "/static/svg/liked.svg";
        } else {
            like_image.src = "/static/svg/like.svg";
        };
    } else {
        document.getElementById('views').textContent = data['views_count']
    }
}

document.getElementById('workoutLikeButton').addEventListener('click', function () {
    workoutSocket.send(JSON.stringify({
        'type': 'like',
    }));
})
workoutSocket.onopen = () => workoutSocket.send(JSON.stringify({ 'type': 'view' }));