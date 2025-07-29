import random

def generate_dynamic_fight_time(method_type, num_rounds, archetype_name=None, score_diff=None):
    """
    Tạo ra thời điểm kết thúc trận đấu một cách "động",
    dựa trên kiểu kết liễu, phong cách và mức độ chênh lệch.
    """
    # Các trận đấu hết giờ sẽ luôn kết thúc ở 5:00 của hiệp cuối.
    if method_type in ["DEC", "DRAW"]:
        return {
            "num_rounds": num_rounds,
            "round": num_rounds,
            "minute": 5,
            "second": 0,
            "note": "Kết thúc bằng điểm số sau hiệp cuối cùng"
        }

    # --- Logic xác định hiệp kết thúc ---
    # Bắt đầu với trọng số cơ bản cho mỗi hiệp
    round_weights = [10.0] * num_rounds

    # 1. Điều chỉnh trọng số dựa trên Phong cách (Archetype)
    if archetype_name:
        if archetype_name == "One-Round Monster":
            round_weights[0] *= 5  # Tăng mạnh khả năng kết thúc ở hiệp 1
            for i in range(1, num_rounds):
                round_weights[i] *= 0.2 # Giảm mạnh ở các hiệp sau
        elif archetype_name == "Durable Grinder":
            round_weights[0] *= 0.5 # Ít có khả năng kết thúc sớm
            if num_rounds > 1:
                round_weights[-1] *= 2 # Khả năng kết thúc ở hiệp cuối cao hơn
        elif archetype_name == "Glass Cannon":
            round_weights[0] *= 3 # Khả năng cao kết thúc sớm

    # 2. Điều chỉnh trọng số dựa trên Mức độ chênh lệch (Score Diff)
    if score_diff is not None:
        if score_diff >= 6: # Out trình
            round_weights[0] *= 2 # Tăng khả năng kết thúc ở hiệp 1
            if num_rounds > 1:
                round_weights[1] *= 1.5
        elif score_diff <= 2: # Cân bằng hoặc nghẹt thở
            if num_rounds > 1:
                # Tăng nhẹ khả năng kéo dài đến hiệp cuối
                round_weights[-1] *= 1.2

    # Chọn hiệp kết thúc dựa trên trọng số đã điều chỉnh
    possible_rounds = list(range(1, num_rounds + 1))
    round_end = random.choices(possible_rounds, weights=round_weights, k=1)[0]

    minute = random.randint(0, 4)
    second = random.randint(0, 59)

    # Nếu kết thúc ở hiệp cuối, đảm bảo không vượt quá 5:00
    if round_end == num_rounds and minute == 5:
        second = 0

    return {
        "num_rounds": num_rounds,
        "round": round_end,
        "minute": minute,
        "second": second,
        "note": f"Kết thúc bằng {method_type} tại hiệp {round_end}, phút {minute}:{str(second).zfill(2)}"
    }