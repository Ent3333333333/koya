
import streamlit as st
import pandas as pd

st.title('合成してみよう')

data={
  'material01':["亀", "鰻", "団子"],
  'material02': ["草", "塩", "ヒトデ"],
}
#dataのままだと辞書型であるため、関数として呼び出せない。
df=pd.DataFrame(data)

# ---------- セレクトボックス ----------
#st.title("素材を選択")
#
#df_select = pd.DataFrame({
#    "material01": ['亀', '鰻', '団子'],
#    })
#selected = st.selectbox(
#    "一つ目の素材を選択してください",
#     df_select["material01"])
#
#df_select = pd.DataFrame({
#    "material02": ['草', '塩', 'ヒトデ'],
#    })
#selected = st.selectbox(
#    "二つ目の素材を選択してください",
#     df_select["material02"])

# ---------- セレクトボックス ----------
st.title("素材を選択")

selected_material1 = st.selectbox(
    "一つ目の素材を選択してください",
     data["material01"],
     key="materaial1"
)

selected_material2 = st.selectbox(
    "二つ目の素材を選択してください",
     data["material02"],
     key="material2"
)

# ---------- ボタン ----------

if st.button("合成"):
    if selected_material1 == "亀" and selected_material2 == "草":
        st.write("牛の餌")
    elif selected_material1 == "亀" and selected_material2 == "塩":
        st.write("亀の塩漬け！　甲羅が更に硬くなった！")
    elif selected_material1 == "亀" and selected_material2 == "ヒトデ":
        st.write("星付きの亀!　レア度が高くなった！")
    elif selected_material1 == "鰻" and selected_material2 == "草":
        st.write("鰻のちまき")
    elif selected_material1 == "鰻" and selected_material2 == "塩":
        st.write("ぬめりの取れた鰻")
    elif selected_material1 == "鰻" and selected_material2 == "ヒトデ":
        st.write("黒こげのやま　唯一の失敗作が完成した")
    elif selected_material1 == "団子" and selected_material2 == "草":
        st.write("草団子")
    elif selected_material1 == "団子" and selected_material2 == "塩":
        st.write("白い塊ができた。　カピカピのなにか")
    elif selected_material1 == "団子" and selected_material2 == "ヒトデ":
        st.write("キラキラな三食団子！　金粉がまぶされている")
