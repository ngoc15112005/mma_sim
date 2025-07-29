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
        "weights": {"KO": 60, "TKO": 25, "SUB": 1, "DEC": 9, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Dựa vào sức mạnh, luôn tìm kiếm một cú đấm 'trời giáng' để kết thúc trận đấu."
    },
    "Technical Boxer": {
        "weights": {"KO": 20, "TKO": 40, "SUB": 1, "DEC": 34, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Bậc thầy về footwork và combo chính xác, thường thắng bằng TKO hoặc điểm số áp đảo."
    },
    "Kickboxer / Muay Thai Specialist": {
        "weights": {"KO": 45, "TKO": 35, "SUB": 2, "DEC": 13, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Sử dụng đa dạng các đòn chân, gối, chỏ tàn khốc, đặc biệt nguy hiểm khi áp sát."
    },
    "Counter Striker": {
        "weights": {"KO": 50, "TKO": 20, "SUB": 2, "DEC": 23, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Kiên nhẫn, dụ đối thủ tấn công để tung ra những đòn phản công chớp nhoáng và chính xác."
    },
    "Volume Striker": {
        "weights": {"KO": 10, "TKO": 45, "SUB": 2, "DEC": 38, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Tấn công liên tục với số lượng lớn để áp đảo đối thủ, yêu cầu thể lực phi thường."
    },
     "Movement-Based Striker / Point Fighter": { # MỚI
        "weights": {"KO": 5, "TKO": 10, "SUB": 1, "DEC": 79, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Sử dụng footwork linh hoạt và tốc độ để ra đòn từ bên ngoài, tích lũy điểm số và tránh giao tranh."
    },
    "Unorthodox Striker": {
        "weights": {"KO": 45, "TKO": 20, "SUB": 5, "DEC": 25, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Sử dụng các kỹ thuật khó đoán (Karate, Capoeira), tạo ra những cú KO bất ngờ."
    },
    # Grappling-focused
    "BJJ Specialist": {
        "weights": {"KO": 2, "TKO": 8, "SUB": 70, "DEC": 15, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Bậc thầy địa chiến, mục tiêu chính là đưa trận đấu xuống sàn và tìm kiếm đòn khóa siết."
    },
    "Wrestler": {
        "weights": {"KO": 5, "TKO": 45, "SUB": 10, "DEC": 35, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Kỹ năng vật và quật ngã thượng thừa, bào mòn thể lực đối thủ bằng Ground and Pound."
    },
    "Sambo Specialist": {
        "weights": {"KO": 5, "TKO": 20, "SUB": 55, "DEC": 15, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Kết hợp các đòn quật ngã mạnh mẽ và các đòn khóa chân (leg locks) cực kỳ nguy hiểm."
    },
    "Submission Wrestler (Catch Wrestler)": { # MỚI
        "weights": {"KO": 5, "TKO": 30, "SUB": 50, "DEC": 10, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Tập trung vào kiểm soát từ vị trí trên, dùng các kỹ thuật khóa siết gây đau đớn để buộc đối thủ đầu hàng."
    },
    # Hybrid/All-rounders
    "Wrestle-Boxer": {
        "weights": {"KO": 25, "TKO": 30, "SUB": 15, "DEC": 25, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Lối đánh toàn diện, dùng boxing để thiết lập vật hoặc dùng vật để tạo cơ hội cho striking."
    },
    "Pressure Fighter": {
        "weights": {"KO": 15, "TKO": 40, "SUB": 10, "DEC": 30, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Luôn tiến về phía trước, dồn ép đối thủ vào lưới và bào mòn họ bằng cả striking và grappling."
    },
    "Clinch Fighter / Dirty Boxer": { # MỚI
        "weights": {"KO": 10, "TKO": 45, "SUB": 5, "DEC": 35, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Bậc thầy ép lưới, kiểm soát và bào mòn đối thủ bằng các đòn gối, chỏ và đấm tầm gần."
    },
    # Specialists/Unique Styles
    "One-Round Monster": {
        "weights": {"KO": 50, "TKO": 30, "SUB": 15, "DEC": 0, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Cực kỳ bùng nổ và nguy hiểm trong hiệp 1, nhưng thể lực giảm sút nhanh chóng."
    },
    "Durable Grinder": {
        "weights": {"KO": 5, "TKO": 10, "SUB": 5, "DEC": 75, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Sở hữu 'cằm sắt' và sức bền phi thường, thường kéo đối thủ vào cuộc chiến thể lực."
    },
    "Glass Cannon": {
        "weights": {"KO": 65, "TKO": 25, "SUB": 2, "DEC": 3, "DQ": 2, "NC": 1, "DRAW": 2},
        "description": "Sức tấn công cực kỳ khủng khiếp nhưng khả năng chịu đòn rất kém. 'Được ăn cả, ngã về không'."
    }
}


def random_finish_method(archetype_name=None):
    # Nếu không có phong cách nào được chỉ định hoặc tên không hợp lệ, chọn ngẫu nhiên.
    if archetype_name is None or archetype_name not in FIGHTER_ARCHETYPES:
        archetype_name = random.choice(list(FIGHTER_ARCHETYPES.keys()))

    archetype = FIGHTER_ARCHETYPES[archetype_name]

    method_types = list(archetype["weights"].keys())
    weights = list(archetype["weights"].values())
    chosen_method_type = random.choices(method_types, weights=weights, k=1)[0]

    specific_finishes = FINISH_METHODS[chosen_method_type]
    specific_finish = random.choice(specific_finishes)

    full_description = specific_finish if chosen_method_type in ["DEC", "DQ", "NC", "DRAW"] else f"{chosen_method_type} – {specific_finish}"

    return {
        "archetype_name": archetype_name,
        "archetype_description": archetype["description"],
        "description": full_description,
        "method_type": chosen_method_type
    }
