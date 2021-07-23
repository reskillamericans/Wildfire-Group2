let questions = document.getElementsByClassName("questions");
// console.log("Hello World");
for (let i = 0; i < questions.length; i++) {
	questions[i].addEventListener("click", function () {
		this.classList.toggle("is-open");
		let content = this.nextElementSibling;
		if (content.style.maxHeight) {
			// if truthy set to falsey
			// set height value to zero or null
			content.style.maxHeight = null;
		} else {
			// if closed (falsey) set to truthy
			// Set max height === content height on screen
			content.style.maxHeight = content.scrollHeight + "px";
		}
	});
}