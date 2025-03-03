---
audio: false
generated: true
lang: hi
layout: post
title: Jenkinsfile लिखना
translated: true
---

Jenkinsfile में एक shared library, एक string parameter, एक try-catch block, एक node block, और एक if statement को incorporate करने ke liye, aap yeh approach use kar sakte hain. Jenkinsfiles Groovy mein likhe jaate hain aur yeh build, test, aur deployment processes ko automate karne ke liye ek pipeline define kar sakte hain. Niche ek complete example hai ek scripted Jenkinsfile jo yeh requirements ko fulfill karta hai.

Pehle, ek shared library ko use karne ke liye, usse `@Library` annotation ke saath import karna padta hai. Jenkins mein shared libraries mein reusable code hota hai jo multiple pipelines se call kiya ja sakta hai. Agar aapka shared library ka naam `my-shared-library` hai, toh aap usse Jenkinsfile ke top par yeh tarah se include karte hain:

```groovy
@Library('my-shared-library') _
```

Annotation ke baad underscore (`_`) ko properly import karne ke liye zaroori hota hai.

Aage, ek string parameter define karne ke liye, `properties` step ka use karein. Isse users ko pipeline ko run karte samay ek string value pass karne ki suvidha milti hai. Yeh tarah se ek string parameter `MY_STRING` add kar sakte hain:

```groovy
properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'A string parameter')
    ])
])
```

`node` block specify karta hai ki pipeline kaha execute hoga, jaise ki kisi bhi available agent par. Is block ke andar aap apne pipeline logic ko include kar sakte hain:

```groovy
node {
    // Pipeline steps go here
}
```

Potential errors ko handle karne ke liye, apne steps ko ek `try-catch` block mein wrap karein. Isse agar kuch fail ho jaye, toh aap exception ko catch kar sakte hain aur usse gracefully handle kar sakte hain. Alag se, ek `if` statement ko use karke, string parameter (`params.MY_STRING`) ke value ke basis par decisions le sakte hain.

Yeh hai complete Jenkinsfile jo sabhi elements ko combine karta hai:

```groovy
@Library('my-shared-library') _

properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'A string parameter')
    ])
])

node {
    try {
        // Call a function from the shared library (assuming it exists)
        myLibraryFunction()

        // Use an if statement based on the string parameter
        if (params.MY_STRING == 'test') {
            echo "Running test"
        } else {
            echo "Not running test"
        }
    } catch (Exception e) {
        echo "An error occurred: ${e.message}"
    }
}
```

### Components ka Explanation

- **`@Library('my-shared-library') _`**: Ek shared library ko import karta hai jo `my-shared-library` kehte hain. `my-shared-library` ko apne library ka actual naam se replace karein. Function `myLibraryFunction()` ko yeh library mein define hona chahiye.
- **`properties`**: Ek string parameter `MY_STRING` define karta hai jo default value `'default'` aur ek description ke saath hai. Aap is parameter ko pipeline mein `params.MY_STRING` ke saath access kar sakte hain.
- **`node`**: Pipeline ko kisi bhi available agent par run karta hai. Agar zaroori hai, toh aap ek particular agent specify kar sakte hain (e.g., `node('linux')`).
- **`try-catch`**: `try` block ke andar steps ko execute karta hai aur `catch` block mein kisi bhi exceptions ko catch karta hai, agar kuch galat ho jaye toh ek error message print karta hai.
- **`if`**: Check karta hai ki `MY_STRING` `'test'` ke barabar hai ya nahi aur accordingly ek message print karta hai. Aap condition aur actions ko modify kar sakte hain jaise ki zaroori hai.

### Notes
- Yeh example ek scripted pipeline ko assume karta hai, jo Groovy syntax ke saath zyada flexibility provide karta hai. Agar aapko declarative pipeline chahiye, toh structure thoda alag hoga (e.g., `pipeline` aur `script` blocks ke liye Groovy code).
- `myLibraryFunction()` call ek placeholder hai. Ensure karein ki aapka shared library yeh function define karta hai, ya phir usse ek actual function se replace karein jo aapke library mein hai.
- Aap is Jenkinsfile ko expand kar sakte hain stages add karke (e.g., `stage('Build')`) ya zyada complex logic add karke jaise ki aapke requirements ke hisaab se.

Yeh Jenkinsfile ek solid foundation provide karta hai jo aapne request ki sabhi elements ko include karta hai: ek shared library, ek string parameter, ek try-catch block, ek node block, aur ek if statement. Aapko specifics (library name, function calls, ya conditions) ko apne use case ke hisaab se adjust karna padega!