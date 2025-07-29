import streamlit as st
import random
from finish_method import get_dynamic_finish_method, FIGHTER_ARCHETYPES, FINISH_METHODS
from battle_result import analyze_battle_result_expanded
from fight_time import generate_dynamic_fight_time
from fighter_class import FIGHTER_CLASSES
from fight_logic import simulate_fight_scores

def simulate_fight_ui(num_rounds, class_a, class_b, selected_archetype):
    # Sử dụng logic mô phỏng mới để tạo ra điểm số, cho phép các kết quả bất ngờ
    a, b = simulate_fight_scores(
        class_a if class_a != "Ngẫu nhiên" else None,
        class_b if class_b != "Ngẫu nhiên" else None
    )

    result_description = analyze_battle_result_expanded(a, b)
    score_diff = abs(a - b)

    # Xử lý logic kết liễu dựa trên kết quả
    if a == b: # Trường hợp Hòa
        finish = {
            "archetype_name": "Không có",
            "archetype_description": "Trận đấu kết thúc với tỷ số hòa.",
            "description": random.choice(FINISH_METHODS["DRAW"]),
            "method_type": "DRAW"
        }
        time_info = generate_dynamic_fight_time("DRAW", num_rounds) # Hòa luôn hết giờ
    else: # Trường hợp có người thắng
        # Xác định phong cách của người thắng
        winner_archetype = None
        if selected_archetype != "Ngẫu nhiên":
            winner_archetype = selected_archetype
        else:
            # Nếu không chọn, lấy ngẫu nhiên một phong cách
            winner_archetype = random.choice(list(FIGHTER_ARCHETYPES.keys()))

        # Gọi hàm logic động mới
        finish = get_dynamic_finish_method(winner_archetype, score_diff)
        time_info = generate_dynamic_fight_time(finish["method_type"], num_rounds, winner_archetype, score_diff)

    st.markdown("## Kết quả mô phỏng")
    st.write(f"**Trận đấu:** `{class_a}` (A) vs `{class_b}` (B)")
    st.write(f"**Điểm kỹ năng:** `{a}` vs `{b}`")
    st.success(f"**Kết quả:** {result_description}")

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
 
# Lấy mô tả và index dựa trên giá trị hiện tại của widget để duy trì trạng thái UI
description_for_help = "Di chuột vào đây sau khi chọn một phong cách để xem mô tả chi tiết."
default_index = 0
if 'archetype_selector' in st.session_state and st.session_state.archetype_selector != "Ngẫu nhiên":
    selected_value = st.session_state.archetype_selector
    description_for_help = FIGHTER_ARCHETYPES[selected_value]["description"]
    # Tìm index của lựa chọn trước đó để đặt làm giá trị mặc định cho lần chạy này
    if selected_value in archetype_options:
        default_index = archetype_options.index(selected_value)
 
selected_archetype = st.selectbox(
    "Phong cách:",
    archetype_options,
    index=default_index, # Đặt giá trị mặc định để duy trì lựa chọn trên UI
    key="archetype_selector", # Key để truy cập giá trị trong session_state
    help=description_for_help
)

if st.button("🎮 Mô phỏng trận đấu"):
    simulate_fight_ui(rounds, selected_class_a, selected_class_b, selected_archetype)