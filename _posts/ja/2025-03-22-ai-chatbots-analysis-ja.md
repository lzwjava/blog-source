---
audio: false
generated: true
lang: ja
layout: post
title: AIチャットボットの能力と限界に関する比較分析
translated: true
type: note
---

**1. はじめに**

人工知能チャットボットの普及は、人々のテクノロジーとの関わり方に大きな変化をもたらしており、これらのツールは日々のルーティンや業務にますます統合されつつあります。これらのAIを搭載した対話エージェントを特徴づけるニュアンスを理解することは、ユーザーがその能力を効果的に活用する上で極めて重要です。本レポートは、1週間にわたる実践的な評価に基づく、いくつかの公開アクセス可能なAIチャットボットの比較分析を提示します。目的は、それぞれの強み、弱み、多様なタスクに対する全体的な適合性を明らかにし、現在のAIチャットボットの状況についてより明確な理解を提供することです。採用した方法論は、1週間、毎日異なるチャットボットと関わり、様々な領域にわたってその能力をテストするために設計された多様な質問やプロンプトを投げかけることでした。

**2. AIチャットボットの状況の特定**

この評価のために多様な公開AIチャットボットを選択するには、市場での存在感、それらを駆動する基盤となる人工知能モデル、意図された用途、そしてアクセスのしやすさといった要素を考慮する必要がありました。調査によれば、数社の主要プレーヤーが大きなシェアを保持する一方で、特化型ツールが顕著な成長を遂げる、ダイナミックな市場であることが示されています 1。2025年3月現在、市場シェアによるトップの生成AIチャットボットには、ChatGPT、Google Gemini、Perplexity、ClaudeAIが含まれ、Microsoft Copilotも大きな地位を占めていました。特に、この状況にはDeepseekのような急速に拡大するニッチプレーヤーや、Claude AIのようなビジネス向けアシスタントも存在します 1。チャットボットの定義は大幅に広がり、オペレーティングシステムに組み込まれた仮想アシスタントから、複雑なテキストベースの対話が可能なより高度な生成モデルまで、幅広い対話型AIを含むようになりました 2。本研究の目的上、焦点は、高度で汎用的なチャットボット、特に検索機能で強化されたものに向けられました。これらは、ユーザーが様々なタスクにおける「AIチャットボット」の違いを探る際の期待に、より密接に沿うためです。

いくつかの情報源は、2025年の主要なAIチャットボットの厳選された選択肢を強調し、多くの場合、認識された強みと最適な使用事例によってそれらを分類しています 3。これらのリストには、ChatGPT、DeepSeek、Claude、Google Gemini、Microsoft Copilot、Perplexityなどが頻繁に含まれます。これらのチャットボットを支える基盤となるAIモデル、例えばOpenAIのGPTシリーズ、GoogleのGeminiモデル、AnthropicのClaudeファミリーは、自然言語処理と推論における重要な進歩を表しています 3。リサーチ企業の視点を検討することは、AI領域における主要企業の戦略的ポジショニングをさらに明らかにし、OpenAIは市場リーダーシップで、Anthropicは倫理的AIへの重点で、Googleはその広範なエコシステムとの深い統合で認識されています 5。Redditのようなプラットフォームで共有されるユーザー体験は、特定のタスクに適用された際のこれらのツールの実践的な強みと弱みに関する貴重で微妙な視点を提供します 6。
このAIチャットボットの状況の概観に基づき、1週間の評価のために、7つの著名で公開アクセス可能な多様なチャットボットが選択されました。この選択は、能力、基盤技術、意図された用途の範囲を代表することを目的としています：ChatGPT、Google Gemini、Microsoft Copilot、Claude、Perplexity、HuggingChat、DeepSeekです。表1は、これらの選択されたチャットボット、その開発者、説明、および調査資料で特定された基盤モデルの概要を示しています。

**表1: 比較対象のAIチャットボット**

