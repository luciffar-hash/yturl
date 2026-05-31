import streamlit as st
import re

# 定義版本號
VERSION = "v1.1.0"

# ==========================================
# 1. 核心邏輯：極光裁決（精準斬斷雜訊，擷取影片 ID）
# ==========================================
def extract_yt_id(url):
    pattern = r'(?:v=|\/v\/|embed\/|shorts\/|\.be\/|\/embed\/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None

# ==========================================
# 2. 網頁介面設定（使用定案的霸氣中英文標題）
# ==========================================
st.title("路西法智庫極光裁決:YT縮網址")
st.subheader("Luciffar Think Tank - Aurora Judgment: YT URL Purifier")

st.markdown("---") # 畫一條分隔線

# ==========================================
# 3. 初始化狀態管理（用於實現清除功能）
# ==========================================
if "url_input" not in st.session_state:
    st.session_state.url_input = ""

# 定義清除邏輯的函式
def clear_text():
    st.session_state.url_input = ""

# ==========================================
# 4. 使用者輸入互動區
# ==========================================
# 加入 Enter 的中英文提示在標題中
raw_url = st.text_input(
    "請投入欲淨化的 YouTube 原始長網址 (請按 Enter 鍵或點擊下方裁決按鈕) / Please enter the YouTube URL (Press Enter or click the button below):", 
    placeholder="https://www.youtube.com/watch?v=...",
    key="url_input"
)

# 建立第一組按鈕：裁決與清除
col1, col2 = st.columns([1, 4])
with col1:
    # 點擊按鈕或直接按 Enter 都會觸發
    judge_button = st.button("⚖️ 裁決 / Judge", type="primary")
with col2:
    # 點擊清除按鈕會清空輸入框
    st.button("🧹 清除輸入 / Clear Input", on_click=clear_text)

# ==========================================
# 5. 裁決與輸出
# ==========================================
# 當使用者有輸入，且（按了 Enter 或 點了裁決按鈕）時才執行
if raw_url and (judge_button or raw_url != ""):
    video_id = extract_yt_id(raw_url)
    
    if video_id:
        short_url = f"https://youtu.be/{video_id}"
        
        st.success("裁決成功！已消除所有雜訊參數。/ Purification successful!")
        
        # 使用 st.code 呈現，它本身就內建了側邊的「一鍵複製」按鈕
        st.code(short_url)
        
        # 建立第二組按鈕：針對輸出格的複製提示與清除
        col3, col4 = st.columns([1.5, 3.5])
        with col3:
            # 提示使用者可以使用內建複製
            st.caption("☝️ 請點擊右側按鈕複製 / Click icon to copy")
        with col4:
            # 清除輸出（透過重置輸入框達成）
            st.button("❌ 清除結果 / Clear Result", on_click=clear_text)
            
    else:
        st.error("無法解析！請確認是否為正確的 YouTube 連結。/ Invalid YouTube URL.")

# ==========================================
# 6. 頁尾版號呈現
# ==========================================
st.markdown("---")
st.caption(f"路西法智庫核心組件 • 目前版本：{VERSION}")
