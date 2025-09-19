from mistralai import Mistral
import os

# Initialize client with your API key
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
api_key = MISTRAL_API_KEY
model = "mistral-small-latest"  # Supports tool calling
client = Mistral(api_key=api_key)

# Define tools (functions)
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the weather for a location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city, e.g., San Francisco",
                    }
                },
                "required": ["location"],
            },
        },
    }
]

# User message
messages = [{"role": "user", "content": "What's the weather in Hangzhou?"}]
print("Initial user message:", messages)

# First API call: Model decides if tool is needed
print("Making first API call to determine tool usage...")
response = client.chat.complete(
    model=model,
    messages=messages,
    tools=tools,
    tool_choice="auto",  # Auto-decides tool use
)
print("First API response received:", response.choices[0].message)

# Check for tool calls
tool_calls = response.choices[0].message.tool_calls
if tool_calls:
    print("Tool call detected:", tool_calls)
    # Append the model's response to messages
    messages.append(response.choices[0].message)
    print("Updated messages with model response:", messages)

    # Simulate executing the tool (in real code, call an actual API)
    tool_call = tool_calls[0]
    if tool_call.function.name == "get_weather":
        location = eval(tool_call.function.arguments)["location"]
        weather_result = "24°C and sunny"  # Replace with real function call
        print(f"Simulated weather result for {location}: {weather_result}")

        # Append tool result
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_call.function.name,
                "content": weather_result,
            }
        )
        print("Updated messages with tool result:", messages)

    # Second API call: Model generates final response
    print("Making second API call for final response...")
    final_response = client.chat.complete(model=model, messages=messages)
    print("Final response received:", final_response.choices[0].message.content)
else:
    print("No tool call needed. Direct response:", response.choices[0].message.content)
