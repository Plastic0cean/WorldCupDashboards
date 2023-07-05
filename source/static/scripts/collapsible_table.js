document.addEventListener("DOMContentLoaded", function() {
    const expandableRows = document.querySelectorAll(".expand");

    expandableRows.forEach(function(row) {
        row.addEventListener("click", function() {
            const expandedRow = this.parentNode.nextElementSibling;

            if (expandedRow.classList.contains("hidden")) {
                expandedRow.classList.remove("hidden");
                this.classList.add("collapsed");
            } else {
                expandedRow.classList.add("hidden");
                this.classList.remove("collapsed");
            }
        });
    });
});
