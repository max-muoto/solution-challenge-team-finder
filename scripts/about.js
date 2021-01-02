function expandOnClick() {
    var more = document.getElementById("more");
    var btn = document.getElementById("more-btn");
    if (more.style.display === "block") {
      more.style.display = "none";
      btn.innerHTML = "Show more";
    } else {
      more.style.display = "block";
      btn.innerHTML = "Show less";
    }
}