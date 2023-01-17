API_URL = "https://localhost:8000"
async function submitQuestion(){
    // Get the users selected option
    // Get the question id
    // Get the form id
    // Extract the CSRF token
    // POST the data as content_type="form-data"
    // Go to the next question (Redirect should come from backend (HTTP 304))


    await fetch(
        API_URL + "/form"
    )
}

//Get the users selected option
function displayRadioValue() {
    var ele = document.getElementsByName("btnQ");
    console.log(ele);
    for(i = 0; i < ele.length; i++) {
        if(ele[i].checked)
            console.log("true");
    }
}