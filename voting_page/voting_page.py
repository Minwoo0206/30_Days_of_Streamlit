import gspread
import pandas as pd
import streamlit as st
from pathlib import Path
from PIL import Image

image_folder = Path("voting_page/images")
image_files = list(image_folder.glob('*'))
questions = []
for idx, image_dir in enumerate(image_files):   
    image = Image.open(image_dir)
    st.image(image)
    question = st.slider(f"'realism' or 'illustration'?(Q{idx})", 0, 10, 5)
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
        st.write("이름을 입력하세요.")