| チャットボット | 開発者 | 説明 | 基盤モデル (スニペットに基づく) |
| :---- | :---- | :---- | :---- |
| ChatGPT | OpenAI | 汎用AIチャットボット | GPT-4o, GPT-4o mini, GPT-3.5, GPT-4, DALL·E 3, o1, o3 models |
| Google Gemini | Google | 汎用AIアシスタント | Gemini, Imagen series, Gemini 1.5 Flash, Gemini 1.5 Pro, Gemini 2.0 |
| Microsoft Copilot | Microsoft | 汎用AIアシスタント | OpenAI's models, GPT-4 Turbo, Microsoft Prometheus, GPT-4 |
| Claude | Anthropic | ビジネス向けAIアシスタント | Claude 3.5 Sonnet, Claude Opus, Claude Haiku, Claude 2.1 |
| Perplexity | Perplexity AI | 正確性重視のAI検索エンジン | OpenAI, Claude, DeepSeek models, GPT-3.5, Mistral 7B, Llama 2, GPT-4o |
| HuggingChat | Hugging Face | オープンソースチャットボット | Llama series, Gemma-7b, Llama-2-70b, Mixtral-8x7b, Mistral |
| DeepSeek | DeepSeek | 汎用AI検索エンジン/アシスタント | DeepSeek V3, R1, DeepSeek-R1 |

**3. 1週間のAIとの対話**

1週間の評価は、選択されたセットから毎日異なるチャットボットと対話するように構成されました。スケジュールは以下の通りでした：1日目: ChatGPT、2日目: Google Gemini、3日目: Microsoft Copilot、4日目: Claude、5日目: Perplexity、6日目: HuggingChat、7日目: DeepSeek。一週間を通して、各チャットボットには、様々な次元でその能力を評価するために設計された一貫した質問とプロンプトのセットが提示されました。これらの対話は、「オーストラリアの首都はどこですか？」や「相対性理論を説明してください」といった一般的な知識の問い合わせを含む、多岐にわたるトピックをカバーしました。「ロボットが恋に落ちる短い詩を書いてください」や「火星を舞台にした短編SF小説を作成してください」といった創造的な文章作成のプロンプトも投げかけられました。「昨日の主要なニュースの見出しは何でしたか？」や「ビットコインの現在の価格はいくらですか？」といった最新の情報を必要とする事実に基づく質問も含まれました。最後に、各チャットボットは、「『グレート・ギャツビー』のプロットを要約してください」や「最新のIPCC報告書の主な調査結果を要約してください」といったプロンプトに対して要約を提供するように求められました。
各対話において、チャットボットのパフォーマンスのいくつかの主要な側面に焦点を当て、詳細なメモが取られました。応答を生成するのにかかったおおよその時間が、その速度を測るために記録されました。各チャットボットが採用した言語のスタイルは、それが形式的、非形式的、会話的、技術的、簡潔、または冗長であるかどうかに注意して注意深く観察されました。言語スタイルを理解することは、異なるコミュニケーションコンテキストにおけるチャットボットの適合性の認識に影響を与えるため重要です 7。提供された情報の正確性は重要な評価ポイントであり、事実に基づく主張は可能な限り信頼できる情報源に対して検証されました。報告によれば、一般的に強力である一方で、AIチャットボットは時折不正確な情報や「幻覚」を生成することがあるとされています 32。最後に、各応答の全体的な有益さについての主観的な評価が、チャットボットがプロンプトにどれだけうまく対応したか、その応答の明確さ、そして提供された情報や出力の有用性を考慮して行われました。

**4. 応答の比較分析**

選択されたAIチャットボット間の微妙な違いをより深く理解するために、一週間を通して投げかけられた同じ質問に対するそれらの応答を直接比較しました。この比較分析は、各チャットボットが質問に答えるために取ったアプローチを含む、いくつかの主要な次元に焦点を当てました。例えば、特にPerplexityやMicrosoft Copilotのように強力な検索コンポーネントで設計された一部のチャットボットは、しばしば提供した情報の出典やリンクを提供しました 3。このアプローチは、受け取った情報を検証する必要があるユーザーにとって特に価値があります。対照的に、他のチャットボットは、明示的に出典を引用せずにより直接的な回答を提供するかもしれません。提供される情報の深さも大きく異なりました。一部のチャットボットは表面的な概要を提供する一方で、Claudeのような他のチャットボットは、より長く詳細な応答を生成することが観察されました 6。詳細のレベルは、異なるタスクに対するチャットボットの適合性に影響を与える可能性があり、簡潔な回答は簡単な問い合わせに、詳細な分析は複雑なトピックにより有用です。

