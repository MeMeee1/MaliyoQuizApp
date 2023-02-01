window.onpopstate = function() {
  selectedOption.disabled = false;
  totalScore = 0;
  localStorage.removeItem("totalScore");
};
var url = "http://127.0.0.1:8000/newquiz/";
console.log(url);

var progressBar = document.getElementById("progress-bar");
var totalQuestions = parseInt(progressBar.getAttribute("total-questions"));
var currentQuestion = localStorage.getItem("currentQuestion") || 0;
optionButtons = document.getElementsByClassName("btn-option");
nextBtn = document.getElementById("nextBtn");
nextBtn.disabled = true;
console.log(optionButtons);

let selectedOption = null;

let totalScore = localStorage.getItem("totalScore") || 0;

document.getElementById("fill").style.width = ((localStorage.getItem("currentQuestion")) / totalQuestions * 100) + "%";
  
Array.from(optionButtons).forEach((element) => {
  var pk = element.getAttribute("data-pk");
  url = "http://127.0.0.1:8000/newquiz/" + pk[0] + "/save/";
  console.log(url);
  console.log(pk);
  element.addEventListener("click", (e) => {
    
    Array.from(optionButtons).forEach((element) => {
      element.disabled = true;
      nextBtn.disabled = false;
      
    });
    if (element.getAttribute("data-correct") === "True") {
      selectedOption = element;
      totalScore++;
      localStorage.setItem("totalScore", totalScore);
      
    } else {
      selectedOption = null;
      
    }
    currentQuestion++;
    localStorage.setItem("currentQuestion", currentQuestion);
    document.getElementById("fill").style.width = ((localStorage.getItem("currentQuestion")) / totalQuestions * 100) + "%";
  
  });
});

nextBtn.addEventListener("click", () => {
  
  if (
    selectedOption &&
    selectedOption.getAttribute("data-correct") === "True"
  ) {
  
    
  } 
  else {
   
  }
  /* let xhr = new XMLHttpRequest();
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      console.log(xhr.responseText);
    }
  };
  xhr.send(`score=${score}`); */
});
