import streamlit as st
import re

# 定義版本號
VERSION = "v1.1.1"

# ==========================================
# 1. 核心邏輯：極光裁決（升級版：支援 live/ 直播網址）
# ==========================================
def extract_yt_id(url):
    # 加入了 live\/ 的捕捉規則
    pattern = r'(?:v=|\/v\/|embed\/|shorts\/|live\/|\.be\/|\/embed\/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None

# ==========================================
# 2. 網頁介面設定
# ==========================================
st.title("路西法智庫極光裁決:YT縮網址")
st.subheader("Luciffar Think Tank - Aurora Judgment: YT URL Purifier")

st.markdown("---") # 畫一條分隔線

# ==========================================
# 3. 初始化狀態管理
# ==========================================
if "url_input" not in st.session_state:
    st.session_state.url_input = ""

def clear_text():
    st.session_state.url_input = ""

# ==========================================
# 4. 使用者輸入互動區
# ==========================================
raw_url = st.text_input(
    "請投入欲淨化的 YouTube 原始長網址 (請按 Enter 鍵或點擊下方裁決按鈕) / Please enter the YouTube URL (Press Enter or click the button below):", 
    placeholder="https://www.youtube.com/watch?v=... 或 https://www.youtube.com/live/...",
    key="url_input"
)

# 建立第一組按鈕
col1, col2 = st.columns([1, 4])
with col1:
    judge_button = st.button("⚖️ 裁決 / Judge", type="primary")
with col2:
    st.button("🧹 清除輸入 / Clear Input", on_click=clear_text)

# ==========================================
# 5. 裁決與輸出
# ==========================================
if raw_url and (judge_button or raw_url != ""):
    video_id = extract_yt_id(raw_url)
    
    if video_id:
        short_url = f"https://youtu.be/{video_id}"
        
        st.success("裁決成功！已消除所有雜訊參數。/ Purification successful!")
        st.code(short_url)
        
        # 建立第二組按鈕
        col3, col4 = st.columns([1.5, 3.5])
        with col3:
            st.caption("☝️ 請點擊右側按鈕複製 / Click icon to copy")
        with col4:
            st.button("❌ 清除結果 / Clear Result", on_click=clear_text)
            
    else:
        st.error("無法解析！請確認是否為正確的 YouTube 連結。/ Invalid YouTube URL.")

# ==========================================
# 6. 頁尾版號呈現
# ==========================================
st.markdown("---")
st.caption(f"路西法智庫核心組件 • 目前版本：{VERSION}")
