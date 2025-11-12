---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 下拉選單可見性與替代方案
translated: true
type: note
---

在提供的 HTML 片段中，您使用了 `<select>` 元素，預設情況下會呈現為下拉選單。這意味著用戶一眼只能看到當前選中的選項——其他選項在點擊或展開下拉選單前（透過鍵盤/滑鼠互動）都是隱藏的。這是 HTML 中 `<select>` 的標準行為，其設計初衷是為了在緊湊空間中進行列表選擇，避免介面雜亂。

HTML 本身沒有專門用於切換 `<select>` 選項可見性的「開關」元素。不過，有幾種方法可以實現您描述的效果（讓所有選項無需下拉即可見，或提供顯示/隱藏它們的切換功能）。我將在下方概述各種方法的優缺點和程式碼範例。這些方法盡可能使用原生 HTML/CSS，並可選用 JavaScript 實現互動性。由於您的程式碼似乎是 Jekyll 網站的一部分（基於 Liquid 模板），這些方法應該能輕鬆整合。

### 1. **使用單選按鈕替代 `<select>`（選項始終可見）**
   - **為何？** 單選按鈕（`<input type="radio">`）會以行內或列表形式顯示所有選項，無需任何互動即可完全可見。這對於短列表（如您的 type-select 只有 2 個選項）非常適合，但對於較長的列表（如您的 language-sort 有 9 個選項）可能會顯得擁擠。
   - **優點：** 無需 JS；易於存取；用戶可立即看到所有內容。
   - **缺點：** 佔用更多空間；如果需要觸發操作（例如排序/篩選文章），則需要 JS 來處理「選擇」邏輯。
   - **範例程式碼：**
     將您的 `<select>` 替換為一組單選按鈕。為了語義化和無障礙性，將它們包在 `<fieldset>` 中。

     ```html
     <div class="sort-container">
       <!-- 類型選擇改為單選按鈕 -->
       <fieldset>
         <legend>Type</legend>
         <label>
           <input type="radio" name="type" value="posts" checked> Posts
         </label>
         <label>
           <input type="radio" name="type" value="notes"> Notes
         </label>
       </fieldset>

       <!-- 語言排序改為單選按鈕 -->
       <fieldset>
         <legend>Sort by Language</legend>
         <label>
           <input type="radio" name="sort" value="en" checked> English
         </label>
         <label>
           <input type="radio" name="sort" value="zh"> 中文
         </label>
         <label>
           <input type="radio" name="sort" value="ja"> 日本語
         </label>
         <!-- 為 es, hi, fr, de, ar, hant 添加更多標籤 -->
       </fieldset>

       <div>
         <span id="post-number" class="post-number">
           {{ site[type].size }} {{ type }}
           ({{ site[type].size | divided_by: 7 | times: 6 }} Translated by <a href="https://openrouter.ai">AI</a>)
         </span>
       </div>
     </div>
     ```

     - 添加 CSS 進行樣式設定（例如，讓它們看起來像按鈕）：
       ```css
       fieldset {
         border: none; /* 移除預設邊框 */
         display: flex;
         gap: 10px;
       }
       label {
         background: #f0f0f0;
         padding: 5px 10px;
         border-radius: 5px;
         cursor: pointer;
       }
       input[type="radio"] {
         appearance: none; /* 隱藏預設單選圓圈 */
       }
       input[type="radio"]:checked + span { /* 如果在標籤內使用 <span> 放置文字 */
         background: #007bff;
         color: white;
       }
       ```
     - 為了實現功能：使用 JS 監聽變化（例如 `addEventListener('change')`）並更新 UI 或觸發排序。

