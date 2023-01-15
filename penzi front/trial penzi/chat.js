// message input
const textarea = document.querySelector('.chatbox-message-input')
const chatboxForm = document.querySelector('.chatbox-message-form')

textarea.addEventListener('input', function () {
    let line = textarea.value.split('\n').length

    if (textarea.rows < 6 || line < 6) {
        textarea.rows = line
    }
    if (textarea.row > 1) {
        chatboxForm.style.alignItems = 'flex-end'
    } else {
        chatboxForm.style.alignItems = 'center'
    }
})

// toggle chatbox
const chatboxToggle = document.querySelector('.chatbox-toggle')
const chatboxMessage = document.querySelector('.chatbox-message-wrapper')

chatboxToggle.addEventListener('click', function () {
    chatboxMessage.classList.toggle('show')
})

// dropdown toggle
const dropdownToggle = document.querySelector('.chatbox-message-dropdown-toggle')
const dropdownMenu = document.querySelector('.chatbox-message-dropdown-menu')

dropdownToggle.addEventListener('click', function () {
    dropdownMenu.classList.toggle('show')
})

document.addEventListener('click', function (e) {
    if (!e.target.matches('.chatbox-message-dropdown, .chatbox-message-dropdown *')) {
        dropdownMenu.classList.remove('show')
    }
})


// chatbox message
const chatboxMessagewrapper = document.querySelector('.chatbox-message-content')
const chatboxNoMessage = document.querySelector('.chatbox-message-no-messages')

chatboxForm.addEventListener('submit', function (e) {
    e.preventDefault()
    if (isValid(textarea.value)) {
        WriteMessage()
        setTimeout(Autoreply, 1000)
    }

})

function addZero(num) {
    return num < 10 ? '0' + num : num
}

function WriteMessage() {

    const today = new Date()
    let message = `
    <div class="chatbox-message-item sent">
        <span class="chatbox-message-item-text">
            ${textarea.value.trim().replace(/\n/g, '<br>\n')}
        </span>
        <span class="chatbox-message-item-time">${addZero(today.getHours())}:${addZero(today.getMinutes())}</span>
    </div>
    `
    chatboxMessagewrapper.insertAdjacentHTML('beforeend', message)
    chatboxForm.style.alignItems = 'center'
    textarea.row = 1
    textarea.focus()
    textarea.value = ''
    chatboxNoMessage.style.display = 'none'
    scrollBottom()
}

var counter = 1

// function Autoreply() {
//     const today = new Date()
//     let message = `
//     <div class="chatbox-message-item received">
//         <span class="chatbox-message-item-text">
//             Thank you for contacting us!!!
//         </span>
//         <span class="chatbox-message-item-time">${addZero(today.getHours())}:${addZero(today.getMinutes())}</span>
//     </div>
//     `
//     chatboxMessagewrapper.insertAdjacentHTML('beforeend', message)
//     scrollBottom()

//     // switch on counter
//     // make API call
//     // increment counter if succesful
//     // Get response and write resonse

// }

function scrollBottom() {
    chatboxMessagewrapper.scrollTo(0, chatboxMessagewrapper.scrollHeight)
}

function isValid(value) {
    let text = value.replace(/\n/g, '')
    text = text.replace(/\s/g, '')
    return text.length > 0

}

    function Autoreply() {
    const today = new Date()
    async function postData(url = '', data = {}) {
        const myHeaders = new Headers();
        myHeaders.append('Content-Type', 'application/json');

        const response = await fetch(url, {
            method: 'POST',
            headers: myHeaders,
            body: JSON.stringify(data)
        });

        const res = await response.json()

        chatboxMessagewrapper.insertAdjacentHTML('beforeend', res)
        scrollBottom()
    }
    postData('http://127.0.0.1:5000/send')
    }

   
        // switch on counter
        // make API call
        // increment counter if succesful
        // Get response and write resonse

