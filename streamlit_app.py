import streamlit as st
from googleapiclient.discovery import build

# YouTube Data API v3のAPIキー
api_key = "AIzaSyCckGeP71CF5741HVdr5sO7-2fEVqORgc0"

# YouTube APIクライアントの作成
youtube = build('youtube', 'v3', developerKey=api_key)

# ビデオID
video_id = "x_BjvhMW9TE"

# ビデオの統計情報を取得
request = youtube.videos().list(part="statistics", id=video_id)
response = request.execute()

# 再生回数を取得
view_count = response['items'][0]['statistics']['viewCount']

# Streamlitで表示
st.line_chart(view_count)
