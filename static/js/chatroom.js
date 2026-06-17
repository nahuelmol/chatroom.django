
var host = window.location.host;

const roomName 		= JSON.parse(document.getElementById('room-name').textContent);
const user_username = JSON.parse(document.getElementById('user-username').textContent);
const user_email	= JSON.parse(document.getElementById('user-email').textContent);

input = document.querySelector('#input');

const chatSocket 	= new WebSocket('ws://'+ host + '/ws/chat/'+ roomName + '/');

const notificationSocket = new WebSocket('ws://' + host + '/ws/notifications/');

chatSocket.onopen = function() {
    console.log("CHAT WEBSOCKET OPEN")
}

chatSocket.onclose = function(e) {
    console.log("CHAT WEBSOCKET CLOSED", e)
}

chatSocket.onopen = function() {
    console.log("NOTIFICATIONS WEBSOCKET OPEN")
}

chatSocket.onclose = function(e) {
    console.log("NOTIFICATIONS WEBSOCKET CLOSED", e)
}


input.addEventListener("keyup", function(event) { //cada vez que hay un keyup en el input
    if (event.keyCode === 13) { //enter tiene codigo 13
        const messageInputDom 	= document.querySelector('#input');
        const message = messageInputDom.value;

        chatSocket.send(JSON.stringify({
            'message':message,
            'username':user_username,
            'email':user_email
        }));
        messageInputDom.value = '';
    }
});

document.querySelector('#submit').onclick = function (e) {
    const messageInputDom 	= document.querySelector('#input');
    const message 			= messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message':message,
        'username':user_username,
        'email':user_email
    }));
    messageInputDom.value = '';
}

var followbtn = document.querySelector('#follwbtn')
if (followbtn){
    followbtn.onclick = function (e) {
        console.log('hello')
    }
}

var submitban = document.querySelector('#submitban');
if (submitban) {
    submitban.onclick = function (e) {
        const input = document.querySelector('#usertoban');
        const usertoban = input.value;

        chatSocket.send(JSON.stringify({
            'message':'@ban',
            'username':usertoban,
            'email':user_email
        }))

        input.value = '';
    }
}

var submitmod = document.querySelector('#submitmod')
if (submitmod) {
    submitmod.onclick = function (e) {
        const input = document.querySelector('#usertomod');
        const usertomod = input.value;

        chatSocket.send(JSON.stringify({
            'message':'@mod',
            'username':usertomod,
            'email':user_email
        }))

        input.value = '';
    }
}

chatSocket.onmessage = function (e){
    const data 		= JSON.parse(e.data);
    if(data.hasOwnProperty('tester')){
        console.log("Welcome!")
        var prove = "<p>Hola, " + data.tester +"</p>"
        document.getElementById('handlebar1').innerHTML = prove;
    }

    if (data.hasOwnProperty('type')) {
        console.log('type detected:' + data.type);
    }

    switch(data.type) {
        case 'game_noti':
            resp = data.message_to_group
            document.getElementById('handlebar1').innerHTML = resp;
            break;
        case 'word_suggest': {
            let username 	= '\n'+data.user_username_ + ' suggested'
            document.querySelector('#chat-text').value 		+= (data.message_to_group);
            break;
        }
        case 'banned': {
            let username 	= '\n'+data.user_username_ + ' banned'
            document.querySelector('#chat-text').value 		+= (data.message_to_group);
            break;
        }
        case 'modded': {
            let username 	= '\n'+data.user_username_ + ' moderator'
            document.querySelector('#chat-text').value 		+= (data.message_to_group);
            break;
        }
        case 'chat_msg': {
            role = '';
            let msg_element = document.createElement("div");
            msg_element.className = "message";
            msg_element.style.margin = "5";

            let usr_element = document.createElement("p");
            let txt_element = document.createElement("p");
            let tme_element = document.createElement("p");
            usr_element.style.margin = "0";
            txt_element.style.margin = "0";
            tme_element.style.margin = "0";
            usr_element.textContent = data.username;
            txt_element.textContent = data.message;
            tme_element.textContent = data.time;

            msg_element.appendChild(usr_element);
            msg_element.appendChild(txt_element);
            msg_element.appendChild(tme_element);

            document.querySelector('#chattext-2').appendChild(msg_element);

            //  document.querySelector('#chattext-2').innerHTML	+= (
            //  '<p><br>'+username+role+
            //  '<br>'+data.message+
            //  '<br>'+data.time+'<br></p>');

            //document.querySelector('#chattext-2').scrollTop = document.querySelector('#chattext-2').scrollHeight;
            
            break;
        }
    }

    if(data.hasOwnProperty('state')){
        document.getElementById('handlebar1').innerHTML = data.state;
    }
}

const requesting_to_back = (url, usuario) => {
    var chat = '{{ room__name }}'
    console.log(url)
    fetch(url, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': '{{ csrf_token }}'
        },
        body: JSON.stringify(usuario)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al realizar la solicitud al backend');
        }
        return response.json();
    })
    .then(data => {
        console.log('Solicitud exitosa:', data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


var followbtn = document.querySelector('#followbtn');

if(followbtn){
    followbtn.onclick = function (e) {
        var room = '{{ room__name|urlencode }}';
        var usuario = { id: '{{ user.id }}', username: '{{ user.username}}'};
        var url = "{% url 'chatapi:followers' name='placeholder' %}".replace('placeholder', room);
        requesting_to_back(url, usuario)  		

    }
}

var subsbtn = document.querySelector('#subsbtn');
if(subsbtn) {
    subsbtn.onclick = function (e) {
        var room = '{{ room__name|urlencode }}'
        var usuario = { id: '{{ user.id }}', username: '{{ user.username}}'};
        var url = "{% url 'chatapi:subs' name='placeholder' %}".replace('placeholder', room);
        requesting_to_back(url, usuario) 
    }
}

$(document).ready(function() {
    var scrollableDiv = document.getElementById("scrollableDiv");
    if(scrollableDiv){
        scrollableDiv.scrollTop = scrollableDiv.scrollHeight;
    }
});

