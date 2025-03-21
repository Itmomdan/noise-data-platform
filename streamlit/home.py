import streamlit as st
from streamlit_option_menu import option_menu
from login import Login_page
from Mypage import Mypage_page
from Dashboard import Dashboard_page
from signup import Signup_page
from home_about import About_page
from home_noisemodel import NoiseModel_page
from home_statistics import Statistics_page
from mypage_edit import Edit_page

class Home_page:
    def __init__(self):
        self.Login = Login_page()
        self.Mypage = Mypage_page()  # Mypage_page 초기화
        self.Dashboard = Dashboard_page()  # Dashboard_page 초기화
        self.Signup = Signup_page()
        self.About = About_page()
        self.NoiseModel = NoiseModel_page()
        self.Statistics = Statistics_page()
        self.Edit = Edit_page()

    def main(self, choose=None):
        menu = ["홈","로그인","회원가입", "마이페이지"]

        # 메뉴 선택에 따라 페이지 전환
        if choose == menu[0]: # 메인 홈화면
            self.bar() 
        elif choose == menu[1]: #login
            self.Login.run()
        elif choose == menu[2]: #회원가입
            self.Signup.run()   
        elif choose == menu[3]:  # 마이페이지 선택
            self.Edit.run()  # Mypage_page 실행
                
    def bar(self):
        col, col1, col2, col3 = st.columns([2, 3, 1.5, 1])
        # 상단 중앙: 로고
        with col1:
            st.image("logo.png", width=200)
        # 상단 오른쪽: 반려묘 선택
        # with col3:
        #     self.petsv.printMyCat(print1=False)

        st.write('#')
        # 사이드바 홈 안의 네비게이션바 설정
        nav = ["About", "소음 분류기", "통계 분석"]
        select = option_menu(None, nav,
                             icons=['house', 'camera fill', 'book'], #사진 추후 수정 
                             default_index=0,
                             styles={
                                 "container": {"padding": "5!important", "background-color": "#fafafa"},
                                 "icon": {"color": "orange", "font-size": "25px"},
                                 "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                                              "--hover-color": "#eee"},
                                 "nav-link-selected": {"background-color": "#02ab21"}
                             }, orientation="horizontal"
                             )
        
        # 로그인 필요 페이지 체크
        if select in [nav[1], nav[2]]:
            if "user_info" not in st.session_state or not st.session_state["user_info"]:
                st.warning("로그인이 필요합니다.")
                return  # 로그인하지 않으면 함수 종료
            
        # 네비게이션바
        if select == nav[0]:
            self.About.about_page()
        if select == nav[1]:
            self.NoiseModel.noisemodel_page()
        if select == nav[2]:
            self.Statistics.statistics_page()    

    def run(self):
        menu = ["홈","로그인","회원가입", "마이페이지"]

        # 사이드바
        with st.sidebar:

            # 세션 상태에서 사용자 이름 가져오기
            if 'user_info' in st.session_state:
                name = st.session_state.user_info['name']
                # 사용자 이름을 사이드바 상단에 표시
                st.markdown(f"<p style='text-align: center; font-weight: bold;'>😊 안녕하세요, {name}님</p>", unsafe_allow_html=True)
                st.write("---")  # 구분선 추가

            choose = option_menu("", menu,
                                 icons=['house', 'bi-clipboard-check', 'gear', 'person lines fill'],
                                 default_index=0
                                 )
        # 네비게이션바에 선택된 페이지 출력
        self.main(choose)

# 앱 실행
if __name__ == "__main__":
    home = Home_page()
    home.run()
