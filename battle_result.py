def analyze_battle_result(a, b):
    total = a + b
    diff = abs(a - b)

    if a == 0 and b == 0:
        return "❌ Thua toàn tập – không có nổi phản kháng"
    elif total == 1:
        return "✅ Thắng cực khó – lật kèo bất ngờ"
    elif total == 2:
        return "✅ Thắng nhọc – trận đấu cân sức"
    elif total == 3:
        return "✅ Thắng khá thuyết phục – có lợi thế rõ"
    elif total == 4 and diff == 0:
        return "✅ Thắng ngang tài – kỹ năng tương đồng"
    elif 4 <= total <= 6 and diff >= 2:
        return "✅ Out trình – điều khiển trận đấu từ đầu đến cuối"
    elif total >= 7:
        return "✅ Làm nhục – highlight trình diễn"
    else:
        return "✅ Thắng – mức độ trung bình"
