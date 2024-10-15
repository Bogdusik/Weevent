"use strict"

var coll = document.getElementsByClassName("collapsible");

for (var i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");

    var content = this.nextElementSibling;

    if (content.style.maxHeight) {
      // Collapse the section
      content.style.maxHeight = null;
    } else {
      // Expand the section
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
}
