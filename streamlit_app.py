import streamlit as st

st.set_page_config(page_title="산리오 감정 표현기")
st.title("🎀 산리오 감정 표현기 🎀")
st.write("오늘 기분을 선택하면 어울리는 산리오 캐릭터를 알려드려요!")

# 산리오 캐릭터 데이터 (감정 10개)
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
    },
    "슬픔": {
        "name": "쿠로미",
        "message": "슬플 땐 쿠로미처럼 시크하게 마음을 추스르세요 😈",
        "img": "https://i.pinimg.com/736x/f5/06/81/f5068121409b9ba574b6b62c328df5bb.jpg"
    },
    "긴장": {
        "name": "포차코",
        "message": "긴장될 땐 포차코처럼 귀엽게 힘내보세요 🐶",
        "img": "https://i.pinimg.com/736x/33/22/86/3322866bafc8b3b2383559389b73d43a.jpg"
    },
    "심심": {
        "name": "한교동",
        "message": "심심할 땐 한교동처럼 신나게 놀아보세요 😼",
        "img": "https://i.pinimg.com/736x/98/fd/a3/98fda35ec98e61dc07dc7a6e9bb7690b.jpg"
    },
    "흥분": {
        "name": "케로케로케로피",
        "message": "흥분되는 순간엔 케로피처럼 즐겁게 뛰어보세요 🐸",
        "img": "https://i.pinimg.com/736x/e9/a9/d3/e9a9d361b4cb207dc046bc243e056fd3.jpg"
    },
    "평온": {
        "name": "리틀트윈스타",
        "message": "평온할 땐 리틀트윈스타처럼 마음을 차분히 해보세요 🌟",
        "img": "https://i.pinimg.com/736x/9a/8d/8b/9a8d8b12c64b44324aef5b7b36d7c1e5.jpg"
    },
    "놀람": {
        "name": "배드마츠마루",
        "message": "놀랐을 땐 배드마츠마루처럼 깜짝 귀여운 표정을 지어보세요 🐥",
        "img": "https://i.pinimg.com/736x/ce/75/d6/ce75d6d90da93464f72479fcc79db579.jpg"
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
