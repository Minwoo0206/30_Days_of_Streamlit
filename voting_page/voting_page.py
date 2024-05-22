import os
import gspread
import pandas as pd
import streamlit as st
from PIL import Image

st.header('ACP 프로토타입 그림 선별', divider='rainbow')

# 설문조사 설명 부분
st.subheader('설명 :sunglasses:')
st.text('''
        여러분은 앞으로 66장의 그림을 보게 될 것이며, 그림이 얼마나 기괴한지 평가할 것입니다.
        그림이 전혀 기괴하지 않다면 1점을, 그림이 매우 기괴하다면 5점을 주세요.
        
        여러분이 보는 그림은 배경 제거 기능을 적용한 그림이므로, 외곽 번짐 혹은 사라짐 현상이 일부 있을 수 있습니다.
        해당 효과는 신경쓰지 않고 평가해주시기 바랍니다.
        ''')

# try:
#     man_real = Image.open("explain/man_real.png")
#     man_anim = Image.open("explain/man_anim.png")
# except:
#     man_real = Image.open("voting_page/explain/man_real.png")
#     man_anim = Image.open("voting_page/explain/man_anim.png")

# st.write("0점은 왼쪽 그림을 기준으로, 10점은 오른쪽 그림을 기준으로 삼습니다.")
# col1, col2 = st.columns(2)
# with col1:
#     st.image(man_real, caption='실제', use_column_width=True)
# with col2:
#     st.image(man_anim, caption='애니메이션', use_column_width=True)

st.text("이해가 다 되었다면 평정을 시작해주세요.")

# 평정 부분
st.header(body="", divider="rainbow")
st.subheader("평정 :sunglasses:")

if os.path.exists("images_processed"):
    image_folder = "images_processed/"
else:
    image_folder = "voting_page/images_processed/"

samples_dir =[]
for idx, image_dir in enumerate(os.listdir(image_folder)):
    if image_dir.split('/')[-1] == '.DS_Store': continue
    samples_dir.append(image_folder+image_dir)
samples_dir.sort()

questions = []
for idx, sample_dir in enumerate(samples_dir):
    sample = Image.open(sample_dir)
    st.image(sample)
    question = st.slider(f"Q{idx+1}. **전혀 기괴하지 않다[1]** - **매우 기괴하다[5]** ({sample_dir.split('/')[-1]})", 1, 5, 3)
    questions.append(question)

# connect gc
credentials = {
    "type": st.secrets['type'],
    "project_id": st.secrets['project_id'],
    "private_key_id": st.secrets['private_key_id'],
    "private_key": st.secrets['private_key'],
    "client_email": st.secrets['client_email'],
    "client_id": st.secrets['client_id'],
    "auth_uri": st.secrets['auth_uri'],
    "token_uri": st.secrets['token_uri'],
    "auth_provider_x509_cert_url": st.secrets['auth_provider_x509_cert_url'],
    "client_x509_cert_url": st.secrets['client_x509_cert_url'],
    "universe_domain": st.secrets['universe_domain']    
}
gc = gspread.service_account_from_dict(credentials)
spreadsheet_url = st.secrets['spreadsheet']
doc = gc.open_by_url(spreadsheet_url)
worksheet = doc.worksheet("Sheet1")

# submit form
st.header(body="", divider="rainbow")
st.subheader("제출 :sunglasses:")

name = st.text_input("이름을 입력하세요.")
submit = st.button('submit')
if submit:
    if name: 
        df = pd.DataFrame(worksheet.get_all_records())
        questions = [name] + questions
        df.loc[len(df)] = questions
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        st.success("설문조사가 완료되었습니다.")
        st.balloons()
    else:
        st.text("이름을 입력하세요.")