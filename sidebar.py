import streamlit as st
import streamlit.components.v1 as components

def show_members():
    st.sidebar.title("Team Members 🏅")
    # TODO: 멤버 소개 작성하기

    st.sidebar.markdown("### Boostcamp AI Tech 4th")

    st.sidebar.markdown('''
        <div class="subtitle">
        😀  김종해 <i class="fa-brands fa-linkedin"></i> <i class="fa-brands fa-github"></i> <br />
        😀  유영준 <i class="fa-brands fa-linkedin"></i> <i class="fa-brands fa-github"></i> <br />
        😀  이태희 <i class="fa-brands fa-linkedin"></i> <i class="fa-brands fa-github"></i> <br />
        😀  조재효 <i class="fa-brands fa-linkedin"></i> <i class="fa-brands fa-github"></i> <br />
        😵‍💫  한상준 <a href="https://www.linkedin.com/in/jphan32/"><i class="fa-brands fa-linkedin"></i></a> <a href="https://github.com/jphan32/"><i class="fa-brands fa-github"></i></a>
        </div>
        ''', unsafe_allow_html=True)