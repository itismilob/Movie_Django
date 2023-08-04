function update(){
    var cards = document.querySelectorAll(".movie_card");
    var card_poster = document.querySelectorAll(".card_poster");
    var preview = document.querySelector(".preview_poster");
    var link = document.querySelector(".link");

    card_poster.forEach((card, i)=>{
        card.addEventListener("click", ()=>{
            preview.src = card_poster[i].src;
            preview.style.width = '500px';
            preview.style.height = '700px';
            link.href = "/pybo/specific/"+card.id+"/";
        });
    });
}

window.onload = ()=>{
    update()
}