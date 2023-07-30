var selected_tag_elements;
var preview_tag_elements;
var add_tag_cover_element;
var tag_input_element = document.querySelector(".tags_input");
var tag_input_text = [];
var preview_tags = {
    "Action": false,
    "Adventure": false,
    "Drama": false,
    "Science Fiction": false,
};
var tags = [
    "Action",
    "Adventure",
    "Drama",
    "Science Fiction",
];
var isAddTagShow = false;


function update_tags() {
    var select_inner = "";
    var preview_inner = "";
    for (var key in preview_tags) {
        var value = preview_tags[key];
        if (value) {
            select_inner += "<div class=\"selected_tag\">".concat(key, "</div>");
        }
        else {
            preview_inner += "<div class=\"preview_tag_cover\"><div class=\"preview_tag\">".concat(key, "</div><div class=\"preview_tag_delete\"><div class=\"delete\"></div></div></div>");
        }
    }
    preview_inner += "<div class=\"add_tag\">\n<div class=\"plus_cover\"><div class=\"plus\"></div></div>\n<div class=\"add_tag_cover\">\n<label><input class=\"add_tag_input\" type=\"text\"></label>\n<input class=\"add_tag_submit\" type=\"button\" value=\"Add\">\n</div>\n</div>";
    document.querySelector(".tags_selected").innerHTML = select_inner;
    document.querySelector(".tags_preview").innerHTML = preview_inner;
    selected_tag_elements = document.querySelectorAll(".selected_tag");
    selected_tag_elements.forEach(function (tag) {
        tag.addEventListener("click", function () {
            var temp = tag_input_text.indexOf(tag.innerHTML);
            tag_input_text.splice(temp, 1);
            tag_input_element.value = tag_input_text.join(",");

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
    add_tag_cover_element = document.querySelector(".add_tag_cover");
    add_tag_cover_element.setAttribute("style", "display: none");
    document.querySelector(".plus_cover").addEventListener("click", plus_btn);
    isAddTagShow = false;
    document.querySelector(".add_tag_submit").addEventListener("click", add_tag_to_DB);
}

function add_tag_to_DB() {
    var _this = this;
    var value = document.querySelector(".add_tag_input").value;
    document.querySelector(".add_tag_input").value = "";
}
function plus_btn() {
    if (isAddTagShow) {
        add_tag_cover_element.setAttribute("style", "display: none");
        isAddTagShow = false;
    }
    else {
        add_tag_cover_element.setAttribute("style", "display: block");
        isAddTagShow = true;
    }
}

window.onload = ()=>{
    console.log("window loaded");
    update_tags();
}