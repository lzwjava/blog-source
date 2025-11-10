---
audio: false
generated: true
lang: hi
layout: post
title: एपीआई में एआई टूल के उपयोग की व्याख्या
translated: true
type: note
---

### AI API में टूल यूज़ क्या है?

टूल यूज़, जिसे अक्सर "टूल कॉलिंग" या "फंक्शन कॉलिंग" कहा जाता है, AI API में एक ऐसी सुविधा है जो बड़े लैंग्वेज मॉडल (LLM) को बाहरी टूल, फ़ंक्शन, या API के साथ इंटरैक्ट करने की अनुमति देती है। केवल अपने आंतरिक ज्ञान के आधार पर प्रतिक्रियाएं उत्पन्न करने के बजाय, मॉडल रीयल-टाइम डेटा प्राप्त करने, गणना करने, या कार्यों को निष्पादित करने के लिए पूर्वनिर्धारित फ़ंक्शन को कॉल करने का निर्णय ले सकता है। यह AI को मौसम की जानकारी प्राप्त करने, डेटाबेस खोजने, या अन्य सेवाओं के साथ एकीकरण जैसे कार्यों के लिए अधिक गतिशील और उपयोगी बनाता है।

यह प्रक्रिया आमतौर पर इस तरह काम करती है:
- आप JSON फॉर्मेट में विवरण और पैरामीटर के साथ टूल (फ़ंक्शन) को परिभाषित करते हैं।
- मॉडल उपयोगकर्ता के क्वेरी का विश्लेषण करता है और, यदि आवश्यक हो, फ़ंक्शन नाम और तर्कों के साथ एक "टूल कॉल" आउटपुट करता है।
- आपका एप्लिकेशन फ़ंक्शन को निष्पादित करता है और परिणाम को वापस मॉडल को फीड करता है।
- मॉडल फिर टूल के आउटपुट को शामिल करते हुए एक अंतिम प्रतिक्रिया उत्पन्न करता है।

यह आमतौर पर OpenAI के फंक्शन कॉलिंग API से प्रेरित है, और Mistral और DeepSeek जैसे कई प्रदाता संगत कार्यान्वयन का समर्थन करते हैं।

### टूल यूज़ के लिए Mistral या DeepSeek?

Mistral AI और DeepSeek AI दोनों अपने API में टूल कॉलिंग का समर्थन करते हैं, जिससे वे एजेंट या ऐसे एप्लिकेशन बनाने के लिए उपयुक्त होते हैं जिन्हें बाहरी एकीकरण की आवश्यकता होती है। उपलब्ध जानकारी के आधार पर यहां एक त्वरित तुलना दी गई है:

- **टूल यूज़ के लिए समर्थन**:
  - दोनों OpenAI के API के समान संरचना का पालन करते हैं, जो JSON स्कीमा के माध्यम से टूल के साथ आसान एकीकरण की अनुमति देते हैं।
  - Mistral इसका समर्थन Mistral Large और Medium जैसे मॉडलों में करता है, जिसमें एजेंट-आधारित वर्कफ़्लो के लिए विकल्प होते हैं।
  - DeepSeek मुख्य रूप से अपने "deepseek-chat" मॉडल के माध्यम से इसका समर्थन करता है और OpenAI के SDK के साथ पूरी तरह से संगत है।

- **फायदे और नुकसान**:
  - **Mistral**: सामान्य कार्यों के लिए अधिक बहुमुखी, कुछ बेंचमार्क में तेज़ अनुमान, और यूरोपीय डेटा गोपनीयता आवश्यकताओं के लिए बेहतर अनुकूल। यह त्वरित प्रतिक्रियाओं में उत्कृष्ट प्रदर्शन करता है और इसकी मजबूत बहुभाषी क्षमताएं हैं। हालाँकि, यह अधिक महंगा हो सकता है (उदाहरण के लिए, DeepSeek की तुलना में इनपुट/आउटपुट लागत अधिक है)।
  - **DeepSeek**: काफी सस्ता (कुछ तुलनाओं में 28 गुना तक कम लागत), गणित, कोडिंग और तर्क कार्यों में मजबूत। यह बजट-सचेत उपयोगकर्ताओं या उच्च-वॉल्यूम उपयोग के लिए आदर्श है। कमियों में गैर-तकनीकी कार्यों में संभावित रूप से धीमा प्रदर्शन और मल्टीमॉडल सुविधाओं पर कम जोर शामिल है।
  - **किसे चुनें?** यदि लागत प्राथमिकता है और आपके उपयोग के मामले में कोडिंग/गणित के साथ टूल शामिल हैं, तो DeepSeek को चुनें। व्यापक अनुप्रयोगों, तेज प्रतिक्रियाओं, या एजेंट जैसी एंटरप्राइज़ सुविधाओं के लिए, Mistral बेहतर है। दोनों ओपन-सोर्स अनुकूल और प्रदर्शनकारी हैं, लेकिन अपनी विशिष्ट आवश्यकताओं के साथ परीक्षण करें।

अंततः, टूल यूज़ के लिए कोई भी सख्ती से "बेहतर" नहीं है - दोनों अच्छी तरह से काम करते हैं। लागत बचत के लिए DeepSeek बेहतर हो सकता है, जबकि Mistral अधिक परिष्कृत एजेंट एकीकरण प्रदान करता है।

