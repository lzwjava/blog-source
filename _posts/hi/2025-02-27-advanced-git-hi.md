---
audio: false
generated: false
lang: hi
layout: post
title: उन्नत Git कमांड
translated: true
---

Git kaa maatrabhut ek Swiss Army knife hai developers ke liye—versatile, powerful, aur kabhi kabhi confusing agar aapko nahi pata hai ki kaun sa tool nikalna hai. Aaj hum kuch Git ke niftiest features aur workflows mein dive kar rahe hain: cherry-picking changes, merging with style, rebasing for a cleaner history, delete karna wo pesky large files jo aapne accidentally committed, aur undo karna ek commit jab aapko lagta hai ki aapne off the rails gaya hai. Chalo isse break karte hain.

#### Cherry-Picking: Grabbing Just What You Need
Socho aapke paas ek feature branch hai jisme dozain commits hain, par ek shiny commit hai jo aapko pluck karke apply karna hai apne main branch mein—bina baaki ke sath. Yahan `git cherry-pick` kaa kaam hai.

Yeh bahut straightforward hai: commit hash ko find karo (aapko `git log` se grab kar sakte hain), us branch par switch karo jahan aapko chahiye, aur run karo:
```
git cherry-pick <commit-hash>
```
Boom, woh commit ab aapke current branch kaa part hai. Agar conflict hai, Git pause karega aur aapko resolve karne ke liye allow karega, just like a merge. Jab aap happy ho jayen, changes ko commit karo, aur aap theek hain.

Main isse kabhi kabhi use karte hoon jab ek bug fix ek messy feature branch mein sneak kar gaya hai, aur mujhe usse `main` par chahiye ASAP. Sirf dhyan rakho—cherry-picking duplicate the commit, toh woh ek naya hash paata hai. Expect nahi karo ki woh theek se play karega agar aap original branch ko later merge karte hain bina kuch cleanup ke.

#### Merge Options: More Than Just “Merge”
Merging Git kaa bread and butter hai, par aapko pata hai ki iske saath flavors aate hain? Default `git merge` ek “fast-forward” karta hai agar possible hai (history ko straighten karke) ya ek merge commit banata hai agar branches diverge ho gaye hain. Par aapke paas options hain:

- **`--no-ff` (No Fast-Forward)**: Merge commit ko force karta hai even agar ek fast-forward possible hai. Main isse pasand karta hoon ek clear record rakhne ke liye jab ek feature branch `main` par land ho gaya. Run karo:
  ```
  git merge --no-ff feature-branch
  ```
- **`--squash`**: Sab changes ko ek branch se ek commit mein pull karta hai aapke current branch par. No merge commit, sirf ek single, tidy package. Perfect hai ek messy branch ko squash karne ke liye kuch presentable mein:
  ```
  git merge --squash feature-branch
  ```
  Iske baad, aapko manually commit karna padega deal ko seal karne ke liye.

Har ek kaa apna place hai. Main `--no-ff` ke liye lean karta hoon long-lived branches ke liye aur `--squash` jab mujhe ek branch full of “WIP” commits hai jo main bhulna chahta hoon.

#### Rebasing: Rewriting History Like a Pro
Agar merges ko cluttered lagta hai, `git rebase` aapka vibe ho sakta hai. Yeh aapke commits ko lekar aur unhe ek aur branch par replay karta hai, aapko ek linear history deta hai jo lagta hai aapne sabse pehle se plan kiya tha.

Switch karo apne feature branch par aur run karo:
```
git rebase main
```
Git aapke commits ko lift karega, branch ko update karega `main` ke saath match karne ke liye, aur aapke changes ko top par slap karega. Agar conflicts pop up karte hain, resolve karo, phir `git rebase --continue` karte raho jab tak complete na ho jaye.

Upside? Ek pristine timeline. Downside? Agar aapne woh branch pehle push kiya hai aur dusre us par kaam kar rahe hain, toh rebasing history ko rewrite karta hai—cue the angry emails from teammates. Main rebasing ke liye local branches ya solo projects par stick karta hoon. Shared stuff ke liye, merge safer hai.

#### Deleting Large Files from History: Oops, That 2GB Video
Hum sabne isse kiya hai: aapne ek massive file ko accidentally commit kiya, push kiya, aur ab aapka repo bloated hai. Git easily bhulata nahi hai, par aap us file ko history se scrub kar sakte hain kuch effort ke saath.

Yahan kaa go-to tool `git filter-branch` hai ya naya `git filter-repo` (main latter ko recommend karta hoon—woh faster aur less error-prone hai). Socho aapne `bigfile.zip` commit kiya hai aur usse chahiye:
1. Install `git-filter-repo` (setup ke liye uske docs check karo).
2. Run karo:
   ```
   git filter-repo --path bigfile.zip --invert-paths
   ```
   Yeh `bigfile.zip` ko history mein har commit se remove karega.
3. Force-push the rewritten history:
   ```
   git push --force
   ```

Heads-up: yeh history ko rewrite karta hai, toh apne team ke saath coordinate karo. Aur agar yeh ek pull request mein hai, toh aapko refs ko clean up karna padega bhi. Jab yeh gone ho jaye, aapka repo slim down hoga baad mein ek garbage collection (`git gc`) ke baad.

#### Uncommitting: Rewinding the Clock
Ek commit kiya aur instantly regret kiya? Git aapke back hai. Isse undo karne ke liye kuch tareeke hain, depend karte hain kitna aapne jaise:

- **Agar aapne pehle push nahi kiya hai**: Use `git reset`. Last commit ko undo karne ke liye aur changes ko aapke working directory mein rakhne ke liye:
  ```
  git reset HEAD^ --soft
  ```
  Changes ko entirely ditch karna chahta ho:
  ```
  git reset HEAD^ --hard
  ```
- **Agar aapne pehle push kiya hai**: Aapko history ko rewrite karna padega. Locally reset karo `git reset HEAD^`, phir force-push:
  ```
  git push --force
  ```
  Phir bhi, yeh shared history ko mess karta hai, toh carefully tread karo.

Mainne `git reset --soft` se apne ko bahut baar bacha liya hai—perfect hai jab main commit too soon karta hoon aur kuch tweak karna chahta hoon.

#### Wrapping Up

Git kaa flexibility usse itna powerful banata hai, par agar aapko apne options nahi pata hain, toh aapko tang ho sakta hai. Cherry-pick karo surgical precision ke liye, merges ko tweak karo apne workflow ke liye fit karne ke liye, rebase karo ek polished history ke liye, aur panic na karo jab aapko ek mistake ko erase karna pade—chahye woh ek huge file ho ya ek hasty commit. Practice karo inko ek test repo par agar aapko nervous lagta hai, aur soon yeh aapke liye second nature lagne lage.

Aapka favorite Git trick kya hai? Mujhe batao—I’m always up for learning something new!