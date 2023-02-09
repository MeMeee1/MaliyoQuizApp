optionButtons = document.getElementsByClassName("btn-option");
var timeleft = 60;
var downloadTimer = setInterval(function () {
  const storedSecondsLeft = localStorage.getItem("seconds");
  // check if you have localstorage stored
  // then override the value of secondsLeft with the localstorage
  if (storedSecondsLeft) {
    timeleft = +storedSecondsLeft;
  }
  if (timeleft <= 5) {
    document.getElementById("timer-box").style.color = "#d00";
  }
  if (timeleft <= 0) {
    clearInterval(downloadTimer);
    Array.from(optionButtons).forEach((element) => {
      var pk = element.getAttribute("data-pk");
      window.location.replace("/newquiz/" + pk[0] + "/thanks");
    });
    localStorage.removeItem('seconds');
    return;
    
    
  } else {
    // document.getElementById("countdown").innerHTML =
    //   timeleft + " seconds remaining";
    document.getElementById("timer-box").innerHTML =
      "0:" + (timeleft == 0 ? "0" : "") + String(timeleft);
  }
  timeleft -= 1;
  localStorage.setItem("seconds", timeleft);
}, 1000);

var loadFunction = function () {
  document.getElementById("main").style.visibility = "visible";
  document.getElementById("loader").style.display = "none";
};

window.onload = function () {
  setTimeout(loadFunction, 3000);
};
