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
            link.href = "/pybo/specific/"+cards[i].id+"/";
        });
    });

    var order_form = document.querySelector(".order_form");
    var order_select = document.querySelector(".order_select");
    var id_input = document.querySelector(".id_input");
    order_select.addEventListener("change", ()=>{
        var id_list = []
        cards.forEach((card, i)=>{
            id_list.push(card.id);
        });
        id_list.sort();
        id_input.value = id_list.toString(',');

        console.log(order_form.value);
        order_form.submit();
    });
}

window.onload = ()=>{
    update()
}