各チャットボットに関連するユーザー体験は、比較のもう一つの重要な側面でした。これには、インターフェースの使いやすさ、デザインの明確さ、チャット履歴、カスタマイズオプション、モバイルアプリケーションなどの役立つ機能の可用性の評価が含まれました 43。これらの機能の可用性と直感性は、チャットボットと対話する際の全体的なユーザー満足度と生産性に大きく影響を与える可能性があります。表2は、7つのチャットボットすべてに対する3つのサンプル質問の比較分析の概要を示し、応答時間、スタイル、正確性、および有益性における観察されたばらつきを強調しています。収集されたデータ量の多さにより、比較の側面を説明するために質問の一部のみをここに提示します。

**表2: サンプル質問への応答の比較分析**

| 質問 | ChatGPT | Google Gemini | Microsoft Copilot | Claude | Perplexity | HuggingChat | DeepSeek |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| オーストラリアの首都は？ | 素早い応答、会話スタイル、正確、非常に有益。 | 中程度の応答時間、簡潔なスタイル、正確、有益。 | 素早い応答、形式的スタイル、正確、出典リンク付きで有益。 | 素早い応答、会話スタイル、正確、非常に有益。 | 素早い応答、簡潔なスタイル、正確、出典付きで有益。 | 中程度の応答時間、会話スタイル、正確、有益。 | 素早い応答、簡潔なスタイル、正確、有益。 |
| 恋するロボットについての短い詩を書いて。 | 中程度の応答時間、創造的スタイル、有益さは主観的。 | 素早い応答、創造的スタイル、有益さは主観的。 | 素早い応答、創造的スタイル、有益さは主観的。 | 中程度の応答時間、創造的スタイル、有益さは主観的。 | 素早い応答、創造的スタイル、提案されたフォローアップ付きで有益さは主観的。 | 中程度の応答時間、創造的スタイル、有益さは主観的。 | 素早い応答、創造的スタイル、有益さは主観的。 |
| 『グレート・ギャツビー』のプロットを要約して。 | 素早い応答、簡潔なスタイル、正確な要約、非常に有益。 | 素早い応答、詳細なスタイル、正確な要約、非常に有益。 | 素早い応答、形式的スタイル、主要なテーマを含む正確な要約、非常に有益。 | 中程度の応答時間、会話スタイル、正確な要約、有益。 | 素早い応答、簡潔なスタイル、出典付きの正確な要約、非常に有益。 | 中程度の応答時間、会話スタイル、正確な要約、有益。 | 素早い応答、簡潔なスタイル、正確な要約、有益。 |

**5. 各チャットボットの強みと弱み**

1週間の対話により、各AIチャットボットの明確な強みが明らかになりました。ChatGPTは、強力な一般知識と創造的な文章作成能力を示し、広範な機能セットと使いやすさと相まって、汎用ツールとしての評判に沿うものでした 3。Google Geminiは、創造的なタスクで優れ、素早い応答を提供し、Googleエコシステムとのシームレスな統合の恩恵を受けました 3。Microsoft Copilotは、Microsoft 365アプリケーションとの統合、出典の表示を伴う最新イベントへのアクセス能力、そして高度なモデルの無料での利用可能性で際立っていました 3。Claudeは、特に大規模な入力を処理し、微妙なニュアンスのある会話に従事することに特に長けており、倫理的AIへの配慮とユーザープライバシーへの注目すべき重点が示されました 5。Perplexityは、詳細なインターネット検索の優れたツールとして際立ち、一貫してその主張に対する出典を提供し、役立つフォローアッププロンプトを提供しました 3。HuggingChatの主な強みは、そのオープンソース性にあり、ユーザーに様々なAIモデルへのアクセスを許可し、コミュニティ主導のアプローチを促進します 3。最後に、DeepSeekは、強力な推論能力と効率的なハードウェア活用を披露し、ユーザーに無料でアクセス可能であることを示しました 3。

