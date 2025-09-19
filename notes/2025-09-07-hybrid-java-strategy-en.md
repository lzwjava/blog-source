---
title: Hybrid Java Development Strategy
date: 2025-09-07
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
---

Short take: for big Java codebases, a **hybrid** works best. Use **VS Code** as your AI-first cockpit (Claude Code + Copilot = faster iteration and boilerplate), and keep **IntelliJ IDEA** around for the “surgery” (deep refactors, inspections, advanced Spring/Gradle/Maven wizards). You don’t have to pick one religion. 🙂

Here’s how I’d think about it—no tables, just the essentials:

### Where VS Code shines

* **AI workflow**: Copilot’s inline completions are still best in VS Code, and Claude Code’s repo-level reasoning feels snappier there. Great for drafting services, tests, mappers, SQL, and quick redesigns.
* **Lightweight & modular**: You bolt on only what you need. Cold starts and memory use are friendlier on huge monorepos.
* **“Jump to” + LSP**: With the Java extensions, “Go to Definition/Implementation,” type hierarchy, call hierarchy, and symbol search are solid enough for day-to-day.

Recommended extensions (search by ID):

* `vscjava.vscode-java-pack` (bundles most of the below)
* `redhat.java` (Language Support for Java)
* `vscjava.vscode-java-debug` / `vscjava.vscode-java-test`
* `vscjava.vscode-maven` / `vscjava.vscode-gradle`
* `vscjava.vscode-spring-boot-dashboard` + `vscjava.vscode-spring-initializr`
* `sonarsource.sonarlint-vscode` (static checks)
* `streetsidesoftware.code-spell-checker` (surprisingly helpful in JavaDocs)
* Claude Code + GitHub Copilot

Performance tweaks for large projects (put in `.vscode/settings.json`):

```json
{
  "java.maxConcurrentBuilds": 4,
  "java.jdt.ls.vmargs": "-Xms512m -Xmx4g -XX:+UseG1GC -XX:+UseStringDeduplication",
  "java.errors.incompleteClasspath.severity": "ignore",
  "java.referencesCodeLens.enabled": false,
  "java.implementationsCodeLens.enabled": false,
  "files.watcherExclude": {
    "**/target/**": true,
    "**/.gradle/**": true,
    "**/node_modules/**": true
  }
}
```

Tips:

* Import as **Gradle** or **Maven** (avoid mixed builds if you can).
* Enable the **Spring Boot Dashboard** for run/debug of multiple services.
* Let Claude/Copilot draft classes & tests, but use **SonarLint** and your unit tests as guardrails.

### Where IntelliJ IDEA still wins

* **Refactoring depth & accuracy**: Rename/move/extract across huge hierarchies, generics-heavy APIs, Lombok, XML config, even Spring bean wiring—IDEA’s semantic model is hard to beat.
* **Inspections & quick-fixes**: The built-in code inspections (and structural search/replace) catch more subtle smells than most VS Code setups.
* **UML & navigation niceties**: Data flow to here/from here, dependency diagrams, and advanced search scopes save time in tangled domains.

Practical pattern:

* Do **exploration + scaffolding + repetitive edits** in VS Code with Claude/Copilot.
* When you need a **non-trivial refactor** (e.g., split a core module, change API contracts across 40 modules, migrate Spring config), open the same repo in IDEA, let it index once, do the refactor safely, push, then go back to VS Code.

### About “Codex”

OpenAI’s old **Codex** models were sunset a while ago. Today you’ll mainly use **GitHub Copilot** (OpenAI-powered under the hood) and **Claude Code**. Treat “Codex” as historical—your current stack should be **Copilot + Claude Code**.

### Static analysis & quality in VS Code

* **SonarLint** in VS Code gives you a near-IDEA feel; pair it with a CI SonarQube/SonarCloud gate.
* Add **SpotBugs** and **Checkstyle** via Gradle/Maven plugins so quality runs in CI (not just locally).
* Use **JUnit** test explorer and **Coverage Gutters** extensions to keep a tight red-green loop.

### Spring/enterprise specifics

* VS Code’s **Spring tooling** is good for run/debug, actuator endpoints, and property hints. For complex auto-config or meta-annotations, IDEA still resolves things more reliably—use it when annotations feel “mysterious.”
* For **Gradle** multi-module monsters: keep daemon + parallel builds on, and consider composite builds to limit workspace size.

### AI workflow that scales

* **Copilot inline** for tiny edits as you type.
* **Claude Code** chat for repo-wide reasoning (“what are the side effects if I change `LedgerPosting`’s constructor?” / “draft a PR to replace our custom retry with resilience4j”).
* Ask the model to produce **refactor plans + checklists**; then apply changes in small, reviewable commits.
* Keep **model output under test**: require unit/integration test diffs in the same PR the AI generated.

### So…which one should you live in?

* If your day is **coding + iterating + lots of AI assists** → **VS Code** as the primary editor feels better right now.
* If your day is **architecting + big refactors + debugging framework edge cases** → keep **IntelliJ** open for those moments.
* Many senior engineers bounce between both. That’s not inefficiency; it’s using the right tool for the right risk level.

If you want, I can generate a one-time **VS Code Java bootstrap** (extensions.json, settings.json, recommended tasks/launch configs) tuned for your monorepo—and a short IDEA checklist for “call in the heavy machinery” moments.