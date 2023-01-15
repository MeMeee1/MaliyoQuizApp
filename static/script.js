"use strict";
let currentQ = 1;
const nextBtn = '<button type="button" class="next animated bounceInLeft">Next</button>';
var circle = new ProgressBar.Circle('#circle-container', {
	duration: 200,
	strokeWidth: 5,
	trailWidth: 5,
	trailColor: "#ddd",
	from: {
		color: '#218CCC'
	},
	to: {
		color: '#047E3C'
	},
	step: function(state, circle) {
		circle.path.setAttribute('stroke', state.color);
	}
});
var arrQ = $(".q");
for(var cpt = 0; cpt<= arrQ.length; cpt++){
	if(cpt>=1) $(arrQ[cpt]).addClass("disabled");
}
$(".btnQ").on('click',function(e){
	if(!$(".q"+currentQ+" .button-space .next").length){
		$(".q"+currentQ+" .button-space").append(nextBtn);
		$(".next").on("click", changeQ);
	}
});
function changeQ(){
	circle.animate((currentQ)/arrQ.length);
	$(".q"+currentQ).addClass("animated fadeOutDown");
	setTimeout(function(){
		$(".q"+currentQ).removeClass("animated fadeOutDown");
		$(".q"+currentQ).addClass("disabled");
		currentQ = currentQ + 1;
		setNewQ();
	}, 1000);
}
function setNewQ(){
	if(currentQ>arrQ.length){
		$(".quiz").append('<div class="end animated bounceInDown">Thanks for sharing...</div>');
	}
	else{
		$(".q"+currentQ).removeClass("disabled");
		$(".q"+currentQ).addClass("animated fadeInDown");
	}
}