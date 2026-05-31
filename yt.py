import streamlit as st
import re

# 定義版本號
VERSION = "v1.0.0"

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
# 3. 使用者輸入互動區
# ==========================================
raw_url = st.text_input(
    "請投入欲淨化的 YouTube 原始長網址：", 
    placeholder="https://www.youtube.com/watch?v=..."
)

# ==========================================
# 4. 裁決與輸出
# ==========================================
if raw_url:
    video_id = extract_yt_id(raw_url)
    
    if video_id:
        short_url = f"https://youtu.be/{video_id}"
        st.success("裁決成功！已消除所有雜訊參數。")
        st.code(short_url)
    else:
        st.error("無法解析！請確認是否為正確的 YouTube 連結。")

# ==========================================
# 5. 頁尾版號呈現
# ==========================================
st.markdown("---")
# 用灰色小字（caption）優雅地呈現版號
st.caption(f"路西法智庫核心組件 • 目前版本：{VERSION}")