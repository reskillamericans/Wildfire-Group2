let currLocation = location.href;
let secondNav = document.querySelector(".top-bar").getElementsByTagName("a");

for (let link of secondNav) {
	if (link.href === currLocation) {
		link.classList.add("current");
	}
}
