window.onpopstate = function() {
  history.pushState(null, null, location.href);
  window.location.replace("/new-page");
};

score = document.getElementById("scoreCard");
score_to_pass = parseInt(score.getAttribute("score-pass"))
var total = (localStorage.getItem("totalScore")/score_to_pass)*100
score.innerHTML=`Score: ${total}`;
imageDisplay = document.getElementById("imageSpace")
if(total>59 && total<=100)
{
  imageDisplay.innerHTML=`<img src="https://usagif.com/wp-content/uploads/gif/heart-eyes-10.gif.webp" alt="this slowpoke moves"  width="100" />`;

  
}
else if(total>49 && total<=59)
{
  imageDisplay.innerHTML=`<img src="https://media.giphy.com/media/dalJ0CpF7hwmN1nZXe/giphy.gif" alt="this slowpoke moves"  width="100" />`;

}
else if(total>=0 && total<=49)
{ 
  imageDisplay.innerHTML=`<img src="https://usagif.com/wp-content/uploads/2022/4hv9xm/crying-emoji-9.gif.webp" alt="this slowpoke moves"  width="100" />`;

}
document.getElementById("filled").style.width = `${total}%`;

homeBtn = document.getElementById("home");
homeBtn.addEventListener("click", () => {
  localStorage.removeItem("seconds");
  localStorage.removeItem("totalScore");
  localStorage.removeItem("currentQuestion")
});
