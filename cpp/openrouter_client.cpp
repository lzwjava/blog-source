#include <iostream>
#include <string>
#include <cpprest/http_client.h>
#include <cpprest/json.h>
#include <map>
#include <stdexcept>

using namespace web;
using namespace web::http;
using namespace web::http::client;
using namespace web::json;

// Function to get environment variable
std::string get_env_var(const std::string& name) {
    const char* value = std::getenv(name.c_str());
    return value ? std::string(value) : std::string();
}

// Model mapping similar to Python dictionary
std::map<std::string, std::string> MODEL_MAPPING = {
    {"claude-opus", "anthropic/claude-opus-4"},
    {"claude-sonnet", "anthropic/claude-sonnet-4"},
    {"gemini-flash", "google/gemini-2.5-flash"},
    {"deepseek-v3", "deepseek/deepseek-chat-v3-0324:free"},
    {"gemini-pro", "google/gemini-2.5-pro"},
    {"kimi-k2", "moonshotai/kimi-k2:free"}
};

std::string call_openrouter_api(const std::string& prompt, const std::string& model = "deepseek-v3") {
    std::string api_key = get_env_var("OPENROUTER_API_KEY");
    if (api_key.empty()) {
        throw std::runtime_error("API key not found in environment variables");
    }

    // Check if model exists in mapping
    if (MODEL_MAPPING.find(model) == MODEL_MAPPING.end()) {
        throw std::runtime_error("Model '" + model + "' not found in MODEL_MAPPING");
    }

    // Prepare JSON payload
    value data;
    data[U("model")] = value::string(MODEL_MAPPING.at(model));
    value messages_array = value::array();
    value message;
    message[U("role")] = value::string(U("user"));
    message[U("content")] = value::string(prompt);
    messages_array[0] = message;
    data[U("messages")] = messages_array;

    // Set up HTTP client and request
    http_client client(U("https://openrouter.ai/api/v1"));
    http_request request(methods::POST);
    request.set_request_uri(U("/chat/completions"));
    request.headers().add(U("Authorization"), U("Bearer ") + utility::conversions::to_string_t(api_key));
    request.headers().add(U("Content-Type"), U("application/json"));
    request.set_body(data);

    // Send request and handle response
    try {
        http_response response = client.request(request).get();
        if (response.status_code() == status_codes::OK) {
            value json_response = response.extract_json().get();
            return json_response[U("choices")][0][U("message")][U("content")].as_string();
        } else {
            throw std::runtime_error("Error: " + std::to_string(response.status_code()) + " - " + response.extract_string().get());
        }
    } catch (const std::exception& e) {
        throw std::runtime_error("An error occurred: " + std::string(e.what()));
    }
}

int main() {
    try {
        std::string result = call_openrouter_api("Hello, can you help me with a simple query?", "deepseek-v3");
        std::cout << "Response from OpenRouter:" << std::endl;
        std::cout << result << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
