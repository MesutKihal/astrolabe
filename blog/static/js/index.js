
const mthBlock = document.getElementById("mth-block")
const phyBlock = document.getElementById("phy-block")
const emptySpace = document.getElementById("empty-space");
const mainbar = document.getElementById("mainbar");
const navbar = document.getElementById("navbar");
const logo = document.getElementById("logo");
const Levels = document.getElementsByName("Levels");

if (screen.width < 600)
{
	mthBlock.setAttribute("class", "w-5");
	phyBlock.setAttribute("class", "w-5");
	emptySpace.remove()
	mainbar.classList.remove("wrap");
	mainbar.classList.add("rows");
	navbar.classList.remove("w-4");
	navbar.classList.add("w-10");
	logo.classList.remove("w-1");
	logo.classList.remove("w-4");
}


Levels.forEach(lvl => {
	lvl.onclick = (event) => {
		getContent(lvl.dataset.id);
	}
})



function getContent(id)
{
	window.location.replace(`exer/${id}`);
	console.log(id);
}