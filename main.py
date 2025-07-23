import random
from finish_method import random_finish_method
from battle_result import analyze_battle_result
from fight_time import generate_fight_time

def simulate_fight(num_rounds):
    a = random.randint(0, 4)
    b = random.randint(0, 4)

    result_description = analyze_battle_result(a, b)
    finish = random_finish_method()
    time_info = generate_fight_time(finish["method_type"], num_rounds)

    print("\n🎮 MÔ PHỎNG TRẬN ĐẤU MMA")
    print("═══════════════════════════")
    print(f"🕒 Số hiệp: {num_rounds}")
    print(f"🎲 Trình độ random: {a} vs {b}")
    print(f"📊 {result_description}")
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