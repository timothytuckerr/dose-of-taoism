window.onload = function(event) {
    console.log("load")
    fetch('https://timoth-yt.herokuapp.com/daily-dose')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            document.getElementById("number").innerHTML = data['number']
            document.getElementById("text").innerHTML = data['text']
        })
};
