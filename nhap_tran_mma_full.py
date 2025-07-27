
import json
import os
from datetime import datetime

FILE_PATH = "lich_su_mma.json"

def nhap_tran_mma():
    tran = {}
    tran["trận"] = int(input("Số trận: "))
    tran["ngày"] = datetime.now().strftime("%Y-%m-%d")
    tran["địa điểm"] = input("Địa điểm thi đấu: ")
    tran["giải đấu"] = input("Giải đấu: ")
    tran["hạng_cân"] = input("Hạng cân (VD: Welterweight 77kg): ")

    # Thông tin đối thủ
    doi_thu = {}
    doi_thu["tên"] = input("Tên đối thủ: ")
    doi_thu["chiều_cao"] = input("Chiều cao đối thủ (VD: 1m80): ")
    doi_thu["cân_nặng"] = input("Cân nặng đối thủ (VD: 77kg): ")
    doi_thu["thành_tích"] = input("Thành tích đối thủ (VD: 10-2): ")
    doi_thu["đội"] = input("Đội của đối thủ: ")
    tran["đối_thủ"] = doi_thu

    # Kết quả
    ket_qua = {}
    ket_qua["kết_thúc"] = input("Kết quả (Thắng/Thua): ")
    ket_qua["kiểu_kết_liễu"] = input("Kiểu kết liễu (VD: KO, SUB, DEC): ")
    ket_qua["kỹ_thuật"] = input("Kỹ thuật kết thúc (VD: Uppercut): ")
    ket_qua["thời_điểm"] = {
        "hiệp": int(input("Hiệp mấy: ")),
        "phút": int(input("Phút: ")),
        "giây": int(input("Giây: "))
    }
    ket_qua["số_hiệp"] = int(input("Tổng số hiệp: "))
    ket_qua["hình_thức"] = input("Hình thức (VD: Hiệp chẵn, thắng điểm): ")
    tran["kết_quả"] = ket_qua

    # Phân tích
    tran["phân_tích_trận"] = {
        "phong_độ_trước_trận": input("Phong độ trước trận: "),
        "chiến_thuật": input("Chiến thuật trận đấu: "),
        "điểm_nổi_bật": input("Điểm nổi bật (cách nhau bởi dấu |): ").split("|")
    }

    # Truyền thông
    tran["truyền_thông"] = {
        "tỷ_lệ_cược": {
            "đại_tiêu": float(input("Tỷ lệ cược Đại Tiêu: ")),
            "đối_thủ": float(input("Tỷ lệ cược đối thủ: "))
        },
        "nhận_định": input("Nhận định trước trận (cách nhau bởi dấu |): ").split("|"),
        "đánh_giá_sau_trận": input("Đánh giá sau trận: ")
    }

    # Hậu trận
    tran["hậu_trận"] = {
        "phản_ứng": input("Phản ứng sau trận: "),
        "định_hướng": input("Định hướng tiếp theo: "),
        "call_out": input("Call out ai không? (nếu có): ")
    }

    tran["ghi_chú_khác"] = input("Ghi chú khác (nếu có): ")
    return tran

def luu_tran_vao_file(tran):
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            ds_tran = json.load(f)
    else:
        ds_tran = []

    ds_tran.append(tran)

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(ds_tran, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã lưu trận đấu #{tran['trận']} thành công!")

if __name__ == "__main__":
    tran_moi = nhap_tran_mma()
    luu_tran_vao_file(tran_moi)
