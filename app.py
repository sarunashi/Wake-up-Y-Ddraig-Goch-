import streamlit as st
import serial
import time
import base64


# ==========================================
# Arduino設定
# ==========================================
SERIAL_PORT = "COM3"
BAUD_RATE = 9600


# ==========================================
# ページ設定
# ==========================================
st.set_page_config(
    page_title="目覚めよ、ファイヤードレイク！",
    page_icon="🐉",
    layout="centered"
)


# ==========================================
# Session State
# ==========================================
if "spell_started" not in st.session_state:
    st.session_state.spell_started = False

if "arduino_sent" not in st.session_state:
    st.session_state.arduino_sent = False


# ==========================================
# タイトル
# ==========================================
st.title("🧙‍♂️ 目覚めよ、ファイヤードレイク！")


# ==========================================
# 魔法を唱える前
# ==========================================
if not st.session_state.spell_started:

    st.image("merlin.png", width=400)

    if st.button(
        "⚡ 目覚めよ！",
        use_container_width=True
    ):

        st.session_state.spell_started = True
        st.session_state.arduino_sent = False

        st.rerun()


# ==========================================
# 魔法発動中
# ==========================================
else:

    # ======================================
    # マーリンのGIF
    # ======================================

    with open("merlin_spell.gif", "rb") as f:
        gif_data = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="data:image/gif;base64,{gif_data}"
                 width="400">
        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")

    # ======================================
    # 呪文
    # ======================================

    st.markdown(
        """
        ## 🪄 呪文

        **「ケルトの神々の名において命じる。  
        目覚めよ、ファイヤードレイク！」**
        """
    )

    st.write("")


    # ======================================
    # ArduinoへGOを一度だけ送信
    # ======================================

    if not st.session_state.arduino_sent:

        try:

            arduino = serial.Serial(
                SERIAL_PORT,
                BAUD_RATE,
                timeout=1
            )

            time.sleep(2)

            arduino.write(b"GO\n")

            st.session_state.arduino_sent = True

            arduino.close()

            st.success("🔥 魔法を送りました！")

        except Exception as e:

            st.error(
                f"Arduinoに接続できませんでした。\n\n{e}"
            )

    else:

        st.success(
            "🔥 魔法はファイヤードレイクに届いています！"
        )


    st.write("")

    # ======================================
    # もう一度
    # ======================================

    if st.button(
        "🔄 もう一度魔法を唱える",
        use_container_width=True
    ):

        st.session_state.spell_started = False
        st.session_state.arduino_sent = False

        st.rerun()