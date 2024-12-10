import streamlit as st
import requests
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
from matplotlib import font_manager
import tempfile

# GitHub에서 TTF 파일 다운로드 (raw URL 사용)
url = 'https://raw.githubusercontent.com/dew02/font-test/main/NoonnuBasicGothicRegular.ttf'
response = requests.get(url)

# TTF 파일을 임시 파일로 저장
with tempfile.NamedTemporaryFile(delete=False, suffix='.ttf') as temp_font_file:
    temp_font_file.write(response.content)
    temp_font_path = temp_font_file.name

# 폰트 등록 (명시적으로 경로 지정)
font_prop = font_manager.FontProperties(fname=temp_font_path)

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
ax.set_title("한글 테스트", fontproperties=font_prop)  # 폰트 속성 추가
ax.set_xlabel("Total Bill", fontproperties=font_prop)
ax.set_ylabel("Tip", fontproperties=font_prop)
ax.legend(prop=font_prop)  # 범례에도 폰트 적용

# 그래프 표시
st.pyplot(fig)
