function toggleGroup(id, button) {
    const group = document.getElementById(id);
    if (group.style.display === "none" || group.style.display === "") {
        group.style.display = "block";
        button.classList.add("active");
    } else {
        group.style.display = "none";
        button.classList.remove("active");
    }
}