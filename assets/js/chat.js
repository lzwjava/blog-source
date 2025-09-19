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
    const messageContainer = document.createElement('div');
    chatDiv.appendChild(messageContainer);

    const inputElement = document.createElement('input');
    inputElement.type = 'text';
    inputElement.placeholder = 'Type your message...';
    chatDiv.appendChild(inputElement);

    const sendButton = document.createElement('button');
    sendButton.textContent = 'Send';
    chatDiv.appendChild(sendButton);


    // Load marked.js only when needed
    const loadMarked = () => {
        if (window.marked) {
            marked = window.marked;
        } else {
            console.error('marked.js not found!');
            alert('marked.js not found! Markdown formatting will not be applied.');
            return;
        }
        sendButton.addEventListener('click', () => {
            sendMessage(inputElement.value, messageContainer);
            inputElement.value = '';
        });
    };

    if (typeof marked === 'undefined') {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/marked/marked.min.js';
        script.onload = loadMarked;
        script.onerror = () => {
            console.error('Failed to load marked.js.');
            alert('Failed to load marked.js. Markdown formatting will not be applied.');
        };
        document.head.appendChild(script);
    } else {
        loadMarked();
    }
} else {
    console.error("Chat div not found!");
}

async function sendMessage(message, messageContainer) {
    if (message.trim() !== '') {
        addUserMessage(message, messageContainer);
        try {
            await callOllamaAPI(message, messageContainer);
        } catch (error) {
            console.error('Error:', error);
            addBotMessage(`Error: Could not communicate with the bot. ${error}`, messageContainer);
        }
    }
}

function addUserMessage(message, messageContainer) {
    const userMessage = document.createElement('div');
    userMessage.classList.add('user-message'); // Add class for styling
    userMessage.innerHTML = marked ? marked.parse(`You: ${message}`) : `You: ${message}`;
    messageContainer.appendChild(userMessage);
}

function addBotMessage(message, messageContainer) {
    const botMessage = document.createElement('div');
    botMessage.classList.add('bot-message'); // Add class for styling
    botMessage.innerHTML = marked ? marked.parse(`Bot: ${message}`) : `Bot: ${message}`;
    messageContainer.appendChild(botMessage);
}

async function callOllamaAPI(message, messageContainer) {
    const botMessageDiv = document.createElement('div');
    botMessageDiv.classList.add('bot-message'); // Add class for styling
    botMessageDiv.innerHTML = 'Bot: ';
    messageContainer.appendChild(botMessageDiv);

    let accumulatedResponse = ''; // Accumulate the response for potential error handling
    let reader; // Declare reader outside the try block

    try {
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

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`HTTP error! status: ${response.status}, body: ${errorText}`);
        }

        reader = response.body.getReader();
        const decoder = new TextDecoder();

        while (true) {
            const { done, value } = await reader.read();

            if (done) {
                break;
            }

            const chunk = decoder.decode(value);
            const jsonStrings = chunk.split('data:').filter(str => str.trim() !== '');

            for (const jsonString of jsonStrings) {
                if (jsonString.trim() === '[DONE]') {
                    break;
                }

                try {
                    const json = JSON.parse(jsonString);
                    if (json.choices && json.choices[0] && json.choices[0].delta && json.choices[0].delta.content) {
                        const content = json.choices[0].delta.content;
                        accumulatedResponse += content;
                        // Split the content into lines and format each line
                        const lines = accumulatedResponse.split('\n');
                        let formattedResponse = '';
                        for (const line of lines) {
                            formattedResponse += (marked ? marked.parseInline(line) : line) + '<br>';
                        }
                        botMessageDiv.innerHTML = 'Bot: ' + formattedResponse;
                    }
                } catch (error) {
                    console.error("Error parsing JSON:", error, jsonString);
                    botMessageDiv.innerHTML = 'Bot: Error parsing response.';
                    return; // Exit the function on a parsing error
                }
            }
        }
    } catch (error) {
        console.error("Stream error:", error);
        botMessageDiv.innerHTML = `Bot: Error: Could not retrieve response from the bot. ${error}`;
    } finally {
        if (reader) {
            if (reader.releaseLock) {
                reader.releaseLock();
            }
        }
    }
}
