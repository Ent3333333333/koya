import streamlit as st
import pandas as pd


st.title('合成してみよう')

data={
  'material01':["亀", "鰻", "団子"],
  'material02': ["草", "塩", "ヒトデ"],
}
#dataのままだと辞書型であるため、関数として呼び出せない。
df=pd.DataFrame(data)


# ---------- セレクトボックス 合成----------
st.title("素材を選択")
st.markdown('<font color="green">素材を選択</font>', unsafe_allow_html=True)

#小さい文字で緑色
#st.markdown('<font color="green">素材を選択</font>', unsafe_allow_html=True)
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

# ---------- ボタン 合成----------

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



st.title('融合してみよう')

data02={
  'fusion01':["鯵", "ピーナッツ", "団子"],
  'fusion02': ["兎", "吸血鬼", "ヒトデ"],
}
#dataのままだと辞書型であるため、関数として呼び出せない。
df02=pd.DataFrame(data02)

# ---------- セレクトボックス 融合----------
st.title("融合物を選択")

selected_fusion1 = st.selectbox(
    "一つ目の融合物を選択してください",
     data02["fusion01"],
     key="fusion1"
)

selected_fusion2 = st.selectbox(
    "二つ目の融合物を選択してください",
     data02["fusion02"],
     key="fusion2"
)

# ---------- ボタン 融合----------

if st.button("融合"):
    if selected_fusion1 == "鯵" and selected_fusion2 == "兎":
        st.write("つぶらな瞳♡　「あじまる」が誕生した！")
        image_url = "https://drive.google.com/uc?id=1DdB1mDMM0r38UyovO3MWfYq9d6v4MlaD"
        st.image(image_url, caption="あじまるの画像")
        
        #通常、Googleドライブ上の画像ファイルを直接的なURLで参照するには、共有可能なリンクのURLを少し変更する必要がある。
        #通常、Googleドライブ上の画像ファイルを直接的なURLで参照するには、共有可能なリンクのURLを少し変更する必要があります。
        #上記の例では、drive.google.com/uc?id=の後にGoogleドライブ上の画像ファイルの固有のIDを指定しています。
        #image_url="https://drive.google.com/file/d/1DdB1mDMM0r38UyovO3MWfYq9d6v4MlaD/view?usp=sharing"
        #st.image(image_url,caption="あじまるの画像")
        
        #image_url="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUpvsZRGnbb8IrNUIRE3NpwCTEcc2n0-SRa9Fi3XzAFT-sSIbQLPzxaFlSAjnm5Vh2pP1QRZCb5dEB091RfcUXvj4BQahbdUc9OmptB-1PD_h1qPs086ra1GhZFV9mSu3OodDNZtAoct_j/s729/bird_gachou.png"
        #st.image(image_url)

#st.image　で直接URLを指定しても、渡せない
       # st.image("https://drive.google.com/file/d/1t2YUyZM_xwTpMaNW49-iMgAAtivuqbn2/view?usp=drive_link")



    elif selected_fusion1 == "鯵" and selected_fusion2 == "ピーナッツ":
        st.write("亀の塩漬け！　甲羅が更に硬くなった！")
    elif selected_fusion1 == "鯵" and selected_fusion2 == "ヒトデ":
        st.write("星付きの亀!　レア度が高くなった！")
    elif selected_fusion1 == "吸血鬼" and selected_fusion2 == "草":
        st.write("鰻のちまき")
    elif selected_fusion1 == "吸血鬼" and selected_fusion2 == "塩":
        st.write("ぬめりの取れた鰻")
    elif selected_fusion1 == "吸血鬼" and selected_fusion2 == "ヒトデ":
        st.write("黒こげのやま　唯一の失敗作が完成した")
    elif selected_fusion1 == "団子" and selected_fusion2 == "草":
        st.write("草団子")
    elif selected_fusion1 == "団子" and selected_fusion2 == "塩":
        st.write("白い塊ができた。　カピカピのなにか")
    elif selected_fusion1 == "団子" and selected_fusion2 == "ヒトデ":
        st.write("キラキラな三食団子！　金粉がまぶされている")
