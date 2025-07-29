import random

# Grouping finish methods by type for easier management
FINISH_METHODS = {
    "KO": [
        "Đấm thẳng mặt", "Móc ngang", "Uppercut", "Counterpunch",
        "Gối bay", "Đá đầu", "Đá xoay", "Elbow", "Body Shot",
        "KO (Đòn Slam)", "KO (Đòn xoay/Spinning Attack)"
    ],
    "TKO": [
        "Ground and Pound", "Standing no defense", "Combo đấm áp đảo",
        "TKO (Bác sĩ dừng trận - Vết rách)", "TKO (Góc ném khăn/Corner Stoppage)",
        "TKO (Chấn thương/Injury)", "TKO (Bỏ cuộc giữa hiệp/Retirement)",
        "TKO (Đầu hàng vì dính đòn/Submission to Strikes)"
    ],
    "SUB": [
        "Rear Naked Choke", "Armbar", "Triangle Choke", "Guillotine Choke",
        "Kimura", "Americana", "Twister", "Von Flue Choke", "Suloev Stretch",
        "Ezekiel Choke", "Peruvian Necktie", "Banana Split",
        "Heel Hook", "Kneebar", "Anaconda Choke", "D'Arce Choke"
    ],
    "DEC": [
        # Chỉ định loại quyết định, thắng/thua sẽ do logic bên ngoài gán
        "Thắng điểm đồng thuận (Unanimous Decision)",
        "Thắng điểm chia (Split Decision)",
        "Thắng điểm đa số (Majority Decision)"
    ],
    "DQ": [
        "Thắng do đối thủ phạm luật (Đòn chỏ 12-6)",
        "Thắng do đối thủ phạm luật (Lên gối vào đầu đối thủ đang nằm)",
        "Thắng do đối thủ phạm luật (Giữ lồng/quần liên tục)",
        "Bị loại vì phạm luật (Ra đòn sau tiếng chuông)"
    ],
    "NC": ["No Contest (Vô hiệu)"],
    "DRAW": ["Hòa điểm đồng thuận (Draw)", "Hòa điểm đa số (Majority Draw)"]
}

# Defining fighter archetypes with their respective finish probabilities
FIGHTER_ARCHETYPES = {
    # Striking-focused
    "Power Puncher / Brawler": {
        "weights": {"KO": 60, "TKO": 25, "SUB": 1, "DEC": 9},
        "description": "Dựa vào sức mạnh, luôn tìm kiếm một cú đấm 'trời giáng' để kết thúc trận đấu."
    },
    "Technical Boxer": {
        "weights": {"KO": 20, "TKO": 40, "SUB": 1, "DEC": 34},
        "description": "Bậc thầy về footwork và combo chính xác, thường thắng bằng TKO hoặc điểm số áp đảo."
    },
    "Kickboxer / Muay Thai Specialist": {
        "weights": {"KO": 45, "TKO": 35, "SUB": 2, "DEC": 13},
        "description": "Sử dụng đa dạng các đòn chân, gối, chỏ tàn khốc, đặc biệt nguy hiểm khi áp sát."
    },
    "Counter Striker": {
        "weights": {"KO": 50, "TKO": 20, "SUB": 2, "DEC": 23},
        "description": "Kiên nhẫn, dụ đối thủ tấn công để tung ra những đòn phản công chớp nhoáng và chính xác."
    },
    "Volume Striker": {
        "weights": {"KO": 10, "TKO": 45, "SUB": 2, "DEC": 38},
        "description": "Tấn công liên tục với số lượng lớn để áp đảo đối thủ, yêu cầu thể lực phi thường."
    },
     "Movement-Based Striker / Point Fighter": { # MỚI
        "weights": {"KO": 5, "TKO": 10, "SUB": 1, "DEC": 79},
        "description": "Sử dụng footwork linh hoạt và tốc độ để ra đòn từ bên ngoài, tích lũy điểm số và tránh giao tranh."
    },
    "Unorthodox Striker": {
        "weights": {"KO": 45, "TKO": 20, "SUB": 5, "DEC": 25},
        "description": "Sử dụng các kỹ thuật khó đoán (Karate, Capoeira), tạo ra những cú KO bất ngờ."
    },
    # Grappling-focused
    "BJJ Specialist": {
        "weights": {"KO": 2, "TKO": 8, "SUB": 70, "DEC": 15},
        "description": "Bậc thầy địa chiến, mục tiêu chính là đưa trận đấu xuống sàn và tìm kiếm đòn khóa siết."
    },
    "Wrestler": {
        "weights": {"KO": 5, "TKO": 45, "SUB": 10, "DEC": 35},
        "description": "Kỹ năng vật và quật ngã thượng thừa, bào mòn thể lực đối thủ bằng Ground and Pound."
    },
    "Sambo Specialist": {
        "weights": {"KO": 5, "TKO": 20, "SUB": 55, "DEC": 15},
        "description": "Kết hợp các đòn quật ngã mạnh mẽ và các đòn khóa chân (leg locks) cực kỳ nguy hiểm."
    },
    "Submission Wrestler (Catch Wrestler)": { # MỚI
        "weights": {"KO": 5, "TKO": 30, "SUB": 50, "DEC": 10},
        "description": "Tập trung vào kiểm soát từ vị trí trên, dùng các kỹ thuật khóa siết gây đau đớn để buộc đối thủ đầu hàng."
    },
    # Hybrid/All-rounders
    "Wrestle-Boxer": {
        "weights": {"KO": 25, "TKO": 30, "SUB": 15, "DEC": 25},
        "description": "Lối đánh toàn diện, dùng boxing để thiết lập vật hoặc dùng vật để tạo cơ hội cho striking."
    },
    "Pressure Fighter": {
        "weights": {"KO": 15, "TKO": 40, "SUB": 10, "DEC": 30},
        "description": "Luôn tiến về phía trước, dồn ép đối thủ vào lưới và bào mòn họ bằng cả striking và grappling."
    },
    "Clinch Fighter / Dirty Boxer": { # MỚI
        "weights": {"KO": 10, "TKO": 45, "SUB": 5, "DEC": 35},
        "description": "Bậc thầy ép lưới, kiểm soát và bào mòn đối thủ bằng các đòn gối, chỏ và đấm tầm gần."
    },
    # Specialists/Unique Styles
    "One-Round Monster": {
        "weights": {"KO": 50, "TKO": 30, "SUB": 15, "DEC": 0},
        "description": "Cực kỳ bùng nổ và nguy hiểm trong hiệp 1, nhưng thể lực giảm sút nhanh chóng."
    },
    "Durable Grinder": {
        "weights": {"KO": 5, "TKO": 10, "SUB": 5, "DEC": 75},
        "description": "Sở hữu 'cằm sắt' và sức bền phi thường, thường kéo đối thủ vào cuộc chiến thể lực."
    },
    "Glass Cannon": {
        "weights": {"KO": 65, "TKO": 25, "SUB": 2, "DEC": 3},
        "description": "Sức tấn công cực kỳ khủng khiếp nhưng khả năng chịu đòn rất kém. 'Được ăn cả, ngã về không'."
    }
}


