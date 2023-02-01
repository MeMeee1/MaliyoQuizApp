
const startBtn = document.getElementById("startbutton");
const pk = startBtn.getAttribute("data-pk");
window.onpopstate = function() {
  history.pushState(null, null, location.href);
  window.location.replace("/newquiz/" + pk + "/");
};
startBtn.addEventListener("click", () => {
  localStorage.removeItem("seconds");
  localStorage.removeItem("totalScore");
  localStorage.removeItem("currentQuestion")
  window.location.replace("/newquiz/" + pk + "/");
});


