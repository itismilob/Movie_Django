var selected_tag_elements;
var preview_tag_elements;
var tag_input_element = document.querySelector(".tags_input");
var tag_input_text = [
];
var preview_tags = {
};

function add_tags(){

    preview_tag_elements = document.querySelectorAll(".preview_tag");
    preview_tag_elements.forEach(function (tag) {
        preview_tags[tag.innerHTML] = false;
    });

    selected_tag_elements = document.querySelectorAll(".selected_tag");
    selected_tag_elements.forEach(function (tag) {
        tag_input_text.push(tag.innerHTML);
        tag_input_text.sort();

        preview_tags[tag.innerHTML] = true;
    });

    var sorted = {}
    Object.keys(preview_tags).sort().forEach((key)=>{
       sorted[key] = preview_tags[key];
    });
    preview_tags = sorted;

    tag_input_element.value = tag_input_text.join(",");
}

function add_events(){
    selected_tag_elements = document.querySelectorAll(".selected_tag");
    selected_tag_elements.forEach(function (tag) {
        tag.addEventListener("click", function () {
            console.log(tag_input_text);
            var temp = tag_input_text.indexOf(tag.innerHTML);
            tag_input_text.splice(temp, 1);
            tag_input_element.value = tag_input_text.join(",");
            console.log(tag_input_text);

            console.log("remove:", tag.innerHTML);
            preview_tags[tag.innerHTML] = false;
            update_tags();
        });
    });

    preview_tag_elements = document.querySelectorAll(".preview_tag");
    preview_tag_elements.forEach(function (tag) {
        tag.addEventListener("click", function () {
            tag_input_text.push(tag.innerHTML);
            tag_input_text.sort();
            tag_input_element.value = tag_input_text.join(",");

            console.log("add:", tag.innerHTML);
            preview_tags[tag.innerHTML] = true;
            update_tags();
        });
    });
}

function update_tags() {
    var select_inner = "";
    var preview_inner = "";
    for (var key in preview_tags) {
        var value = preview_tags[key];
        if (value) {
            select_inner += "<div class=\"selected_tag\">".concat(key, "</div>");
        }
        else {
            preview_inner += "<div class=\"preview_tag_cover\"><div class=\"preview_tag\">".concat(key, "</div></div>");
        }
    }
    document.querySelector(".tags_selected").innerHTML = select_inner;
    document.querySelector(".tags_preview").innerHTML = preview_inner;

    add_events();
}

window.onload = ()=>{
    add_tags();
    add_events();
}