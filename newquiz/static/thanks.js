window.onpopstate = function() {
  history.pushState(null, null, location.href);
  window.location.replace("/new-page");
};

score = document.getElementById("scoreCard");
score_to_pass = parseInt(score.getAttribute("score-pass"))
var total = (localStorage.getItem("totalScore")/score_to_pass)*100
score.innerHTML=`Score: ${total}`;
imageDisplay = document.getElementById("imageSpace")
if(total>=60 && total<=100)
{
  imageDisplay.innerHTML=`<img src="https://media.tenor.com/a1VADuLpJLQAAAAi/%E3%81%8A%E3%82%81%E3%81%A7%E3%81%A8%E3%81%86-%E3%81%8A%E7%A5%9D%E3%81%84.gif" alt="this slowpoke moves"  width="100" />`;

  
}
else if(total>=50 && total<=59)
{
  imageDisplay.innerHTML=`<img src="https://media.giphy.com/media/dalJ0CpF7hwmN1nZXe/giphy.gif" alt="this slowpoke moves"  width="100" />`;

}
else if(total>=0 && total<=49)
{ 
  imageDisplay.innerHTML=`<img src="https://media.tenor.com/uiGdXpO3wosAAAAi/sad-gif.gif" width="100" />`;

}
document.getElementById("filled").style.width = `${total}%`;

homeBtn = document.getElementById("home");
homeBtn.addEventListener("click", () => {
  localStorage.removeItem("seconds");
  localStorage.removeItem("totalScore");
  localStorage.removeItem("currentQuestion")
});
