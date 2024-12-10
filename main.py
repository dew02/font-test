# -*- coding:utf-8 -*-
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# 한글폰트 적용
# 폰트 적용
import os
import matplotlib.font_manager as fm  # 폰트 관련 용도 as fm


@st.cache_data
def fontRegistered():
    font_dirs = [os.getcwd() + '/customFonts']
    font_files = fm.findSystemFonts(fontpaths=font_dirs)

    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    fm._load_fontmanager(try_read_cache=False)


def main():
    fontRegistered()

    # 시스템에 설치된 폰트 이름 목록 가져오기
    fontNames = list(set(f.name for f in fm.fontManager.ttflist))

    # Streamlit의 selectbox로 폰트 선택
    fontname = st.selectbox("폰트 선택", fontNames)

    # 선택된 폰트로 설정
    plt.rc('font', family=fontname)

    # 간단한 데이터프레임 생성
    data = {
        'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59],
        'tip': [1.01, 1.66, 3.50, 3.31, 3.61],
        'day': ['Sun', 'Sun', 'Sun', 'Sun', 'Sun']
    }
    df = pd.DataFrame(data)

    # 스캐터 플롯 그리기
    fig, ax = plt.subplots()
    ax.scatter(df['total_bill'], df['tip'], c='blue', label='Tips')

    # 제목, 축 레이블 추가
    ax.set_title("한글 테스트")
    ax.set_xlabel("Total Bill")
    ax.set_ylabel("Tip")
    ax.legend()

    # 그래프 표시
    st.pyplot(fig)

    # 데이터프레임 표시
    st.dataframe(df)


if __name__ == "__main__":
    main()
