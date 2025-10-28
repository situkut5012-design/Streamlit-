# 売上データ可視化アプリ（Streamlit）

## 💡 概要
PythonとStreamlitで作成した、CSVデータをアップロードするだけで
売上集計とグラフを自動生成する可視化アプリです。


---

## 🛠 使用技術
- Python 3.12
- pandas（データ集計）
- matplotlib / plotly（グラフ描画）
- Streamlit（Webアプリ化）

---

## ⚙️ 機能
1. CSVファイルのアップロード  
2. データプレビュー（表形式）  
3. 月別売上の棒グラフ表示  
4. 顧客別売上の折れ線グラフ表示  
5. 自動グラフ生成と結果の可視化

---

## 🚀 実行方法（ローカル）
1. 仮想環境を有効化
```bash
# PowerShell
.\venv\Scripts\Activate.ps1

2．ライブラリをインストール
pip install -r requirements.txt

3．Streamlitを起動
streamlit run app.py


4．ブラウザが開き、CSVをアップロードしてグラフを確認
プロジェクト構成
streamlit_dashboard/
 ├─ app.py              # メインアプリ
 ├─ sample_data.csv     # テスト用データ
 ├─ requirements.txt    # ライブラリ一覧
 └─ README.md           # 説明ファイル


<img width="881" height="685" alt="image" src="https://github.com/user-attachments/assets/7f914f46-1a7f-4bc5-8d51-fe5d0a2d1ff4" />