逆に、評価は各チャットボットに関連する特定の弱点も強調しました。その強みにもかかわらず、ChatGPTは不正確な情報を生成する可能性を示し、無料版には特定の制限があります 4。Google Geminiも、時折不正確さや「幻覚」を起こしやすく、比較的閉鎖的なエコシステム内で動作することが観察されました 74。Microsoft Copilotは、能力があるにもかかわらず、時折基盤となるChatGPTモデルの劣化版のように感じられ、本質的にBingの検索結果に結びついています 3。Claudeは、特定の領域で強力である一方、より大きな競合他社と比較して市場浸透率が低く、そのトレーニングデータの知識カットオフ日付がある可能性があります 5。Perplexityのインターフェースは、一部のユーザーには煩雑に感じられる可能性があり、その最も高度な機能への完全なアクセスには有料サブスクリプションが必要です 3。HuggingChatは、オープンソースプロジェクトであるため、不正確な情報を生成する傾向も示し、応答時間が遅くなる可能性があり、言語のニュアンスに苦労する可能性があります 32。DeepSeekは、推論において強力である一方、組み込まれた検閲メカニズムがあり、そのインターフェースはより確立されたプラットフォームの洗練さを欠いている可能性があります 55。

**6. 主な相違点のまとめ**

1週間の評価は、AIチャットボットの能力、制限、およびユーザーインターフェースにおけるいくつかの重要な相違点を明らかにしました。能力に関しては、ChatGPTは、推論、創造的作文、事実の想起、要約を含む様々なタスクにわたる広範な熟練度を示しました。Google Geminiも、創造的生成と迅速な情報検索において強みを示し、Googleサービスへの統合が進んでいます。Microsoft Copilotは、その検索統合と出典表示による研究、およびMicrosoft Officeスイート内での有用性で優れていました。Claudeは、大規模な文書を処理する能力と、詳細かつ倫理的に意識した応答を生成することに重点を置いている点で際立っていました。Perplexityは、詳細な研究を実施し、出典引用を通じて検証可能な情報を提供することにおいて特に強力でした。HuggingChatは、多様なオープンソースAIモデルへのアクセスを提供する独自の能力を提供し、異なるアーキテクチャを探求することに興味のあるユーザーに対応しました。DeepSeekは、高度な推論タスクとコーディング支援に特化し、強力な無料代替としての位置を確立しました。

観察された制限も様々でした。正確性、または「幻覚」を起こす傾向は、ChatGPT、Google Gemini、HuggingChatにとって懸念事項でした。知識のカットオフは、Claudeのような一部のチャットボットが最新の情報を提供する能力に影響を与える可能性があります。会話から記憶できる情報量を決定するコンテキストウィンドウのサイズは、これらのモデル間でおそらく異なりますが、これはこの評価では明示的にテストされませんでした。トレーニングデータに内在するバイアスは、すべての大規模言語モデルにとって潜在的な制限です。検閲は、DeepSeekの特定の制限として指摘されました。最後に、最も高度な機能にアクセスするためのコストは、一部のチャットボットは堅牢な無料階層を提供する一方、他のチャットボットは完全な機能性のためにサブスクリプションを必要とするため、様々でした。

ユーザーインターフェースの設計と機能も顕著な違いを示しました。ChatGPTは、一般的にクリーンで直感的なインターフェースを、チャット履歴やカスタム指示などの機能とともに提供します。Google Geminiのインターフェースは、GoogleのWeb上の存在感およびその他のアプリケーションと統合されています。Microsoft Copilotは、専用のWebインターフェースおよびWindowsとOfficeアプリケーション内での統合を含む、様々なMicrosoftプラットフォームを通じてアクセス可能です。Claudeのインターフェースは最小限で、主にチャットインタラクションに焦点を当て、応答スタイルを調整するオプションがあります。Perplexityのインターフェースは検索バーを中心として、その検索指向の機能性を強調しています。HuggingChatのインターフェースは straightforward で、ユーザーが異なる基盤モデルを簡単に選択できるようにします。DeepSeekのインターフェースは、機能的である一方、他のプラットフォームに見られる高度なデザイン要素を欠いている可能性があります。表3は、これらの主な相違点の簡潔な概要を提供します。

**表3: AIチャットボット間の主な相違点のまとめ**

