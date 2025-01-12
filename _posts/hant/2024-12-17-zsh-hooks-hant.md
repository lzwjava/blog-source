---
audio: true
lang: hant
layout: post
title: Zsh 钩子
---

在探索了“让Zsh在执行网络命令前显示代理设置”之后，我借助ChatGPT深入研究了Zsh钩子。以下为未来参考的简要概述。

---

在 Zsh 中，钩子（hooks）允许你在 shell 操作的特定时刻执行自定义函数。除了 `preexec` 之外，Zsh 还提供了多种钩子来增强你的环境：

### 1. `precmd`
- **何時使用**：在提示符顯示之前。
- **用途**：更新提示符或執行清理操作。
- **範例**：
  ```zsh
  precmd() {
    echo "準備好接收下一個指令！"
  }
  ```

### 2. `chpwd`
- **触发时机**：当当前目录发生变化时。
- **用途**：更新环境变量或根据目录触发特定操作。
- **示例**：
  ```zsh
  chpwd() {
    echo "已切换至：$PWD"
  }
  ```

### 3. `preexec_functions` 和 `precmd_functions`
- **时机**：类似于 `preexec` 和 `precmd`，但支持多个函数。
- **用途**：附加多个操作而不覆盖现有的钩子。
- **示例**：
  ```zsh
  precmd_functions+=(additional_precmd)
  
  additional_precmd() {
    echo "额外的 precmd 任务。"
  }
  ```

### 4. `TRAPDEBUG`
- **触发时机**：每条命令执行后，结果显示之前。
- **用途**：调试、记录命令执行情况。
- **示例**：
  ```zsh
  TRAPDEBUG() {
    echo "已执行: $1"
  }
  ```

### 5. `TRAPEXIT`
- **触发时机**：当 shell 退出时。
- **用途**：用于执行清理任务或显示退出信息。
- **示例**：
  ```zsh
  TRAPEXIT() {
    echo "再见！"
  }
  ```

### 6. `zle` 钩子
- **时机**：在命令行编辑期间。
- **用途**：自定义命令行行为。
- **示例**：
  ```zsh
  zle-line-init() {
    echo "正在编辑新命令。"
  }
  zle -N zle-line-init
  ```

### 7. 历史钩子 (`zshaddhistory`, `zshremovehistory`)
- **时机**：添加或删除历史记录条目时。
- **用途**：过滤或管理历史记录。
- **示例**：
  ```zsh
  zshaddhistory() {
    [[ $1 == *"secret"* ]] && return 1
    return 0
  }
  ```

### 8. `periodic`
- **触发时机**：按照`period`设置的间隔时间定期执行。
- **用途**：用于例行检查或更新任务。
- **示例**：
  ```zsh
  periodic() {
    echo "正在執行定期任務..."
  }
  ```

### 9. `add-zsh-hook`
- **用途**：安全地向钩子添加函数。
- **用法**：追加多个函数而不覆盖原有函数。
- **示例**：
  ```zsh
  add-zsh-hook precmd another_precmd
  
  another_precmd() {
    echo "另一个 precmd 函数。"
  }
  ```

### 总结

Zsh的钩子系统功能多样，支持自动化与定制化操作：

- `preexec`：命令执行前。
- `precmd`：提示符显示前。
- `chpwd`：目录变更时。
- `TRAPDEBUG`：调试用的后置命令。
- `TRAPEXIT`：Shell退出时。
- `zle` 钩子：行编辑期间。
- 历史钩子：管理命令历史。
- `periodic`：设定间隔时。
- `add-zsh-hook`：添加多个钩子函数。

利用这些钩子可以极大地提升您的Zsh体验，使您的Shell更加高效，并更好地适应您的工作流程。