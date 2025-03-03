---
audio: false
generated: true
lang: zh
layout: post
title: 使用 PopMenu 在 iOS
translated: true
---

在你的iOS项目中使用 `pod 'PopMenu', '2.4'`，你将通过CocoaPods（一个流行的iOS依赖管理器）集成PopMenu库（版本2.4）。这个库提供了一个受新浪微博或网易等应用启发的弹出动画菜单。以下是设置和使用它的步骤：

---

### 第1步：安装CocoaPods（如果尚未安装）
如果你的系统上没有安装CocoaPods，请先安装它：
1. 打开你的终端。
2. 运行以下命令：
   ```bash
   sudo gem install cocoapods
   ```
3. 验证安装：
   ```bash
   pod --version
   ```

---

### 第2步：设置你的Podfile
1. 在终端中导航到你的Xcode项目目录：
   ```bash
   cd /path/to/your/project
   ```
2. 如果你还没有Podfile，通过运行以下命令创建一个：
   ```bash
   pod init
   ```
3. 使用文本编辑器打开`Podfile`（例如`nano Podfile`或使用Xcode）。
4. 添加以下行以指定你的目标的PopMenu pod：
   ```ruby
   platform :ios, '8.0'  # 如果需要，调整iOS版本
   target 'YourAppName' do
     use_frameworks!
     pod 'PopMenu', '2.4'
   end
   ```
   - 将`YourAppName`替换为你的Xcode目标的名称。
   - `use_frameworks!`行是必需的，因为PopMenu可能是一个基于框架的库。

5. 保存并关闭Podfile。

---

### 第3步：安装Pod
1. 在终端中运行：
   ```bash
   pod install
   ```
2. 这将下载并将PopMenu版本2.4集成到你的项目中。等待看到类似以下的消息：
   ```
   Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
   ```
3. 如果Xcode项目已打开，请关闭它，然后打开新生成的`.xcworkspace`文件（例如`YourAppName.xcworkspace`），而不是`.xcodeproj`文件。

---

### 第4步：在代码中进行基本使用
PopMenu是用Objective-C编写的，因此你需要相应地使用它。以下是如何在你的应用中实现它的示例：

1. **导入库**：
   - 在你的Objective-C文件（例如`ViewController.m`）中：
     ```objective-c
     #import "PopMenu.h"
     ```
   - 如果你使用Swift，创建一个桥接头文件：
     - 转到`File > New > File > Header File`（例如`YourAppName-Bridging-Header.h`）。
     - 添加：
       ```objective-c
       #import "PopMenu.h"
       ```
     - 在Xcode中，在`Build Settings > Swift Compiler - General > Objective-C Bridging Header`下设置桥接头文件的路径（例如`YourAppName/YourAppName-Bridging-Header.h`）。

2. **创建菜单项**：
   定义你想要在弹出菜单中的项目。每个项目都可以有标题、图标和发光颜色。
   ```objective-c
   NSMutableArray *items = [[NSMutableArray alloc] init];

   MenuItem *menuItem1 = [[MenuItem alloc] initWithTitle:@"Flickr"
                                               iconName:@"post_type_bubble_flickr"
                                              glowColor:[UIColor grayColor]
                                                  index:0];
   [items addObject:menuItem1];

   MenuItem *menuItem2 = [[MenuItem alloc] initWithTitle:@"Twitter"
                                               iconName:@"post_type_bubble_twitter"
                                              glowColor:[UIColor blueColor]
                                                  index:1];
   [items addObject:menuItem2];
   ```

3. **初始化并显示菜单**：
   创建一个`PopMenu`实例并在你的视图中显示它。
   ```objective-c
   PopMenu *popMenu = [[PopMenu alloc] initWithFrame:self.view.bounds items:items];
   popMenu.menuAnimationType = kPopMenuAnimationTypeNetEase; // 选项：kPopMenuAnimationTypeSina或kPopMenuAnimationTypeNetEase
   popMenu.perRowItemCount = 2; // 每行的项目数
   [popMenu showMenuAtView:self.view];
   ```

4. **处理选择（可选）**：
   你可以子类化或扩展功能以检测点击，尽管PopMenu的基本版本（约2.4）可能不原生支持委托。检查GitHub上的库文档（`xhzengAIB/PopMenu`）以获取任何更新或自定义。

---

### 第5步：运行你的项目
在Xcode中构建并运行你的项目（`Cmd + R`）。如果图标（例如`post_type_bubble_flickr`）是你的资产目录的一部分，请确保它们已添加到你的项目中。如果没有，你需要获取或创建它们。

---

### 注意事项
- **版本特定性**：`pod 'PopMenu', '2.4'`将你锁定在版本2.4。如果你想要最新版本，使用`pod 'PopMenu'`而不带版本号，但这可能会引入破坏性更改。
- **兼容性**：确保你的项目的部署目标至少是iOS 8.0（或在Podfile中调整`platform`）。
- **自定义**：PopMenu允许动画类型和布局调整（例如`perRowItemCount`）。探索源代码以获取更多选项。
- **故障排除**：如果遇到类似“文件未找到”的错误，请确保你的Pods正确安装并且你在使用工作区。

这应该让你开始在iOS应用中使用PopMenu 2.4！如果你需要进一步的澄清，请告诉我。