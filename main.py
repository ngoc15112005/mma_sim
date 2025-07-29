import random
from finish_method import get_dynamic_finish_method, FIGHTER_ARCHETYPES, FINISH_METHODS
from battle_result import analyze_battle_result_expanded
from fight_time import generate_dynamic_fight_time
from fighter_class import FIGHTER_CLASSES, generate_skill_point
from fight_logic import simulate_fight_scores

def simulate_fight(num_rounds):
    # Tự động chọn ngẫu nhiên đẳng cấp cho hai võ sĩ
    class_a_name = random.choice(list(FIGHTER_CLASSES.keys()))
    class_b_name = random.choice(list(FIGHTER_CLASSES.keys()))

    # Sử dụng logic mô phỏng mới để tạo ra điểm số
    a, b = simulate_fight_scores(class_a_name, class_b_name)

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
        # Trong main.py, chúng ta chọn ngẫu nhiên phong cách cho người thắng
        winner_archetype = random.choice(list(FIGHTER_ARCHETYPES.keys()))

        # Gọi hàm logic động mới
        finish = get_dynamic_finish_method(winner_archetype, score_diff)
        time_info = generate_dynamic_fight_time(finish["method_type"], num_rounds, winner_archetype, score_diff)

    print("\n🎮 MÔ PHỎNG TRẬN ĐẤU MMA")
    print("═══════════════════════════")
    print(f"⚔️  Trận đấu: {class_a_name} (A) vs {class_b_name} (B)")
    print(f"🕒 Số hiệp: {num_rounds}")
    print(f"🎲 Điểm kỹ năng: {a} vs {b}")
    print(f"📊 {result_description}")
    print(f"💪 Phong cách thi đấu: {finish['archetype_name']} ({finish['archetype_description']})")
    print(f"🏁 Kiểu kết liễu: {finish['description']}")
    print(f"⏱️ Thời điểm: Hiệp {time_info['round']}/{time_info['num_rounds']} – {time_info['minute']}:{str(time_info['second']).zfill(2)}")
    print(f"📝 Ghi chú: {time_info['note']}")
    print("═══════════════════════════\n")

if __name__ == "__main__":
    while True:
        rounds = input("🔢 Chọn số hiệp (3 hoặc 5): ")
        if rounds in ['3', '5']:
            simulate_fight(int(rounds))
            break
        else:
            print("⚠️ Vui lòng nhập đúng 3 hoặc 5.")