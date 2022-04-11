window.onload = function(event) {
    console.log("load")
    fetch('https://timoth-yt.herokuapp.com/api/taoism/daily-dose')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            document.getElementById("header").innerHTML = "The Tao Te Ching, Chapter " + data['number']
            document.getElementById("text").innerHTML = data['text']
            document.body.style.backgroundImage = "url(" + data['image']['url'] + ")";
    })
};
