# -*- coding:utf-8 -*-
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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
    fontNames = list(set(f.name for f in fm.fontManager.ttflist))
    fontname = st.selectbox("폰트 선택", fontNames)

    plt.rc('font', family=fontname)
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots()
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day')
    ax.set_title("한글 테스트")
    st.pyplot(fig)

    st.dataframe(tips)


if __name__ == "__main__":
    main()
