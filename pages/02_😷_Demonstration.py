import streamlit as st
from sidebar import show_members
from header import page_header, toastMessage, config
from enum import Enum
from random import randint

from predict import load_model, get_prediction

################################################################################
# Header
page_header()

### Sidebar View ###
show_members()
################################################################################

### Enum Type
class SourceType(Enum):
    Image = 1
    WebCam = 2

### Default Sesseion State
if "source_type" not in st.session_state:
    st.session_state.source_type = SourceType.Image
if "complete_pred" not in st.session_state:
    st.session_state.complete_pred = False
    st.session_state.pred = None
    st.session_state.img_file = None
if "file_uploader_key" not in st.session_state:
    st.session_state.file_uploader_key = str(randint(1000, 100000000))


### Main View
st.title("[CV] 마스크 착용 상태 분류")
st.header("카메라로 촬영한 사람 얼굴 이미지의 마스크 착용 여부를 판단하는 Task")

model = load_model()
toastMessage("[Success] Model loaded", style = "success", wait = 3)

### Columns
params, launcher = st.columns([2, 4], gap="medium")

with launcher:
    st.subheader("Model Inference Result")
    message_placeholder = st.empty()
    result_placeholder = st.empty()

    if st.session_state.complete_pred == False:
        message_placeholder.success("이미지를 업로드 후 실행해주세요")
        result_placeholder.empty()
    else:
        message_placeholder.success(f"Success : {config['classes'][st.session_state.pred]}")
        result_placeholder.image(st.session_state.img_file)

        pass


with params:
    st.subheader("Input")
    st.radio("Select source type", (SourceType.Image.name, SourceType.WebCam.name), disabled=True)
    # TODO: Domain 이슈로 Chrome 등에서 WebCam 접근 권한을 요청하지 못하는 이슈 등 해결 후 구현 예정
    st.text("TODO: ↑ WebCam 추후 구현")

    img_file = st.file_uploader("얼굴 사진 업로드", type=["jpg", "jpeg","png"], key=st.session_state.file_uploader_key)
    if img_file is not None:
        pass
    
    def reset():
        img_file = None
        st.session_state.file_uploader_key = str(randint(1000, 100000000))
        st.session_state.complete_pred = False

    def inference():
        # TODO: placeholder 안에 spinner가 안된다..
        #with message_placeholder.spinner("In Progress..."):
        #    time.sleep(5)
        message_placeholder.warning("In Progress...")
        st.session_state.pred = get_prediction(model, img_file.getvalue()).item()
        st.session_state.img_file = img_file.getvalue()
        st.session_state.complete_pred = True

    # TODO: Columns may not be nested inside other columns..... 안되다니..
    #left, right = st.columns([1, 1], gap="large")
    #with left:
    #    st.button('초기화', on_click=reset)
    #with right:
    #    st.button('실행', on_click=inference)

    st.button('초기화', on_click=reset, type="secondary")
    st.button('실행', on_click=inference, type="primary", disabled=(img_file is None))
