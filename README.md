# 専門家AIアシスタント

LangChainとOpenAI APIを使用した専門家AIアシスタントアプリケーションです。ユーザーは専門家の種類を選択し、質問を入力することで、選択した専門家としてAIが回答します。

## 機能

- 複数の専門家（医療、プログラミング、料理、金融）から選択可能
- テキスト入力フォームで質問を送信
- 選択した専門家の役割に基づいたAI回答の生成

## 使用技術

- Python 3.12.5
- Streamlit
- LangChain
- OpenAI API

## セットアップ方法

※ python 3.12.5 を推奨

1. リポジトリをクローンします

```bash
git clone <リポジトリURL>
cd <リポジトリ名>
```

2.必要なパッケージをインストールします

```bash
pip install -r requirements.txt
```

3.`.env`ファイルを作成し、OpenAI APIキーを設定します

```.env
OPENAI_API_KEY=your_openai_api_key_here
```

4.アプリケーションを実行します

```python
streamlit run app.py
```

## Streamlit Community Cloudへのデプロイ

1. GitHubにリポジトリをプッシュします
2. Streamlit Community Cloudにログインします
3. 「New app」をクリックし、GitHubリポジトリを選択します
4. Python 3.11を選択し、デプロイします

## GitHubアップロード時の注意点

1. `.env`ファイルをGitHubにアップロードしないでください（APIキーが漏洩する可能性があります）
2. `.gitignore`ファイルに`.env`を追加してください
3. 大きなファイルやキャッシュファイルもアップロードしないようにしてください
4. 機密情報が含まれていないか確認してください

## ライセンス

MITライセンス
