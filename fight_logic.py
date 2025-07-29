import random
from fighter_class import generate_skill_point

def simulate_fight_scores(class_a, class_b):
    """
    Mô phỏng điểm số trận đấu bằng cách kết hợp kỹ năng cơ bản với "Yếu tố Phong độ".
    Điều này cho phép các kết quả bất ngờ (upset) và làm cho mô phỏng trở nên năng động hơn.
    """
    # 1. Lấy điểm kỹ năng cơ bản từ Đẳng cấp của võ sĩ
    skill_a = generate_skill_point(class_a)
    skill_b = generate_skill_point(class_b)

    # 2. Tạo ra một "Yếu tố Phong độ" ngẫu nhiên cho mỗi võ sĩ trong trận đấu này
    # Tượng trưng cho việc họ có một ngày thi đấu tốt hay tệ.
    # Phạm vi rộng hơn cho phép các cuộc lật đổ kịch tính hơn.
    performance_a = random.randint(-2, 4)
    performance_b = random.randint(-2, 4)

    # 3. Tính điểm số cuối cùng
    final_score_a = skill_a + performance_a
    final_score_b = skill_b + performance_b

    # Đảm bảo điểm số không xuống dưới 0 để logic mô tả kết quả được đơn giản
    final_score_a = max(0, final_score_a)
    final_score_b = max(0, final_score_b)

    return final_score_a, final_score_b