---
audio: false
generated: true
lang: zh
layout: post
title: 使用 MBProgressHUD 在 iOS 中
translated: true
---

看起来你在询问如何在 iOS 项目中通过 Podfile 在 CocoaPods 中使用 `MBProgressHUD` 库，特别是版本 `0.9.1`。让我逐步指导你完成这个过程。

### 什么是 MBProgressHUD？
`MBProgressHUD` 是一个流行的第三方库，用于 iOS，它提供了一种简单的方式来显示带有活动指示器、进度条或自定义视图的 HUD（Heads-Up Display），通常用于显示加载状态或简短消息。

### 使用 `pod 'MBProgressHUD', '0.9.1'` 的步骤

#### 1. **安装 CocoaPods（如果尚未安装）**
CocoaPods 是 iOS 项目的依赖管理器。如果你还没有安装，请在终端中运行以下命令：
```bash
sudo gem install cocoapods
```

#### 2. **设置 Podfile**
- 在终端中导航到你的 Xcode 项目目录：
  ```bash
  cd /path/to/your/project
  ```
- 如果你还没有 Podfile，可以通过运行以下命令来创建一个：
  ```bash
  pod init
  ```
- 使用文本编辑器打开 `Podfile`（例如 `nano Podfile` 或 `open Podfile`）。

#### 3. **将 MBProgressHUD 添加到你的 Podfile**
在 `Podfile` 中，在你的应用程序的目标块中添加 `MBProgressHUD` 版本 `0.9.1` 的行。它应该看起来像这样：
```ruby
platform :ios, '9.0'  # 指定你的部署目标

target 'YourAppName' do
  use_frameworks!
  pod 'MBProgressHUD', '0.9.1'
end
```
- 用你的 Xcode 目标的实际名称替换 `'YourAppName'`。
- `platform :ios, '9.0'` 行设置最低 iOS 版本；根据你的项目需求进行调整。

#### 4. **安装 Pod**
- 保存 `Podfile` 并在终端中运行以下命令：
  ```bash
  pod install
  ```
- 这将下载并将 `MBProgressHUD` 版本 `0.9.1` 集成到你的项目中。如果成功，你会看到确认安装的输出。

#### 5. **打开工作区**
- 安装后，关闭你的 Xcode 项目（如果打开）并打开新创建的 `.xcworkspace` 文件（例如 `YourAppName.xcworkspace`），而不是 `.xcodeproj` 文件。CocoaPods 生成这个工作区来管理依赖项。

#### 6. **在代码中使用 MBProgressHUD**
- **Swift**：导入模块并在代码中使用：
  ```swift
  import MBProgressHUD

  class ViewController: UIViewController {
      override func viewDidLoad() {
          super.viewDidLoad()

          // 显示一个简单的 HUD 与加载指示器
          let hud = MBProgressHUD.showAdded(to: self.view, animated: true)
          hud.label.text = "Loading..."

          // 在一定时间后隐藏它（例如 2 秒）
          DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
              hud.hide(animated: true)
          }
      }
  }
  ```

- **Objective-C**：导入头文件并在代码中使用：
  ```objc
  #import <MBProgressHUD/MBProgressHUD.h>

  @interface ViewController ()
  @end

  @implementation ViewController
  - (void)viewDidLoad {
      [super viewDidLoad];

      // 显示一个简单的 HUD 与加载指示器
      MBProgressHUD *hud = [MBProgressHUD showHUDAddedTo:self.view animated:YES];
      hud.label.text = @"Loading...";

      // 在一定时间后隐藏它（例如 2 秒）
      dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
          [hud hideAnimated:YES];
      });
  }
  @end
  ```

#### 7. **常见的 MBProgressHUD 功能**
- **基本 HUD**：如上所示，显示一个旋转指示器，可选文本。
- **仅文本自定义**：
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .text
  hud.label.text = "Done!"
  hud.hide(animated: true, afterDelay: 1.5)
  ```
- **进度条**：
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .determinate
  hud.progress = 0.5 // 50% 进度
  ```

#### 注意事项
- **版本 0.9.1**：这是一个较旧的版本（大约在 2015 年发布）。截至 2025 年 3 月的最新版本要新得多（例如 1.2.0 或更高）。要使用最新版本，只需写 `pod 'MBProgressHUD'` 而不指定版本号。除非你特别需要 0.9.1 以保持兼容性，否则考虑更新。
- **文档**：查看 [MBProgressHUD GitHub 页面](https://github.com/jdg/MBProgressHUD) 以获取更多选项和示例。版本 0.9.1 可能比现代版本具有更少的功能。

如果你需要帮助排除故障或更具体的示例，请告诉我！