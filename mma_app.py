import streamlit as st
import random
from finish_method import random_finish_method
from battle_result import analyze_battle_result
from fight_time import generate_fight_time

def simulate_fight_ui(num_rounds):
    a = random.randint(0, 4)
    b = random.randint(0, 4)

    result_description = analyze_battle_result(a, b)
    finish = random_finish_method()
    time_info = generate_fight_time(finish["method_type"], num_rounds)

    st.markdown("## Kết quả mô phỏng")
    st.write(f"Trình độ random: {a} vs {b}")
    st.write(f"{result_description}")
    st.write(f"Kiểu kết liễu: {finish['description']}")
    st.write(f"Thời điểm: Hiệp {time_info['round']}/{time_info['num_rounds']} – {time_info['minute']}:{str(time_info['second']).zfill(2)}")
    st.write(f"Ghi chú: {time_info['note']}")

# --- Giao diện ---
st.title("🔥 Mô Phỏng MMA Vĩ Đại 🔥")

rounds = st.radio("Chọn số hiệp:", [3, 5], index=0)

if st.button("🎮 Mô phỏng trận đấu"):
    simulate_fight_ui(rounds)