### टूल यूज़ का उपयोग कैसे करें

टूल कॉलिंग का उपयोग करने के लिए, आपको संबंधित प्रदाता (Mistral के लिए mistral.ai पर या DeepSeek के लिए platform.deepseek.com पर साइन अप करें) से एक API कुंजी की आवश्यकता होगी। दोनों OpenAI के समान Python SDK का उपयोग करते हैं। नीचे एक साधारण मौसम क्वेरी टूल के लिए चरण-दर-चरण उदाहरण दिए गए हैं।

#### Mistral AI के साथ टूल यूज़ का उपयोग करना
Mistral का API चैट कंप्लीशन के माध्यम से टूल कॉलिंग का समर्थन करता है। SDK को `pip install mistralai` के साथ इंस्टॉल करें।

**उदाहरण Python कोड** (आधिकारिक और सामुदायिक स्रोतों से अनुकूलित):
```python
from mistralai import Mistral

# Initialize client with your API key
api_key = "YOUR_MISTRAL_API_KEY"
model = "mistral-large-latest"  # Supports tool calling
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
                    "location": {"type": "string", "description": "The city, e.g., San Francisco"}
                },
                "required": ["location"]
            }
        }
    }
]

# User message
messages = [{"role": "user", "content": "What's the weather in Hangzhou?"}]

# First API call: Model decides if tool is needed
response = client.chat.complete(
    model=model,
    messages=messages,
    tools=tools,
    tool_choice="auto"  # Auto-decides tool use
)

# Check for tool calls
tool_calls = response.choices[0].message.tool_calls
if tool_calls:
    # Append the model's response to messages
    messages.append(response.choices[0].message)
    
    # Simulate executing the tool (in real code, call an actual API)
    tool_call = tool_calls[0]
    if tool_call.function.name == "get_weather":
        location = eval(tool_call.function.arguments)["location"]
        weather_result = "24°C and sunny"  # Replace with real function call
        
        # Append tool result
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_call.function.name,
            "content": weather_result
        })
    
    # Second API call: Model generates final response
    final_response = client.chat.complete(model=model, messages=messages)
    print(final_response.choices[0].message.content)
else:
    print(response.choices[0].message.content)
```

यह कोड एक क्वेरी भेजता है, टूल कॉल की जांच करता है, उसे निष्पादित करता है (यहां सिम्युलेटेड), और अंतिम उत्तर प्राप्त करता है। एजेंट-आधारित सेटअप के लिए, अधिक जटिल वर्कफ़्लो के लिए Mistral के बीटा एजेंट्स API का उपयोग करें।

#### DeepSeek AI के साथ टूल यूज़ का उपयोग करना
DeepSeek का API OpenAI-संगत है, इसलिए आप OpenAI Python SDK का उपयोग कर सकते हैं। `pip install openai` के साथ इंस्टॉल करें।

**उदाहरण Python कोड** (आधिकारिक डॉक्स से):
```python
from openai import OpenAI

# Initialize client with DeepSeek base URL and API key
client = OpenAI(
    api_key="YOUR_DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com"
)

# Define tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of a location, the user should supply a location first",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["location"]
            },
        }
    },
]

# Function to send messages
def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-chat",  # Supports tool calling
        messages=messages,
        tools=tools
    )
    return response.choices[0].message

# User message
messages = [{"role": "user", "content": "How's the weather in Hangzhou?"}]
message = send_messages(messages)
print(f"User>\t {messages[0]['content']}")

# Handle tool call
tool = message.tool_calls[0]
messages.append(message)

# Simulate tool execution (replace with real function)
messages.append({"role": "tool", "tool_call_id": tool.id, "content": "24℃"})

# Get final response
message = send_messages(messages)
print(f"Model>\t {message.content}")
```

यह समान प्रवाह का पालन करता है: क्वेरी → टूल कॉल → निष्पादित → अंतिम प्रतिक्रिया। DeepSeek संदर्भ लंबाई को सीमित करता है, इसलिए संदेशों को संक्षिप्त रखें।

उन्नत उपयोग के लिए, दर सीमा, लागत और मॉडल-विशिष्ट डॉक्स की जांच करें। अमान्य पैरामीटर जैसी त्रुटियों को संभालने के लिए सैंडबॉक्स में परीक्षण करें।

### संदर्भ
- [Mistral AI Function Calling Documentation](https://docs.mistral.ai/agents/function_calling/)
- [DeepSeek API Function Calling Guide](https://api-docs.deepseek.com/guides/function_calling)
- [Mistral AI Function Calling Example with Code](https://medium.com/@jcrsch/mistral-ai-function-calling-a-simple-example-with-code-72f3a762550f)
- [DeepSeek vs. Mistral: A Comprehensive AI Models Comparison](https://medium.com/ai-tools-tips-and-news/deepseek-vs-mistral-a-comprehensive-ai-models-comparison-f7d7b86f4b28)
- [Mistral Large vs DeepSeek-V3 Comparison](https://docsbot.ai/models/compare/mistral-large-2/deepseek-v3)