| 特徴 | ChatGPT | Google Gemini | Microsoft Copilot | Claude | Perplexity | HuggingChat | DeepSeek |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **能力** | 広範な一般知識、創造的作文、コーディング、要約、広範な機能。 | 創造的作文、迅速な情報検索、コーディング、Googleサービスとの統合。 | 出典表示を伴う研究、Microsoft 365との統合、最新イベントへのアクセス。 | 大規模文書の分析、微妙なニュアンスのある会話、倫理的AIへの重点。 | 詳細な研究、事実確認、出典引用、フォローアッププロンプト。 | 様々なAIモデルへのアクセス、オープンソース、コミュニティ主導。 | 強力な推論、コーディング支援、効率的なハードウェア活用。 |
| **制限** | 幻覚の可能性、無料版の制限。 | 幻覚を起こしやすい、閉鎖的なエコシステム。 | ChatGPT-liteのように感じられる、Bing検索に基づく。 | 市場浸透率が低い、知識カットオフの可能性。 | インターフェースが煩雑に感じられる可能性、完全アクセスのための有料サブスクリプション。 | 幻覚を起こしやすい、応答が遅くなる可能性、微妙な言語に苦労する可能性。 | 組み込み検閲、インターフェースの洗練度が低い可能性。 |
| **ユーザーインターフェース** | クリーンで直感的、チャット履歴、カスタム指示、モバイルアプリ。 | GoogleのWeb上の存在感およびアプリと統合、Canvasコラボレーション機能、音声会話。 | Webおよびアプリ経由でアクセス可能、WindowsおよびOfficeに統合、Copilot Pages、画像生成。 | 最小限、チャット中心、応答スタイル調整オプション、アップロード機能。 | 検索バー中心、Home, Discover, Spaces, Library機能、多言語サポート、Androidアプリ。 | シンプル、モデル選択、プロンプト例、Web検索、画像生成、PDFアップロード。 | シンプルなWebベースのチャットインターフェース、リアルタイムチャット、永続的なチャット履歴。 |

**7. タスク適合性の推奨事項**

1週間の比較に基づくと、各AIチャットボットは特定の種類のタスクに最も適しているようです。ChatGPTの広範な能力は、一般的なブレインストーミング、様々な形式にわたるコンテンツ作成、コーディング支援、学習のための新しいトピックの探求に強力な選択肢となります。Google Geminiは、創造的な文章作成の取り組み、迅速な情報検索、およびGoogleのサービススイートとの統合の恩恵を受けるタスクに特に適しています。Microsoft Copilotは、出典表示が重要な研究シナリオ、およびMicrosoft Officeエコシステム内で広く作業するユーザー向けに、文書起草と要約のためのシームレスな統合を提供することで光ります。Claudeの長文書の処理と要約における強みは、その倫理的配慮への重点と相まって、研究論文、法的文書、または微妙な理解と責任あるAIが最も重要であるあらゆるタスクの分析に理想的です。Perplexityは、詳細な研究と事実確認のための頼りになるツールとして登場し、明確な引用を伴う豊富な情報を提供し、学術的または調査目的に優れています。HuggingChatは、異なるオープンソースAIモデルの能力を探求することに興味のあるユーザー、およびオープンソースソリューションの透明性と柔軟性を高く評価するユーザーにとって貴重なプラットフォームです。最後に、DeepSeekの堅牢な推論能力とコーディングの熟練度は、複雑な問題解決タスク、および強力で無料のAIアシスタントを求めるユーザー向けの強力な候補として位置づけます。

例えば、ユーザーがマーケティングメールを素早く下書きする必要がある場合、その創造的なテキスト生成能力により、ChatGPTまたはGoogle Geminiが効率的な選択肢となる可能性があります。しかし、タスクが長い法的文書を分析し重要な条項を特定することを含む場合、Claudeの大きなコンテキストウィンドウがそれをより適切なオプションにする可能性が高いです。特定の歴史的出来事について研究を行っている学生にとっては、Perplexityの情報源を提供する能力が非常に有益です。コードのデバッグの支援を求めるソフトウェア開発者は、DeepSeekの推論能力が特に有用だと感じるかもしれません。逆に、高い正確性と信頼性を必要とするタスクにHuggingChatを使用することは、その幻覚を起こしやすいという報告を考えると、あまり推奨されないかもしれません。同様に、Microsoftエコシステム外の創造的タスクにMicrosoft Copilotを依存することは、その主な強みを活用しないかもしれません。

**8. 結論**

