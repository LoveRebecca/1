# 导入Streamlit库和其他必要的库
import streamlit as st
import requests

# Streamlit应用程序的标题
st.title("城市天气查询")

# 创建一个下拉菜单，用户可以选择城市
selected_city = st.selectbox("请选择城市", ["北京", "上海", "广州", "深圳"])

# 根据用户选择的城市获取气温信息的URL
weather_api_url = f"https://wttr.in/{selected_city}?format=3"
# 发送HTTP请求获取气温信息
response = requests.get(weather_api_url)

# 检查请求是否成功
if response.status_code == 200:
    # 显示气温信息
    st.write(f"{response.text}")
else:
    # 如果请求失败，显示错误消息
    st.error("获取气温信息时出现错误，请重试。")

# 提示用户可以在下方留下评论
st.text("在下方留下评论:")
user_comment = st.text_area("您的评论", "")

# 显示提交按钮
if st.button("提交评论"):
    # 处理用户的评论，这里可以添加保存评论的逻辑
    st.success("评论提交成功！感谢您的反馈。")
