---
lang: en
layout: post
title: "Node.js OpenSSL Compatibility"
---

When running `ng build` with **Node.js 22.9.0** and **npm 10.8.3**, you encounter the error:

```
error 0308010C digital envelope routines::unsupported
```

This error typically arises due to a compatibility issue between newer versions of Node.js (like 22.9.0, which uses OpenSSL 3.0 or later) and certain cryptographic algorithms relied upon by tools like Webpack, which Angular uses under the hood. Below is a step-by-step guide to fix this issue.

---

### Solution

#### Step 1: Enable the OpenSSL Legacy Provider
The simplest and most immediate fix is to enable the OpenSSL legacy provider by setting the `NODE_OPTIONS` environment variable. This allows Node.js to use older cryptographic algorithms that may no longer be supported by default in OpenSSL 3.0+.

- **For macOS/Linux**:
  Open your terminal and run:
  ```bash
  export NODE_OPTIONS=--openssl-legacy-provider
  ng build
  ```

- **For Windows (Command Prompt)**:
  Open Command Prompt and run:
  ```cmd
  set NODE_OPTIONS=--openssl-legacy-provider
  ng build
  ```

- **For Windows (PowerShell)**:
  Open PowerShell and run:
  ```powershell
  $env:NODE_OPTIONS="--openssl-legacy-provider"
  ng build
  ```

After setting the environment variable, run `ng build` again. This should resolve the error in most cases by allowing Node.js to process the unsupported routines.

---

#### Step 2: Verify and Update Angular CLI (If Needed)
If the error persists after Step 1, your version of the Angular CLI might not be fully compatible with Node.js 22.9.0. Updating it to the latest version can help.

- Check your current Angular CLI version:
  ```bash
  ng --version
  ```

- Update Angular CLI globally:
  ```bash
  npm install -g @angular/cli
  ```

- Then, try running `ng build` again.

---

#### Step 3: Check and Update Project Dependencies (Optional)
If the issue still isn’t resolved, outdated dependencies in your project might be causing the problem. To address this:

- Open your `package.json` file and review the versions of your dependencies (e.g., `@angular/core`, `@angular/cli`, etc.).
- Update them carefully to their latest compatible versions:
  ```bash
  npm install
  ```
  or, if you want to update all dependencies:
  ```bash
  npm update
  ```

- Run `ng build` again to test.

*Note*: Be cautious with updates, as they might introduce breaking changes. Test your application thoroughly afterward.

---

#### Step 4: Downgrade Node.js (Last Resort)
If none of the above solutions work, Node.js 22.9.0 might not yet be fully supported by your project’s current configuration. Downgrading to a Long-Term Support (LTS) version of Node.js, such as **20.x** or **18.x**, could resolve the issue.

- Uninstall your current Node.js version.
- Download and install an LTS version from the [official Node.js website](https://nodejs.org/).
- Verify the installed version:
  ```bash
  node -v
  ```
- Reinstall your project dependencies:
  ```bash
  npm install
  ```
- Run `ng build` again.

---

### Recommended Approach
Start with **Step 1** (setting `NODE_OPTIONS`), as it’s the quickest fix and allows you to keep using Node.js 22.9.0. If that doesn’t work, proceed to **Step 2** and **Step 3**. Use **Step 4** only if necessary, as downgrading Node.js might limit access to newer features.

This should resolve the "error 0308010C digital envelope routines::unsupported" and get your `ng build` command working again!