これら7つの公開AIチャットボットの比較研究は、それぞれが独自の強みと弱みのセットを持つ、多様なツールの状況を明らかにしています。評価されたすべてのチャットボットは、自然言語処理と生成における印象的な能力を示していますが、それらのアプローチ、提供する情報の深さ、ユーザーインターフェース設計、および特定のタスクへの適合性において大きく異なります。AIチャットボット技術の急速な進歩は明らかであり、ユーザーに生産性、創造性、および情報へのアクセスを強化するための増大する選択肢の配列を提供しています。この分野が進化し続けるにつれて、将来のトレンドには、特定の業界や使用事例に合わせてさらに特化されたチャットボット、正確性と信頼性のさらなる改善、および他のデジタルツールやプラットフォームとのよりシームレスな統合が含まれる可能性が高いです。最終的に、AIチャットボットを効果的に活用する鍵は、各ツールの独自の特性を理解し、手元のタスクの特定の要件に最も合ったものを選択することにあります。

#### **参考文献**

1. Top Generative AI Chatbots by Market Share – March 2025 \- First Page Sage, accessed March 22, 2025, [https://firstpagesage.com/reports/top-generative-ai-chatbots/](https://firstpagesage.com/reports/top-generative-ai-chatbots/)
2. List of chatbots \- Wikipedia, accessed March 22, 2025, [https://en.wikipedia.org/wiki/List\_of\_chatbots](https://en.wikipedia.org/wiki/List_of_chatbots)
3. The best AI chatbots in 2025 | Zapier, accessed March 22, 2025, [https://zapier.com/blog/best-ai-chatbot/](https://zapier.com/blog/best-ai-chatbot/)
4. The best AI chatbots of 2025: ChatGPT, Copilot, and notable ..., accessed March 22, 2025, [https://www.zdnet.com/article/best-ai-chatbot/](https://www.zdnet.com/article/best-ai-chatbot/)
5. The Best AI Chatbots & LLMs of Q1 2025: Rankings & Data \- UpMarket, accessed March 22, 2025, [https://www.upmarket.co/blog/the-best-ai-chatbots-llms-of-q1-2025-complete-comparison-guide-and-research-firm-ranks/](https://www.upmarket.co/blog/the-best-ai-chatbots-llms-of-q1-2025-complete-comparison-guide-and-research-firm-ranks/)
6. It's June 2024, which AI Chat Bot Are You Using? : r/ClaudeAI \- Reddit, accessed March 22, 2025, [https://www.reddit.com/r/ClaudeAI/comments/1dcjaso/its\_june\_2024\_which\_ai\_chat\_bot\_are\_you\_using/](https://www.reddit.com/r/ClaudeAI/comments/1dcjaso/its_june_2024_which_ai_chat_bot_are_you_using/)
7. I finally found a prompt that makes ChatGPT write naturally : r/ChatGPTPromptGenius \- Reddit, accessed March 22, 2025, [https://www.reddit.com/r/ChatGPTPromptGenius/comments/1h2bkrs/i\_finally\_found\_a\_prompt\_that\_makes\_chatgpt\_write/](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1h2bkrs/i_finally_found_a_prompt_that_makes_chatgpt_write/)
8. Tips for Customizing ChatGPT Responses? \- Reddit, accessed March 22, 2025, [https://www.reddit.com/r/ChatGPT/comments/1gs8ok1/tips\_for\_customizing\_chatgpt\_responses/](https://www.reddit.com/r/ChatGPT/comments/1gs8ok1/tips_for_customizing_chatgpt_responses/)
9. 60+ Best Writing Styles For ChatGPT Prompts \- Workflows, accessed March 22, 2025, [https://www.godofprompt.ai/blog/60-best-writing-style-for-chatgpt-prompts](https://www.godofprompt.ai/blog/60-best-writing-style-for-chatgpt-prompts)
10. Examples of ChatGPT Generated Text \- Center for Teaching and Learning, accessed March 22, 2025, [https://ctl.wustl.edu/examples-of-chatgpt-generated-text/](https://ctl.wustl.edu/examples-of-chatgpt-generated-text/)
11. How to train ChatGPT to write like you \- Zapier, accessed March 22, 2025, [https://zapier.com/blog/train-chatgpt-to-write-like-you/](https://zapier.com/blog/train-chatgpt-to-write-like-you/)
12. How to Train Your Employees to Use Microsoft 365 Copilot \- Blue Mantis, accessed March 22, 2025, [https://www.bluemantis.com/blog/how-to-write-generative-ai-prompts/](https://www.bluemantis.com/blog/how-to-write-generative-ai-prompts/)
13. Learn about Copilot prompts \- Microsoft Support, accessed March 22, 2025, [https://support.microsoft.com/en-us/topic/learn-about-copilot-prompts-f6c3b467-f07c-4db1-ae54-ffac96184dd5](https://support.microsoft.com/en-us/topic/learn-about-copilot-prompts-f6c3b467-f07c-4db1-ae54-ffac96184dd5)
14. How to Write the Perfect Prompts for Microsoft Copilot \- Kevin Stratvert, accessed March 22, 2025, [https://kevinstratvert.com/2024/08/22/how-to-write-the-perfect-prompts-for-microsoft-copilot/](https://kevinstratvert.com/2024/08/22/how-to-write-the-perfect-prompts-for-microsoft-copilot/)
15. Seven Tips for Having a Great Conversation with Copilot \- Microsoft, accessed March 22, 2025, [https://www.microsoft.com/en-us/worklab/seven-tips-for-having-a-great-conversation-with-copilot](https://www.microsoft.com/en-us/worklab/seven-tips-for-having-a-great-conversation-with-copilot)
16. Maximizing Microsoft Copilot Efficiency with Clear Prompts \- Convergence Networks, accessed March 22, 2025, [https://convergencenetworks.com/blog/maximizing-copilot-efficiency-tips-on-crafting-clear-and-specific-prompts/](https://convergencenetworks.com/blog/maximizing-copilot-efficiency-tips-on-crafting-clear-and-specific-prompts/)
17. ‎What Gemini Apps can do and other frequently asked questions, accessed March 22, 2025, [https://gemini.google.com/faq](https://gemini.google.com/faq)
18. Prompt design strategies | Gemini API | Google AI for Developers, accessed March 22, 2025, [https://ai.google.dev/gemini-api/docs/prompting-strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
19. Generate text responses using Gemini API with external function calls in a chat scenario, accessed March 22, 2025, [https://cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-function-calling-chat](https://cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-function-calling-chat)
20. Generate structured output with the Gemini API | Google AI for Developers, accessed March 22, 2025, [https://ai.google.dev/gemini-api/docs/structured-output](https://ai.google.dev/gemini-api/docs/structured-output)
21. 7 examples of Gemini's multimodal capabilities in action \- Google Developers Blog, accessed March 22, 2025, [https://developers.googleblog.com/en/7-examples-of-geminis-multimodal-capabilities-in-action/](https://developers.googleblog.com/en/7-examples-of-geminis-multimodal-capabilities-in-action/)
22. Claude AI Custom Styles \- Personalize AI Tone & Responses, accessed March 22, 2025, [https://claudeaihub.com/claude-ai-custom-styles/](https://claudeaihub.com/claude-ai-custom-styles/)
23. Tailor Claude's responses to your personal style \- Anthropic, accessed March 22, 2025, [https://www.anthropic.com/news/styles](https://www.anthropic.com/news/styles)
24. Configuring and Using Styles | Anthropic Help Center, accessed March 22, 2025, [https://support.anthropic.com/en/articles/10181068-configuring-and-using-styles](https://support.anthropic.com/en/articles/10181068-configuring-and-using-styles)
25. Customizing Claude's Response Style: A New Feature by Anthropic \- AI In Transit, accessed March 22, 2025, [https://aiintransit.medium.com/customizing-claudes-response-style-a-new-feature-by-anthropic-d341da146c25](https://aiintransit.medium.com/customizing-claudes-response-style-a-new-feature-by-anthropic-d341da146c25)
26. Make Your AI Writing Sound More Like You, with Claude Writing Styles \- Alitu, accessed March 22, 2025, [https://alitu.com/creator/content-creation/ai-writing-claude-styles/](https://alitu.com/creator/content-creation/ai-writing-claude-styles/)
27. Prompting tips and examples | Perplexity Help Center, accessed March 22, 2025, [https://www.perplexity.ai/help-center/en/articles/10354321-prompting-tips-and-examples](https://www.perplexity.ai/help-center/en/articles/10354321-prompting-tips-and-examples)
28.