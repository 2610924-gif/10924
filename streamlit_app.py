import streamlit as st

# 1. 페이지 제목 및 기본 데이터 설정
st.title("💊 개인 맞춤형 영양제 복용 체크리스트")

pills = ["비타민 C", "루테인", "유산균", "오메가3"]
dosages = [1, 1, 1, 2]

# 2. 세션 상태(Session State) 초기화 (새로고침되어도 기록이 유지되도록 함)
if "taken_list" not in st.session_state:
    st.session_state.taken_list = []

# 3. 영양제 권장 복용량 안내 (화면 표시)
st.subheader("📋 영양제별 권장 복용 횟수")
col1, col2 = st.columns(2)

with col1:
    for i in range(len(pills)):
        st.write(f"**{i + 1}. {pills[i]}** (권장: {dosages[i]}회)")

with col2:
    # 기록 초기화 버튼 추가 (테스트하기 편하도록)
    if st.button("🔄 기록 초기화", type="secondary"):
        st.session_state.taken_list = []
        st.rerun()

st.markdown("---")

# 4. 영양제 복용 기록 입력 (Selectbox와 Button 활용)
st.subheader("📥 복용 기록하기")
selected_pill = st.selectbox("방금 복용한 영양제를 선택해주세요:", pills)

if st.button("✅ 복용 기록 추가"):
    st.session_state.taken_list.append(selected_pill)
    st.toast(f"[{selected_pill}]의 복용이 기록되었습니다!")  # 화면 하단에 잠시 뜨는 알림

st.markdown("---")

# 5. 결과 출력 및 목표 달성 체크
total_taken = len(st.session_state.taken_list)
st.metric(label="오늘의 총 영양제 복용 횟수", value=f"{total_taken} 회")

# 목표 복용 횟수 입력 받기
my_target = st.number_input(
    "오늘의 목표 복용 횟수를 입력해주세요:", min_value=0, value=5, step=1
)

# 목표 달성 여부 확인 버튼
if st.button("🏆 목표 달성 확인"):
    if total_taken == my_target:
        st.success("🎉 복용 성공!")
        st.subheader("---[복용 완료 체크리스트]---")
        for item in st.session_state.taken_list:
            st.write(f"- {item}")
    else:
        st.error(f"❌ 복용 실패 (목표인 {my_target}회와 현재 복용 횟수 {total_taken}회가 일치하지 않습니다.)")

# 실시간 복용 현황 리스트 보여주기 (참고용)
if st.session_state.taken_list:
    with st.expander("👀 현재까지 복용한 리스트 보기"):
        st.write(st.session_state.taken_list)