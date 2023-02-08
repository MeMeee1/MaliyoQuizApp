window.onpopstate = function() {
  selectedOption.disabled = false;
  totalScore = 0;
  localStorage.removeItem("totalScore");
};
var url = "http://127.0.0.1:8000/newquiz/";

var progressBar = document.getElementById("progress-bar");
var totalQuestions = parseInt(progressBar.getAttribute("total-questions"));
var currentQuestion = localStorage.getItem("currentQuestion") || 0;
optionButtons = document.getElementsByClassName("btn-option");


let selectedOption = null;
let questions=localStorage.getItem("questions") || 1;
console.log(questions)
let totalScore = localStorage.getItem("totalScore") || 0;

document.getElementById("fill").style.width = ((localStorage.getItem("currentQuestion")) / totalQuestions * 100) + "%";
document.getElementById("showQuestion").innerHTML=`${questions}/${totalQuestions}`; 
Array.from(optionButtons).forEach((element) => {
  var pk = element.getAttribute("data-pk");
  url = "http://127.0.0.1:8000/newquiz/" + pk[0] + "/save/";
  
  element.addEventListener("click", (e) => {
    
    Array.from(optionButtons).forEach((element) => {
      element.disabled = true;
     
      
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
    questions++;
    localStorage.setItem("questions", questions);
    document.getElementById("fill").style.width = ((localStorage.getItem("currentQuestion")) / totalQuestions * 100) + "%";
  
  });
 
    console.log(questions);
    
    document.getElementById("showQuestion").innerHTML=`${questions}/${totalQuestions}`;
});

