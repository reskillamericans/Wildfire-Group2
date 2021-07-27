let questions = document.querySelector(".accordian");
// targeting the div containing the questions

questions.addEventListener("click", (e) => {
	// event parameter captures the event
	e.target.classList.toggle("is-open");
	//event.target figures out what element within the div was clicked
	let content = e.target.nextElementSibling;
	if (content.style.maxHeight) {
		// if truthy set to falsey
		// set height value to zero or null
		content.style.maxHeight = null;
	} else {
		// if closed (falsey) set to truthy
		// Set max height === content height on screen
		content.style.maxHeight = content.scrollHeight + "px";
	};
});
