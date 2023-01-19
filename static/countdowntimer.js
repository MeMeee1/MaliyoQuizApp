var timeleft = 10;
var downloadTimer = setInterval(function () {
  const storedSecondsLeft = localStorage.getItem('seconds');
  // check if you have localstorage stored
  // then override the value of secondsLeft with the localstorage
  if (storedSecondsLeft) {
    timeleft = +storedSecondsLeft;
  }
  if(timeleft <= 5)
  {
    document.getElementById("countdown").style.color ="#d00";
  }
  
  if (timeleft <= 0) {
    clearInterval(downloadTimer);
    
    window.location.replace("https://maliyoquizapp.onrender.com/out-of-time/");
    localStorage.removeItem('seconds');
    return;
  } 
  else {
    // document.getElementById("countdown").innerHTML =
    //   timeleft + " seconds remaining";
    document.getElementById("countdown").innerHTML ="0:" + (timeleft == 0 ? "0" : "") + String(timeleft);
  }
  timeleft -= 1;
  localStorage.setItem('seconds', timeleft);
}, 1000);
 