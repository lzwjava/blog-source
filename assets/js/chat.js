// ---
// audio: false
// lang: en
// layout: post
// title: Chat With My Blog
// translated: false
// ---

// <script async src="assets/js/chat.js"></script>
// <div class="chat"></div>

let marked;

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

    // Load marked.js only when needed
    if (typeof marked === 'undefined') {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/marked/marked.min.js';
        script.onload = () => {
            marked = window.marked;
            sendButton.addEventListener('click', () => {
                sendMessage(inputElement.value, messageContainer);
                inputElement.value = '';
            });
        };
        document.head.appendChild(script);
    } else {
        sendButton.addEventListener('click', () => {
            sendMessage(inputElement.value, messageContainer);
            inputElement.value = '';
        });
    }
} else {
    console.error("Chat div not found!");
}

async function sendMessage(message, messageContainer) {
    if (message.trim() !== '') {
        addUserMessage(message, messageContainer);
        try {
            // const botResponse = await callOllamaAPI(message);
            // addBotMessage(botResponse, messageContainer);
            await callOllamaAPI(message, messageContainer);
        } catch (error) {
            console.error('Error:', error);
            addBotMessage('Error: Could not communicate with the bot.', messageContainer);
        }
    }
}

function addUserMessage(message, messageContainer) {
    const userMessage = document.createElement('div');
    userMessage.innerHTML = marked ? marked.parse(`You: ${message}`) : `You: ${message}`;
    messageContainer.prepend(userMessage); // Add to the top
}

function addBotMessage(message, messageContainer) {
    const botMessage = document.createElement('div');
    botMessage.innerHTML = marked ? marked.parse(`Bot: ${message}`) : `Bot: ${message}`;
    messageContainer.prepend(botMessage); // Add to the top
}

async function callOllamaAPI(message, messageContainer) {
    const botMessageDiv = document.createElement('div');
    botMessageDiv.innerHTML = 'Bot: ';
    messageContainer.prepend(botMessageDiv); // Add to the top

    const response = await fetch('http://192.168.1.3:11434/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            messages: [{ role: 'user', content: message }],
            model: 'deepseek-r1:14b', // Replace with your desired model
            stream: true
        })
    });

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    try {
        while (true) {
            const { done, value } = await reader.read();

            if (done) {
                break;
            }

            const chunk = decoder.decode(value);
            // Process each chunk of data
            const lines = chunk.split('\n');

            for (const line of lines) {
                if (line.trim() === '') continue;

                try {
                    const json = JSON.parse(line);
                    if (json.choices && json.choices[0] && json.choices[0].delta && json.choices[0].delta.content) {
                        const content = json.choices[0].delta.content;
                        botMessageDiv.innerHTML += marked ? marked.parseInline(content) : content;
                    }
                } catch (error) {
                    console.error("Error parsing JSON:", error, line);
                }
            }
        }
    } catch (error) {
        console.error("Stream error:", error);
        botMessageDiv.innerHTML = 'Error: Could not retrieve response from the bot.';
    } finally {
        reader.releaseLock();
    }
}