def get_dynamic_finish_method(archetype_name=None, score_diff=None):
    # Nếu không có phong cách nào được chỉ định hoặc tên không hợp lệ, chọn ngẫu nhiên.
    if archetype_name is None or archetype_name not in FIGHTER_ARCHETYPES:
        archetype_name = random.choice(list(FIGHTER_ARCHETYPES.keys()))

    archetype = FIGHTER_ARCHETYPES[archetype_name]

    # Lấy trọng số cơ bản từ phong cách (đã được dọn dẹp)
    base_weights = archetype["weights"].copy()

    # --- Bước 1.3: Thêm Logic "Động" điều chỉnh trọng số ---
    if score_diff is not None:
        if score_diff >= 6: # Out trình -> Tăng khả năng kết thúc sớm
            base_weights["KO"] = base_weights.get("KO", 0) * 2.0
            base_weights["TKO"] = base_weights.get("TKO", 0) * 1.5
            base_weights["SUB"] = base_weights.get("SUB", 0) * 1.5
            base_weights["DEC"] = base_weights.get("DEC", 0) * 0.1 # Giảm mạnh khả năng thắng điểm
        elif score_diff == 1: # Thắng nghẹt thở -> Tăng khả năng thắng điểm
            base_weights["DEC"] = base_weights.get("DEC", 0) * 2.0

    # --- Bước 1.4: Hoàn thiện và tích hợp lại các kết quả tình huống ---
    # Thêm các loại kết quả cố định không phụ thuộc vào phong cách với trọng số nhỏ
    final_weights = base_weights
    final_weights.update({"DQ": 2, "NC": 1})

    method_types = list(final_weights.keys())
    weights = list(final_weights.values())

    # Đảm bảo không có lỗi nếu tất cả trọng số bằng 0 (ví dụ: One-Round Monster chỉ có DEC=0)
    if not any(w > 0 for w in weights):
        # Fallback: nếu không có trọng số, chọn ngẫu nhiên từ các loại có thể
        chosen_method_type = random.choice(method_types)
    else:
        # Đảm bảo không có trọng số âm hoặc bằng không để tránh lỗi
        positive_weights = [max(0.01, w) for w in weights]
        chosen_method_type = random.choices(method_types, weights=positive_weights, k=1)[0]

    # Chọn một diễn giải chi tiết từ loại kết liễu
    specific_finishes = FINISH_METHODS[chosen_method_type]
    specific_finish = random.choice(specific_finishes)

    # Tạo mô tả đầy đủ
    # Đối với DEC, mô tả đã đủ chi tiết
    full_description = specific_finish if chosen_method_type in ["DEC", "DQ", "NC", "DRAW"] else f"{chosen_method_type} – {specific_finish}"

    return {
        "archetype_name": archetype_name,
        "archetype_description": archetype["description"],
        "description": full_description,
        "method_type": chosen_method_type
    }
