// ---
// audio: false
// lang: en
// layout: post
// title: Chat With My Blog
// translated: false
// ---

// <script async src="assets/js/chat.js"></script>
// <div class="chat"></div>

const chatDiv = document.querySelector('.chat');

if (chatDiv) {
    const inputElement = document.createElement('input');
    inputElement.type = 'text';
    inputElement.placeholder = 'Type your message...';
    chatDiv.appendChild(inputElement);

    const sendButton = document.createElement('button');
    sendButton.textContent = 'Send';
    chatDiv.appendChild(sendButton);

    const messageContainer = document.createElement('div');
    chatDiv.appendChild(messageContainer);

    sendButton.addEventListener('click', () => {
        const message = inputElement.value;
        if (message.trim() !== '') {
            const userMessage = document.createElement('p');
            userMessage.textContent = `You: ${message}`;
            messageContainer.appendChild(userMessage);

            const botMessage = document.createElement('p');
            botMessage.textContent = `Bot: hi`;
            messageContainer.appendChild(botMessage);

            inputElement.value = '';
        }
    });
} else {
    console.error("Chat div not found!");
}
