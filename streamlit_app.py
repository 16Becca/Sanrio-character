import streamlit as st

st.set_page_config(page_title="산리오 감정 표현기")
st.title("🎀 산리오 감정 표현기 🎀")
st.write("오늘 기분을 선택하면 어울리는 산리오 캐릭터를 알려드려요!")

# 산리오 캐릭터 데이터
characters = {
    "행복": {
        "name": "시나모롤",
        "message": "오늘은 시나모롤처럼 따뜻하고 행복한 하루예요 ☁️🍪",
        "img": "https://i.pinimg.com/1200x/07/ee/d7/07eed72eda898a292169c2b79cd87b72.jpg"
    },
    "피곤": {
        "name": "구데타마",
        "message": "피곤한 하루엔 구데타마처럼 느긋하게 쉬어주세요 🥚",
        "img": "https://i.pinimg.com/736x/e0/08/8e/e0088e011b97af839b5656affce243f1.jpg"
    },
    "짜증": {
        "name": "헬로키티",
        "message": "짜증 날 땐 헬로키티처럼 귀엽게 마음을 달래봐요 🎀",
        "img": "https://i.pinimg.com/736x/db/05/b0/db05b0391e1708a604eb0e48717397fc.jpg"
    },
    "설렘": {
        "name": "마이멜로디",
        "message": "설레는 기분엔 마이멜로디처럼 상큼하게 즐겨요 🎀",
        "img": "https://i.pinimg.com/736x/87/04/9a/87049a2daf300ae55cc4c5dcce9719e8.jpg"
    }
}

# 세션 상태 초기화
if "mood" not in st.session_state:
    st.session_state.mood = None

# 라디오 버튼으로 기분 선택
mood_choice = st.radio("오늘의 기분을 선택하세요:", list(characters.keys()))

# 제출 버튼
if st.button("결과 보기"):
    st.session_state.mood = mood_choice

# 결과 출력
if st.session_state.mood:
    character = characters[st.session_state.mood]
    st.write(f"**{character['message']}**")
    st.image(character['img'], width=200)
