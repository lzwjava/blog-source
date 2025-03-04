---
audio: false
generated: true
lang: zh
layout: post
title: 发布 iOS 应用到应用商店
translated: true
---

要使用 Apple 开发者计划上传 iOS 应用程序，无论是个人使用还是企业使用，都需要注册该计划、准备和打包应用程序、上传应用程序以及管理更新。以下是一个详细的步骤指南，涵盖了您的所有问题，包括企业使用所需的 Dun & Bradstreet（D-U-N-S）号码、打包应用程序、上传归档文件以及通过 Apple 网站更新应用程序。

---

### 1. 注册 Apple 开发者计划

#### 个人（个人使用）
- **创建 Apple ID**：
  如果没有，请访问 [appleid.apple.com](https://appleid.apple.com) 并使用个人电子邮件地址注册。
- **注册计划**：
  - 访问 [developer.apple.com/programs/](https://developer.apple.com/programs/) 并点击“注册”。
  - 使用您的 Apple ID 登录。
  - 同意条款，提供个人的法律姓名和地址，并支付每年 99 美元的费用。
- **注意事项**：您的个人姓名将作为 App Store 的卖家显示。

#### 企业（组织使用）
- **获取 D-U-N-S 号码**：
  - D-U-N-S 号码是 Dun & Bradstreet 分配的唯一九位数字标识符，用于验证您组织的法律实体状态。Apple 对企业账户要求此项。
  - 在 [dnb.com](https://www.dnb.com) 检查您的组织是否已经有了一个。如果没有，请通过他们的网站免费申请，处理时间可能需要两周。
- **注册计划**：
  - 使用与您的组织相关的 Apple ID（例如，商业电子邮件）。
  - 访问 [developer.apple.com/programs/](https://developer.apple.com/programs/) 并点击“注册”。
  - 选择“组织”，并提供：
    - 法律实体名称
    - 总部地址
    - D-U-N-S 号码
  - 注册人必须有法律权限代表组织同意 Apple 的条款。
  - 支付每年 99 美元的费用。
- **注意事项**：您的组织名称将作为 App Store 的卖家显示。

---

### 2. 准备和打包应用程序
- **在 Xcode 中开发您的应用程序**：
  - 使用 Xcode，Apple 的官方开发工具，构建您的 iOS 应用程序。
  - 确保它符合 [App Store 审核指南](https://developer.apple.com/app-store/review/guidelines/)。
  - 设置部署目标，并在项目设置中更新应用程序的版本和构建号。
- **归档应用程序**：
  - 在 Xcode 中打开您的项目。
  - 选择“通用 iOS 设备”（或任何模拟器）作为构建目标。
  - 在菜单栏中选择 **Product** > **Archive**。
  - Xcode 将编译您的应用程序并创建一个归档文件，这是一个准备好用于分发的打包版本，包括代码、资源和签名信息。

---

### 3. 上传应用程序归档
- **使用 Xcode**：
  - 归档后，Xcode 会自动打开组织器窗口。
  - 选择您的归档文件，然后点击 **Distribute App**。
  - 选择 **App Store Connect** 作为分发方法。
  - 按照提示验证并将归档文件上传到 App Store Connect。
- **使用 Transporter（替代方法）**：
  - 从 Mac App Store 下载 [Transporter 应用程序](https://apps.apple.com/us/app/transporter/id1450874784)。
  - 使用您的 Apple ID 登录。
  - 添加从 Xcode 导出的归档应用程序文件（作为 `.ipa` 文件）并将其上传到 App Store Connect。
  - 此选项适用于高级用户或批量上传。

---

### 4. 使用 Apple 网站（App Store Connect）更新应用程序
- **访问 App Store Connect**：
  - 访问 [appstoreconnect.apple.com](https://appstoreconnect.apple.com) 并使用您的 Apple ID 登录。
- **管理您的应用程序**：
  - 从仪表板中选择您的应用程序。
  - 导航到 **App Store** 选项卡。
  - 更新元数据（例如，应用程序描述、截图、关键字）。
  - 在“版本”中，选择您上传的新构建。
- **提交审核**：
  - 点击 **Submit for Review** 将更新发送到 Apple 的审核团队。
  - 审核通过后，您可以手动发布或安排自动发布。

---

### 附加说明
- **企业特定细节**：
  - 确保您的 D-U-N-S 号码和组织信息准确，以避免注册延迟。
  - 您可以通过 App Store Connect 邀请团队成员（例如，开发人员、测试人员）并分配角色，如“开发人员”或“管理员”。
- **常见挑战和技巧**：
  - **代码签名问题**：在 Xcode 中的 **Signing & Capabilities** 下验证您的证书和配置文件。如果不确定，请使用“自动管理签名”选项。
  - **应用审核拒绝**：彻底测试您的应用程序，以符合 Apple 的指南并避免延迟。
  - **D-U-N-S 延迟**：如果您是企业，请尽早申请 D-U-N-S 号码，因为这是注册的先决条件。

---

通过这些步骤，您可以成功使用 Apple 开发者计划上传和更新您的 iOS 应用程序，无论是作为个人还是企业。有关更多详细信息，请参阅 Apple 的官方文档 [developer.apple.com](https://developer.apple.com)。