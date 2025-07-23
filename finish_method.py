import random

FINISH_LIST = [
    "KO – Đấm thẳng mặt",
    "KO – Móc ngang",
    "KO – Uppercut",
    "KO – Jab đơn",
    "KO – Counterpunch",
    "KO – Gối bay",
    "KO – Đá đầu",
    "KO – Đá xoay",
    "KO – Elbow",
    "KO – Body Shot",
    "TKO – Ground and Pound",
    "TKO – Standing no defense",
    "TKO – Combo đấm",
    "TKO – Gãy chân/tay",
    "TKO – Doctor Stoppage",
    "TKO – Góc ném khăn",
    "TKO – Ngã trượt rồi bị kết liễu",
    "SUB – Rear Naked Choke",
    "SUB – Armbar",
    "SUB – Triangle Choke",
    "SUB – Guillotine Choke",
    "SUB – Kimura",
    "SUB – Americana",
    "SUB – Twister",
    "SUB – Von Flue Choke",
    "SUB – Suloev Stretch",
    "SUB – Ezekiel Choke",
    "SUB – Peruvian Necktie",
    "SUB – Banana Split",
    "DEC – Thắng điểm đồng thuận",
    "DEC – Thắng điểm chia",
    "DEC – Thắng điểm đa số",
    "DEC – Thua điểm đồng thuận",
    "DEC – Thua điểm chia",
    "DEC – Thua điểm đa số",
    "DQ – Bị loại vì phạm luật",
    "DQ – Thắng do đối thủ phạm luật",
    "NC – No Contest",
    "DRAW – Hòa",
    "DRAW – Majority Draw"
]

def random_finish_method():
    idx = random.randint(0, len(FINISH_LIST) - 1)
    return {
        "code": idx,
        "description": FINISH_LIST[idx],
        "method_type": FINISH_LIST[idx].split(" – ")[0]
    }
