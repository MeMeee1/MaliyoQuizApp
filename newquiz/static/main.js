console.log('hello world')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML = `
        <div class="h5 mb-3">Are you sure you want to begin "<b>${name}</b>"?</div>
        <hr>
        <div class="h5 mb-3 text-center"><b>Question stats</b></div>
        <div class="h5 mb-1 text-center">Difficulty: <b>${difficulty}</b></div>
        <div class="h5 mb-1 text-center">Number of questions: <b>${numQuestions}</b></div>
        <div class="h5 mb-1 text-center">Score to pass: <b>${scoreToPass}%</b></div>
        <div class="h5 mb-1 text-center">Time: <b>${time} min</b></div>
        
        
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}))