### 2. **使用按鈕或 Div 作為可點擊選項（自定義「按鈕群組」）**
   - **為何？** 如果您想要更像按鈕的介面，可以使用 `<button>` 或 `<div>` 元素並將其樣式設為按鈕。這會顯示所有可見選項，並允許自定義切換。
   - **優點：** 樣式靈活；可以模擬標籤頁或藥丸形狀；易於實現響應式設計。
   - **缺點：** 需要 JS 來管理活動狀態和操作；語義上不如表單元素正確（使用 ARIA 屬性來確保無障礙性）。
   - **範例程式碼：**
     ```html
     <div class="sort-container">
       <!-- 類型作為按鈕群組 -->
       <div class="button-group" role="group" aria-label="Type selection">
         <button data-type="posts" class="active">Posts</button>
         <button data-type="notes">Notes</button>
       </div>

       <!-- 語言作為按鈕群組 -->
       <div class="button-group" role="group" aria-label="Language selection">
         <button data-sort="en" class="active">English</button>
         <button data-sort="zh">中文</button>
         <button data-sort="ja">日本語</button>
         <!-- 為其他語言添加更多按鈕 -->
       </div>

       <div>
         <span id="post-number" class="post-number">
           {{ site[type].size }} {{ type }}
           ({{ site[type].size | divided_by: 7 | times: 6 }} Translated by <a href="https://openrouter.ai">AI</a>)
         </span>
       </div>
     </div>
     ```

     - 按鈕樣式的 CSS：
       ```css
       .button-group {
         display: flex;
         gap: 5px;
         flex-wrap: wrap; /* 對於長列表 */
       }
       button {
         padding: 5px 10px;
         border: 1px solid #ccc;
         border-radius: 5px;
         cursor: pointer;
       }
       button.active {
         background: #007bff;
         color: white;
       }
       ```
     - 處理點擊事件的 JS（將其添加到 `<script>` 標籤或外部檔案中）：
       ```javascript
       document.querySelectorAll('.button-group button').forEach(button => {
         button.addEventListener('click', function() {
           // 移除同層級按鈕的 active 類
           this.parentNode.querySelectorAll('button').forEach(btn => btn.classList.remove('active'));
           this.classList.add('active');
           // 在此觸發您的排序邏輯，例如更新 post-number 或篩選內容
           console.log('Selected:', this.dataset.type || this.dataset.sort);
         });
       });
       ```

### 3. **添加切換開關以展開選項（混合方法）**
   - **為何？** 如果您希望保持緊湊的 `<select>`，但允許用戶「切換」到顯示所有選項的視圖，可以使用樣式設為切換開關的核取方塊來顯示/隱藏擴展列表。
   - **優點：** 保持預設的緊湊性；使用原生 HTML 進行切換。
   - **缺點：** 需要 CSS/JS；增加複雜性。
   - **範例：** 使用 `<input type="checkbox">` 作為開關，並切換顯示包含所有列出選項的 div 的可見性。
     ```html
     <div class="sort-container">
       <!-- 您原始的 selects 放在這裡 -->

       <!-- 切換開關 -->
       <label class="switch">
         <input type="checkbox" id="show-all-toggle">
         <span>Show All Options</span>
       </label>

       <!-- 隱藏的擴展視圖 -->
       <div id="expanded-options" style="display: none;">
         <!-- 將所有類型和排序選項列為純文字或按鈕 -->
         <ul>
           <li>Posts</li>
           <li>Notes</li>
           <li>English</li>
           <li>中文</li>
           <!-- 等等 -->
         </ul>
       </div>

       <!-- 您的 post-number span -->
     </div>
     ```

     - 開關的 CSS：
       ```css
       .switch input {
         opacity: 0;
         width: 0;
         height: 0;
       }
       .switch span {
         /* 樣式設為切換滑塊 */
         position: relative;
         display: inline-block;
         width: 40px;
         height: 20px;
         background: #ccc;
         border-radius: 20px;
         transition: background 0.3s;
       }
       .switch input:checked + span {
         background: #007bff;
       }
       /* 使用 ::before 或 ::after 添加滑塊旋鈕 */
       ```
     - 切換的 JS：
       ```javascript
       document.getElementById('show-all-toggle').addEventListener('change', function() {
         document.getElementById('expanded-options').style.display = this.checked ? 'block' : 'none';
       });
       ```

### 建議
- 對於您的 **type-select**（僅 2 個選項），單選按鈕或按鈕效果很好且保持簡單。
- 對於 **sort-select**（9 種語言），如果空間允許，按鈕群組是可以的；否則，請堅持使用 `<select>` 並添加工具提示或標籤說明。
- 測試無障礙性（例如使用螢幕閱讀器）和行動裝置響應性。
- 如果這是用於動態網站，請與您現有的 JS 整合，以根據選擇更新 `post-number`。

如果這不符合您所說的「開關」的意思，或者如果您提供更多上下文（例如這些 selects 的作用），我可以進一步完善！