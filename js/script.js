
function showMessage() {
    const messages = [
        "🔥 환영합니다! 즐거운 시간 보내세요!",
        "🏍️ 라이딩처럼 신나는 하루 되세요!",
        "🚀 방문해 주셔서 감사합니다!",
        "⭐ 이승호의 공간에 오신 것을 환영합니다!"
    ];

    const random =
        messages[Math.floor(Math.random() * messages.length)];

    document.getElementById("message").innerText = random;
}