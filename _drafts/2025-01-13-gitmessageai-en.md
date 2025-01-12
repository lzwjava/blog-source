---
audio: true
lang: en
layout: post
title: gitmessageai
---

```bash
function gitmessageai {
  # Stage all changes
  git add -A

  # Get the diff of staged changes
  local diff=$(git diff --staged)

  # Prepare the prompt for the AI
  local prompt="Generate a concise and meaningful commit message for the following code changes:\n\n$diff"

  # Send the prompt to the DeepSeek API
  local response=$(curl -s -X POST https://api.deepseek.com/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
    -d "{
          \"model\": \"deepseek-chat\",
          \"messages\": [
            {
              \"role\": \"user\",
              \"content\": \"${prompt}\"
            }
          ],
          \"max_tokens\": 100
        }")

  # Extract the generated commit message from the API response
  local commit_message=$(echo $response | jq -r '.choices[0].message.content' | xargs)

  # Commit with the generated message
  git commit -m "$commit_message"

  # Push the changes
  git push
}
```