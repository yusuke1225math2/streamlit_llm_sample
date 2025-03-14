import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import StrOutputParser

# 環境変数の読み込み
load_dotenv()

# ページ設定
st.set_page_config(page_title="専門家AIアシスタント", page_icon="🧠", layout="wide")

# アプリのタイトルとガイド
st.title("専門家AIアシスタント")
st.markdown("""
### アプリの使い方
1. 下のラジオボタンから相談したい専門家を選択してください
2. テキスト入力欄に質問や相談内容を入力してください
3. 「送信」ボタンをクリックすると、選択した専門家としてAIが回答します
""")

# 専門家の種類と対応するシステムメッセージ
expert_types = {
    "医療専門家": "あなたは医療の専門家です。医学的な知識に基づいて、健康や病気に関する質問に答えてください。ただし、診断や治療の代わりにはならないことを明示してください。",
    "プログラミング専門家": "あなたはプログラミングの専門家です。コードの書き方、デバッグ、アルゴリズム、ベストプラクティスなどについて詳しく説明してください。",
    "料理専門家": "あなたは料理の専門家です。レシピ、調理技術、食材の選び方、料理のコツなどについて詳しく説明してください。",
    "金融アドバイザー": "あなたは金融の専門家です。投資、貯蓄、予算管理などの金融アドバイスを提供してください。ただし、個別の投資アドバイスではなく一般的な情報提供に留めてください。",
}


def get_llm_response(input_text, expert_type):
    """
    入力テキストとラジオボタンでの選択値を引数として受け取り、LLMからの回答を返す関数

    Args:
        input_text (str): ユーザーからの入力テキスト
        expert_type (str): 選択された専門家の種類

    Returns:
        str: LLMからの回答
    """
    # システムメッセージの取得
    system_message = expert_types[expert_type]

    # LLMの初期化
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
    )

    # プロンプトテンプレートの作成
    prompt = ChatPromptTemplate.from_messages(
        [("system", system_message), ("human", "{input}")]
    )

    # LangChainのチェーンを作成
    chain = prompt | llm | StrOutputParser()

    # 入力テキストを処理して回答を取得
    response = chain.invoke({"input": input_text})

    return response


# 専門家選択のラジオボタンを配置（アプリの使い方説明欄の下）
st.header("専門家を選択")
selected_expert = st.radio(
    "どの専門家に相談しますか？", list(expert_types.keys())
)

# メインエリアに入力フォームを配置
st.subheader(f"選択中の専門家: {selected_expert}")
user_input = st.text_area("質問や相談内容を入力してください:", height=150)

# 送信ボタン
if st.button("送信"):
    if user_input:
        with st.spinner("回答を生成中..."):
            # LLMからの回答を取得
            response = get_llm_response(user_input, selected_expert)

            # 回答を表示
            st.subheader("回答:")
            st.markdown(response)
    else:
        st.error("質問や相談内容を入力してください。")

# フッター
st.markdown("---")
st.markdown(
    "このアプリはLangChainとOpenAI APIを使用しています。実際の専門家のアドバイスの代わりにはなりません。"
)
