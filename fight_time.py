import random

def generate_fight_time(method_type, num_rounds):
    if method_type == "DEC":
        return {
            "num_rounds": num_rounds,
            "round": num_rounds,
            "minute": 5,
            "second": 0,
            "note": "Kết thúc bằng điểm số sau hiệp cuối cùng"
        }

    if method_type in ["DQ", "NC"]:
        round_end = random.choices([1, 2, 3], weights=[60, 30, 10])[0]
    else:
        round_end = random.randint(1, num_rounds)

    minute = random.randint(0, 4)
    second = random.randint(0, 59)

    return {
        "num_rounds": num_rounds,
        "round": round_end,
        "minute": minute,
        "second": second,
        "note": f"Kết thúc bằng {method_type} tại hiệp {round_end}, phút {minute}:{str(second).zfill(2)}"
    }