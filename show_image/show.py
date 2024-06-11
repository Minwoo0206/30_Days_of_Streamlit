import random
import streamlit as st
import matplotlib.pyplot as plt

# setting
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False


# title
st.title("동물가족화 기준 만들기")
st.caption("")
st.caption("")


# first header 
st.subheader("아빠-아기 크기 검증")
st.caption("")
keys = ['2배', '4배', '6배', '8배', '10배', '12배', '14배', '16배', '18배', '20배']
values = [38, 37, 25, 16, 8, 8, 11, 10, 15, 22]

c1, c2 = st.columns([3, 2])

with c1:
    fig, ax = plt.subplots()
    ax.bar(keys, values)
    ax.set_ylim(top=40)
    ax.set_xlabel("아빠-아기 크기 비율")
    ax.set_ylabel("왜곡 응답 수")
    ax.set_title("아빠-아기 크기 검증")
    st.pyplot(fig)

with c2:
    picture = st.text_input("원하는 사진을 입력하세요.", key='first')
    dir = "father-child" + '/' + picture + '.png'
    try:
        st.image(dir)
    except:
        st.image("father-child/2배.png")

st.caption("")
st.caption("")


# second header 
st.subheader("엄마-아기 크기 검증")
st.caption("")
keys = ['2배', '4배', '6배', '8배', '10배', '12배', '14배', '16배', '18배', '20배']
values = [39, 26, 16, 9, 9, 11, 16, 25, 35, 35]

c1, c2 = st.columns([3, 2])

with c1:
    fig, ax = plt.subplots()
    ax.bar(keys, values)
    ax.set_ylim(top=40)
    ax.set_xlabel("엄마-아기 크기 비율")
    ax.set_ylabel("왜곡 응답 수")
    ax.set_title("엄마-아기 크기 검증")
    st.pyplot(fig)

with c2:
    picture = st.text_input("원하는 사진을 입력하세요.", key='second')
    dir = "mother-child" + '/' + picture + '.png'
    try:
        st.image(dir)
    except:
        st.image("mother-child/2배.png")

st.caption("")
st.caption("")


# third header
st.subheader("아빠-엄마 크기 검증")
st.caption("")
keys = ['2배', '4배', '6배', '8배', '10배', '12배', '14배', '16배', '18배', '20배']
values = [13, 17, 22, 30, 30, 31, 32, 32, 33, 35]

c1, c2 = st.columns([3, 2])

with c1:
    fig, ax = plt.subplots()
    ax.bar(keys, values)
    ax.set_ylim(top=40)
    ax.set_xlabel("아빠-엄마 크기 비율")
    ax.set_ylabel("왜곡 응답 수")
    ax.set_title("아빠-엄마 크기 검증")
    st.pyplot(fig)

with c2:
    picture = st.text_input("원하는 사진을 입력하세요.", key='third')
    dir = "father-mother" + '/' + picture + '.png'
    try:
        st.image(dir)
    except:
        st.image("father-mother/2배.png")

st.caption("")
st.caption("")


# fourth header
st.subheader("엄마-아빠 크기 검증")
st.caption("")
keys = ['2배', '4배', '6배', '8배', '10배', '12배', '14배', '16배', '18배', '20배']
values = [26, 32, 33, 31, 30, 33, 34, 38, 38, 39]

c1, c2 = st.columns([3, 2])

with c1:
    fig, ax = plt.subplots()
    ax.bar(keys, values)
    ax.set_ylim(top=40)
    ax.set_xlabel("엄마-아빠 크기 비율")
    ax.set_ylabel("왜곡 응답 수")
    ax.set_title("엄마-아빠 크기 검증")
    st.pyplot(fig)

with c2:
    picture = st.text_input("원하는 사진을 입력하세요.", key='fourth')
    dir = "mother-father" + '/' + picture + '.png'
    try:
        st.image(dir)
    except:
        st.image("mother-father/2배.png")

st.caption("")
st.caption("")


# fifth header
st.subheader("거리 왜곡 검증")
st.caption("")
keys = ['20%', '30%', '40%', '50%', '60%', '70%', '80%']
values = [7, 1, 10, 24, 27, 38, 38]

c1, c2 = st.columns([3, 2])

with c1:
    fig, ax = plt.subplots()
    ax.bar(keys, values)
    ax.set_ylim(top=40)
    ax.set_xlabel("떨어진 거리(단위: 용지의 비율)")
    ax.set_ylabel("왜곡 응답 수")
    ax.set_title("거리 왜곡 검증")
    st.pyplot(fig)

with c2:
    picture = st.text_input("원하는 사진을 입력하세요.", key='fifth')
    dir = "distance" + '/' + picture + '_' + str(random.randint(0, 2)) + '.png'
    try:
        st.image(dir)
    except:
        st.image("distance/20%_0.png")

st.caption("")
st.caption("")


# sixth header
st.subheader("병렬 여부 검증")
st.caption("")
keys = ['0-20%', '20-40%', '40-60%', '60-80%', '80-100%']
values = [3, 12, 26, 32, 36]

c1, c2 = st.columns([3, 2])

with c1:
    fig, ax = plt.subplots()
    ax.bar(keys, values)
    ax.set_ylim(top=40)
    ax.set_xlabel("서로 겹치지 않는 정도(세로축 기준)")
    ax.set_ylabel("왜곡 응답 수")
    ax.set_title("병렬 여부 검증")
    st.pyplot(fig)

with c2:
    picture = st.text_input("원하는 사진을 입력하세요.", key='sixth')
    dir = "parallel" + '/' + picture + '_' + str(random.randint(0, 2)) + '.png'
    try:
        st.image(dir)
    except:
        st.image("parallel/0-20%_0.png")

st.caption("")
st.caption("")