import streamlit as st
import streamlit.components.v1 as components

def show_members():
    st.sidebar.title("Team Members π")
    # TODO: λ©€λ² μκ° μμ±νκΈ°

    st.sidebar.markdown("### Boostcamp AI Tech 4th")

    st.sidebar.markdown('''
        <div class="subtitle">
        π  κΉμ’ν΄ <i class="fa-brands fa-linkedin"></i> <i class="fa-brands fa-github"></i> <br />
        π  μ μμ€ <i class="fa-brands fa-linkedin"></i> <i class="fa-brands fa-github"></i> <br />
        π  μ΄νν¬ <i class="fa-brands fa-linkedin"></i> <i class="fa-brands fa-github"></i> <br />
        π  μ‘°μ¬ν¨ <i class="fa-brands fa-linkedin"></i> <i class="fa-brands fa-github"></i> <br />
        π΅βπ«  νμμ€ <a href="https://www.linkedin.com/in/jphan32/"><i class="fa-brands fa-linkedin"></i></a> <a href="https://github.com/jphan32/"><i class="fa-brands fa-github"></i></a>
        </div>
        ''', unsafe_allow_html=True)