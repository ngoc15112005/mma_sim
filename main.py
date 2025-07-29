import random
from finish_method import random_finish_method, FIGHTER_ARCHETYPES
from battle_result import analyze_battle_result_expanded
from fight_time import generate_fight_time
from fighter_class import FIGHTER_CLASSES, generate_skill_point
from fight_logic import simulate_fight_scores

def simulate_fight(num_rounds):
    # Tự động chọn ngẫu nhiên đẳng cấp cho hai võ sĩ
    class_a_name = random.choice(list(FIGHTER_CLASSES.keys()))
    class_b_name = random.choice(list(FIGHTER_CLASSES.keys()))

    # Sử dụng logic mô phỏng mới để tạo ra điểm số
    a, b = simulate_fight_scores(class_a_name, class_b_name)

    result_description = analyze_battle_result_expanded(a, b)
    finish = random_finish_method()
    time_info = generate_fight_time(finish["method_type"], num_rounds)

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