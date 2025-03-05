---
audio: false
generated: true
lang: zh
layout: post
title: 分叉的 Git 分支
translated: true
---

当你的本地 `main` 分支和远程 `origin/main` 分支在 Git 中发生分歧时—分别有 74 和 70 个不同的提交—这意味着它们共享一个共同的祖先，但自那时起已经发展出了独特的提交。你的目标是使你的本地 `main` 分支与 `origin/main` 匹配，通过将本地分支重置到共同祖先（即“两者的父级”）并使用 `git pull` 来引入远程更改，从而有效地丢弃本地分歧的提交，以便使用远程的提交。以下是实现这一目标的步骤。

### 修复分歧的步骤

1. **获取最新的远程更改**
   首先，确保你的本地仓库有来自远程的最新信息。这将更新你对 `origin/main` 的引用，而不会立即更改你的本地 `main` 分支。

   ```bash
   git fetch origin
   ```

2. **找到共同祖先提交**
   使用 `git merge-base` 来识别本地 `main` 和 `origin/main` 之间的共同祖先提交。这是分支分歧的点。

   ```bash
   ancestor=$(git merge-base main origin/main)
   ```

   这个命令将共同祖先的提交哈希存储在变量 `ancestor` 中。

3. **将本地 `main` 重置为共同祖先**
   将你的本地 `main` 分支重置为共同祖先提交。`--hard` 选项确保分支指针和工作目录都会更新，丢弃所有在该点之后的本地提交和更改。

   ```bash
   git reset --hard $ancestor
   ```

   **注意**：这个步骤将丢弃工作目录和暂存区中的所有未提交更改，以及本地 `main` 的 74 个独特提交。如果需要保留这些，请考虑先创建一个备份分支（见“可选备份”）。

4. **拉取远程更改**
   现在，从 `origin/main` 拉取更改。由于你的本地 `main` 现在在共同祖先，而 `origin/main` 领先 70 个提交，这将快进你的本地 `main` 以匹配 `origin/main`。

   ```bash
   git pull origin main
   ```

   完成后，你的本地 `main` 分支将与 `origin/main` 完全相同，所有本地分歧的提交都被丢弃。

### 完整命令序列

以下是要执行的完整命令序列：

```bash
git fetch origin
ancestor=$(git merge-base main origin/main)
git reset --hard $ancestor
git pull origin main
```

### 发生了什么？
- **在步骤 1 之后**：你的本地仓库知道 `origin/main` 的最新状态。
- **在步骤 2 之后**：你已经识别出共同祖先提交（例如，一个哈希值如 `abc123`）。
- **在步骤 3 之后**：你的本地 `main` 被重置为 `abc123`，丢失了 74 个独特的本地提交。
- **在步骤 4 之后**：`git pull` 快进 `main` 到 `origin/main`，引入远程分支的 70 个提交。

结果是你的本地 `main` 与 `origin/main` 完全匹配，实现了使用远程分支的目标。

### 可选备份
如果你不确定是否要丢弃本地提交，并且希望保留它们以备将来使用，请在重置之前创建一个备份分支：

```bash
git branch backup-main
```

在 `git reset` 命令之前运行此命令。你的 74 个本地提交将保留在 `backup-main` 上，你可以稍后查看它们。

### 重要说明
- **未提交的更改**：如果你有未提交的更改（在工作目录或暂存区中），并且希望保留它们，请在重置之前暂存它们：
  ```bash
  git stash
  ```
  完成过程后，你可以使用 `git stash pop` 来检索它们。
- **为什么有效**：重置到共同祖先并拉取确保了一个干净的快进到 `origin/main`，避免了直接拉取时可能出现的分歧分支的合并冲突。

通过遵循这些步骤，你将成功地将本地 `main` 重置为与 `origin/main` 匹配。