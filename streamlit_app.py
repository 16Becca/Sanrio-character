import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="산리오 감정 표현기")
st.title("🎀 산리오 감정 표현기 🎀")
st.write("오늘 기분을 선택하면 어울리는 산리오 캐릭터를 알려드려요!")

# 산리오 캐릭터 데이터 (감정 10개 + 폭죽 색상)
characters = {
    "행복": {"name": "시나모롤", "message": "오늘은 시나모롤처럼 따뜻하고 행복한 하루예요 ☁️🍪",
              "img": "https://i.pinimg.com/1200x/07/ee/d7/07eed72eda898a292169c2b79cd87b72.jpg",
              "color": ["#ffffff", "#87cefa", "#ffb6c1"]},
    "피곤": {"name": "구데타마", "message": "피곤한 하루엔 구데타마처럼 느긋하게 쉬어주세요 🥚",
              "img": "https://i.pinimg.com/736x/e0/08/8e/e0088e011b97af839b5656affce243f1.jpg",
              "color": ["#f5deb3", "#ffe4b5", "#ffdead"]},
    "짜증": {"name": "헬로키티", "message": "짜증 날 땐 헬로키티처럼 귀엽게 마음을 달래봐요 🎀",
              "img": "https://i.pinimg.com/736x/db/05/b0/db05b0391e1708a604eb0e48717397fc.jpg",
              "color": ["#ff69b4", "#ffc0cb", "#ffffff"]},
    "설렘": {"name": "마이멜로디", "message": "설레는 기분엔 마이멜로디처럼 상큼하게 즐겨요 🎀",
              "img": "https://i.pinimg.com/736x/87/04/9a/87049a2daf300ae55cc4c5dcce9719e8.jpg",
              "color": ["#ff69b4", "#fff0f5", "#ffa07a"]},
    "슬픔": {"name": "쿠로미", "message": "슬플 땐 쿠로미처럼 시크하게 마음을 추스르세요 😈",
              "img": "https://i.pinimg.com/736x/f5/06/81/f5068121409b9ba574b6b62c328df5bb.jpg",
              "color": ["#8b008b", "#4b0082", "#000000"]},
    "긴장": {"name": "포차코", "message": "긴장될 땐 포차코처럼 귀엽게 힘내보세요 🐶",
              "img": "https://i.pinimg.com/736x/33/22/86/3322866bafc8b3b2383559389b73d43a.jpg",
              "color": ["#add8e6", "#ffffff", "#87ceeb"]},
    "심심": {"name": "한교동", "message": "심심할 땐 한교동처럼 신나게 놀아보세요 😼",
              "img": "https://i.pinimg.com/736x/98/fd/a3/98fda35ec98e61dc07dc7a6e9bb7690b.jpg",
              "color": ["#ffa500", "#ffdead", "#f0e68c"]},
    "흥분": {"name": "케로케로케로피", "message": "흥분되는 순간엔 케로피처럼 즐겁게 뛰어보세요 🐸",
              "img": "https://i.pinimg.com/736x/e9/a9/d3/e9a9d361b4cb207dc046bc243e056fd3.jpg",
              "color": ["#00ff00", "#7fff00", "#32cd32"]},
    "평온": {"name": "리틀트윈스타", "message": "평온할 땐 리틀트윈스타처럼 마음을 차분히 해보세요 🌟",
              "img": "https://i.pinimg.com/736x/9a/8d/8b/9a8d8b12c64b44324aef5b7b36d7c1e5.jpg",
              "color": ["#87cefa", "#e0ffff", "#f0fff0"]},
    "놀람": {"name": "배드마츠마루", "message": "놀랐을 땐 배드마츠마루처럼 깜짝 귀여운 표정을 지어보세요 🐥",
              "img": "https://i.pinimg.com/736x/ce/75/d6/ce75d6d90da93464f72479fcc79db579.jpg",
              "color": ["#000000", "#ffffff", "#808080"]}
}

# 세션 상태 초기화
if "mood" not in st.session_state:
    st.session_state.mood = None

# 기분 선택
mood_choice = st.radio("오늘의 기분을 선택하세요:", list(characters.keys()))

# 제출 버튼
if st.button("결과 보기"):
    st.session_state.mood = mood_choice

# 결과 출력
if st.session_state.mood:
    character = characters[st.session_state.mood]
    
    # 폭죽용 HTML + JS (components.html 사용, 전체 화면 입체 폭죽)
    colors = character["color"]
    confetti_html = f"""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <canvas id="myCanvas" style="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;"></canvas>
    <script>
        var duration = 2500;
        var animationEnd = Date.now() + duration;
        var defaults = {{ startVelocity: 45, spread: 360, ticks: 100, gravity: 0.8, zIndex: 999 }};
        function randomInRange(min, max) {{ return Math.random() * (max - min) + min; }}
        var interval = setInterval(function() {{
            var timeLeft = animationEnd - Date.now();
            if(timeLeft <= 0) {{
                return clearInterval(interval);
            }}
            // 화면 전체 랜덤 위치에서 폭죽 발생
            var particleCount = 100 * (timeLeft / duration);
            confetti(Object.assign({{
                particleCount: particleCount,
                origin: {{ x: randomInRange(0, 1), y: randomInRange(0, 1) }},
                colors: {colors}
            }}, defaults));
        }}, 200);
    </script>
    """
    components.html(confetti_html, height=0)
    
    st.write(f"**{character['message']}**")
    st.image(character['img'], width=200)
