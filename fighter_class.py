import random

FIGHTER_CLASSES = {
    "Tân binh (Rookie)": {
        "skill_range": (0, 2),
        "description": "Võ sĩ mới vào nghề, còn non kinh nghiệm nhưng đầy tiềm năng."
    },
    "Kỳ cựu (Veteran)": {
        "skill_range": (2, 4),
        "description": "Võ sĩ dày dạn kinh nghiệm, thi đấu ổn định và khó bị bắt bài."
    },
    "Ngôi sao (Contender)": {
        "skill_range": (4, 6),
        "description": "Võ sĩ thuộc top đầu, có khả năng tranh đai vô địch."
    },
    "Nhà vô địch (Champion)": {
        "skill_range": (5, 7),
        "description": "Đỉnh cao của giải đấu, sở hữu kỹ năng và bản lĩnh vượt trội."
    },
    "Huyền thoại (Legend)": {
        "skill_range": (6, 7),
        "description": "Một biểu tượng của môn thể thao, đã chứng tỏ đẳng cấp qua nhiều thế hệ."
    }
}

def generate_skill_point(class_name):
    """
    Tạo ra một điểm kỹ năng ngẫu nhiên dựa trên đẳng cấp của võ sĩ.
    Nếu class_name không hợp lệ, sẽ trả về một điểm ngẫu nhiên trong toàn bộ thang điểm.
    """
    if class_name not in FIGHTER_CLASSES:
        return random.randint(0, 7) # Trả về ngẫu nhiên nếu đẳng cấp không hợp lệ

    min_skill, max_skill = FIGHTER_CLASSES[class_name]["skill_range"]
    return random.randint(min_skill, max_skill)