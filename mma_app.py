import streamlit as st
import random
from finish_method import random_finish_method, FIGHTER_ARCHETYPES
from battle_result import analyze_battle_result_expanded
from fight_time import generate_fight_time
from fighter_class import FIGHTER_CLASSES
from fight_logic import simulate_fight_scores

def simulate_fight_ui(num_rounds, class_a, class_b, selected_archetype):
    # Sử dụng logic mô phỏng mới để tạo ra điểm số, cho phép các kết quả bất ngờ
    a, b = simulate_fight_scores(
        class_a if class_a != "Ngẫu nhiên" else None,
        class_b if class_b != "Ngẫu nhiên" else None
    )

    result_description = analyze_battle_result_expanded(a, b)
    finish = random_finish_method(selected_archetype if selected_archetype != "Ngẫu nhiên" else None) # Phong cách của người thắng
    time_info = generate_fight_time(finish["method_type"], num_rounds)

    st.markdown("## Kết quả mô phỏng")
    st.write(f"**Trận đấu:** `{class_a}` (A) vs `{class_b}` (B)")
    st.write(f"**Điểm kỹ năng:** `{a}` vs `{b}`")
    st.success(f"**Kết quả:** {result_description}")

    # Chỉ hiển thị phong cách nếu có người thắng cuộc rõ ràng
    if not result_description.startswith("🤝"):
        st.info(f"**Phong cách của người thắng:** {finish['archetype_name']} – *{finish['archetype_description']}*")

    st.error(f"**Kiểu kết liễu:** {finish['description']}")
    st.write(f"Thời điểm: Hiệp {time_info['round']}/{time_info['num_rounds']} – {time_info['minute']}:{str(time_info['second']).zfill(2)}")
    st.write(f"Ghi chú: {time_info['note']}")

# --- Giao diện ---
st.title("🔥 Mô Phỏng MMA Vĩ Đại 🔥")
rounds = st.radio("Chọn số hiệp:", [3, 5], index=0)

st.markdown("---")

# --- Lựa chọn Võ sĩ ---
st.markdown("### 1. Chọn Đẳng Cấp Võ Sĩ")
class_options = ["Ngẫu nhiên"] + list(FIGHTER_CLASSES.keys())
col1, col2 = st.columns(2)
with col1:
    selected_class_a = st.selectbox("Võ sĩ A:", class_options, key="class_a")
with col2:
    selected_class_b = st.selectbox("Võ sĩ B:", class_options, key="class_b")

# --- Lựa chọn Phong cách ---
st.markdown("### 2. Chọn Phong Cách Thi Đấu (của người thắng)")
archetype_options = ["Ngẫu nhiên"] + list(FIGHTER_ARCHETYPES.keys())
selected_archetype = st.selectbox("Phong cách:", archetype_options)

if st.button("🎮 Mô phỏng trận đấu"):
    simulate_fight_ui(rounds, selected_class_a, selected_class_b, selected_archetype)