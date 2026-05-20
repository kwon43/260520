import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('권민솔의 웹앱')
st.write('반갑습니다!!🙌')

# 1. 페이지 기본 설정 (가장 상단에 위치해야 합니다)
st.set_page_config(
    page_title="권민솔의 스페이스",
    page_icon="🚀",
    layout="centered"
)

# 2. 사이드바 메뉴 구성
with st.sidebar:
    st.markdown("# 🧭 Navigation")
    menu = st.radio(
        "이동할 페이지를 선택하세요:",
        ["홈 (Home)", "내 능력치 (Analytics)", "방명록 (Guestbook)"]
    )
    st.divider()
    st.caption("© 2026 권민솔. All rights reserved.")

# 3. 메뉴별 페이지 구현
# --- 홈 화면 ---
if menu == "홈 (Home)":
    st.title('🚀 권민솔의 웹앱')
    st.subheader('반갑습니다!! 🙌 저의 공간에 오신 것을 환영합니다.')
    
    # 멋진 이미지나 카드 스타일 레이아웃 (Layout Columns)
    col1, col2 = st.columns([1, 2])
    with col1:
        # 이모지로 프로필 이미지 대체
        st.markdown("<h1 style='text-align: center; font-size: 80px;'>🧑‍💻</h1>", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        ### Intro
        - **Name:** 권민솔
        - **Interest:** 웹 앱 개발, 데이터 분석, 인공지능
        - **Goal:** Streamlit으로 세상에 유용한 서비스 만들기!
        """)
    
    st.divider()
    st.info("💡 왼쪽 사이드바 메뉴를 클릭해 다른 페이지도 구경해 보세요!")

# --- 능력치 화면 ---
elif menu == "내 능력치 (Analytics)":
    st.title('📊 나의 역량 분석 그래프')
    st.write('현재 집중하고 있는 분야와 성장 곡선입니다.')
    
    # 샘플 데이터 생성
    chart_data = pd.DataFrame(
        np.random.randn(20, 3) + [1, 2, 5],
        columns=['Python', 'Streamlit', 'UI/UX 디자인']
    )
    
    # 멋진 라인 차트 시각화
    st.line_chart(chart_data)
    
    # 메트릭(지표) 표시
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Python 숙련도", value="85%", delta="+5%")
    col2.metric(label="Streamlit 경험", value="92%", delta="+12% 🔥")
    col3.metric(label="열정 지수", value="100%", delta="MAX")

# --- 방명록 화면 ---
elif menu == "방명록 (Guestbook)":
    st.title('✍️ 방명록')
    st.write('방문해주신 흔적을 남겨주세요!')
    
    # 사용자 입력 폼
    with st.form("guestbook_form", clear_on_submit=True):
        visitor_name = st.text_input("닉네임", placeholder="이름을 입력하세요")
        message = st.text_area("메시지", placeholder="응원의 한마디를 남겨주세요!")
        submitted = st.form_submit_button("방명록 남기기")
        
        if submitted:
            if visitor_name and message:
                # 성공 애니메이션 트리거
                st.balloons()
                st.success(f"🎉 {visitor_name}님의 소중한 메시지가 등록되었습니다!")
                st.toast("방명록 작성 완료!", icon="✅")
                
                # 입력된 내용 보여주기
                st.markdown(f"**[{visitor_name}]** : {message}")
            else:
                st.error("닉네임과 메시지를 모두 입력해주세요.")
