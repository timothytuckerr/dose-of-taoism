window.onload = function(event) {
    console.log("load")
    fetch('https://timoth-yt.herokuapp.com/daily-dose')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            document.getElementById("header").innerHTML = "The Tao Te Ching, Chapter " + data['number']
            document.getElementById("text").innerHTML = data['text']
    })
    fetch('https://timoth-yt.herokuapp.com/daily-dose-image')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            document.body.style.backgroundImage = "url(" + data['url'] + ")";
    })
};

let button = document.getElementById("refresh");
button.addEventListener("click", function(event) {
    console.log('click');
    fetch('https://timoth-yt.herokuapp.com/refresh-daily-image')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            window.location.reload();
    })
})
