let url = window.location.href;
let domain = url.replace('http://','').replace('https://','').split(/[/?#]/)[0];
const API_URL = `https://${domain}`;

async function submitQuestion() {
  // Get the users selected option
  // Get the question id
  // Get the form id
  // Extract the CSRF token
  // POST the data as content_type="form-data"
  // Go to the next question (Redirect should come from backend (HTTP 304))

  await fetch(API_URL + "/form");
}

const selectedClass = "btn-primary",
  defaultDeselectedClass = "btn-outline-primary";

let selectedOption = undefined,
  questionID,
  formID;

$("document").ready(function () {
  questionID = document.getElementById("question-id").innerText;
  formID = document.getElementById("form-id").innerText;
  optionButtons = document.getElementsByClassName("btn-option");
  Array.from(optionButtons).forEach((element) => {
    element.addEventListener("click", (e) => {
      updateSelectedOption(e.target);
    });
  });
});

function updateSelectedOption(element) {
  if (typeof selectedOption !== "undefined") {
    selectedOption.classList.remove(selectedClass);
    selectedOption.classList.add(defaultDeselectedClass);
  }

  element.classList.remove(defaultDeselectedClass);
  element.classList.add(selectedClass);
  selectedOption = element;

  const submitButton = document.getElementById("submit-btn");
  submitButton.disabled = false;
}

//Get the users selected option
function getUserResponse() {
  const data = new FormData();
  data.append("question", questionID);
  data.append("form", formID);
  data.append("selected_options", [selectedOption.id]);
  data.append("user_value", selectedOption.value);
  return data;
}

async function submitResponse() {
  userResponse = getUserResponse();
  response = await fetch(
    `${API_URL}/${formID}/question/${questionID}/`,
    (options = {
      method: "POST",
      headers: { "X-CSRFToken": getCookie("csrftoken") },
      body: userResponse,
    })
  );
  await handleFormResponse(response);
}

async function handleFormResponse(response) {
  if (response.status < 400) {
    console.log("Redirecting");
    window.location.href = response.url;
  } else {
    console.error(response);
  }
}

function getCookie(name) {
  let cookie = document.cookie.match("(^|;) ?" + name + "=([^;]*)(;|$)");
  return cookie ? cookie[2] : null;
}
