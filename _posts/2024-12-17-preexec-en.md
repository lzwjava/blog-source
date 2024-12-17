---
layout: post  
title: "Display Proxy Settings for Network Commands in Zsh"
---

Living in China or working within companies that use VPNs and proxies can complicate software development. Forgetting to configure these settings often leads to connectivity issues. To streamline your workflow, I created a simple Zsh script with the help of ChatGPT that automatically displays your proxy settings when you run specific network-dependent commands.

## **Why Display Proxy Settings?**

Proxies and VPNs are essential for accessing external resources securely. Displaying your proxy settings before executing network-dependent commands helps you quickly identify and troubleshoot connectivity issues.

## **The Script**

This script utilizes Zsh's `preexec` function to check if the upcoming command is network-dependent. If it is and proxy environment variables are set, it displays the current proxy settings.

```bash
# Function to check and display proxy settings before certain commands
preexec() {
    # Define network-dependent commands
    local network_commands=(
        "gpa"
        "git"
        "pip"
        "pip3"
        "bundle"
        "brew"
        "cpanm"
        "adb"
        "bundle exec jekyll"
        "make"
        # Add more commands as needed
    )

    # Extract the first word (command) from the command line
    local cmd
    cmd=$(echo "$1" | awk '{print $1}')

    # Function to display proxy variables
    display_proxy() {
        echo -e "\n🚀 **Proxy Settings Detected:**"

        [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
        [ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
        [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
        [ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
        [ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
        [ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"

        echo ""
    }

    # Check if the command is network-dependent
    for network_cmd in "${network_commands[@]}"; do
        if [[ "$1" == "$network_cmd"* ]]; then
            if [ -n "$HTTP_PROXY" ] || [ -n "$http_proxy" ] || \
               [ -n "$HTTPS_PROXY" ] || [ -n "$https_proxy" ] || \
               [ -n "$ALL_PROXY" ] || [ -n "$all_proxy" ]; then
               
                display_proxy
            fi
            break
        fi
    done
}
```

## **Setting Up the Script in Zsh**

1. **Open Your `.zshrc` File**

   ```bash
   nano ~/.zshrc
   ```

2. **Add the `preexec` Function**

   Paste the script above at the end of the file.

3. **Save and Close**

   Press `CTRL + O` to save and `CTRL + X` to exit.

4. **Apply the Changes**

   ```bash
   source ~/.zshrc
   ```

## **Testing the Setup**

1. **With Proxy Enabled**

   ```bash
   export HTTP_PROXY="http://127.0.0.1:7890"
   git status
   ```

   **Output:**

   ```
   
   🚀 **Proxy Settings Detected:**
      - HTTP_PROXY: http://127.0.0.1:7890
      - http_proxy: 127.0.0.1:7890
      - HTTPS_PROXY: 127.0.0.1:7890
      - https_proxy: 127.0.0.1:7890
      - ALL_PROXY: 127.0.0.1:7890
      - all_proxy: 127.0.0.1:7890

   On branch main
   Your branch is up to date with 'origin/main'.

   nothing to commit, working tree clean
   ```

2. **Without Proxy Enabled**

   ```bash
   unset HTTP_PROXY
   git status
   ```

   **Output:**

   ```
   On branch main
   Your branch is up to date with 'origin/main'.

   nothing to commit, working tree clean
   ```

3. **Non-Network Command**

   ```bash
   ls
   ```

   **Output:**

   ```
   [List of files and directories]
   ```

## **Customization**

- **Extend `network_commands`:** Add any additional network-dependent commands to the `network_commands` array.
  
  ```bash
  local network_commands=(
      "gpa"
      "git"
      "pip"
      "pip3"
      "bundle"
      "brew"
      "cpanm"
      "adb"
      "bundle exec jekyll"
      "make"
      "docker"
      "curl"
      "wget"
      # Add more as needed
  )
  ```

- **Handle Aliases:** Ensure that any aliases for network-dependent commands are included in the `network_commands` list.

## **Conclusion**

Managing proxy settings is crucial for smooth software development in restricted network environments. This Zsh script ensures you're always informed about your proxy configurations when running commands that require network access, enhancing your workflow and troubleshooting efficiency.

**Happy Coding! 🚀**

