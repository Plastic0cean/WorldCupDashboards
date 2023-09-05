let limit = 10;
let list = document.querySelectorAll(".row-on-hover-grey")
let button = document.getElementsByClassName("show-more")[0]

function loadTableRows() {

    if (list.length > limit) {
        button.style.display = "inline-block";
        list.forEach((item, key) => {
            if (key > limit) {
                item.style.display = "none";
            }
            else {
                item.style.display = "table-row";
            }
        })
    }
    else {
        button.style.display = "none";
    }
}

function showMore() {
    limit = limit + 10;
    loadTableRows();
    window.scrollTo({ left: 0, top: document.body.scrollHeight, behavior: "smooth" });
}

loadTableRows()