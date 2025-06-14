import random

def tung_xuc_xac():
    return random.randint(1, 6)

def choi_nui_khi():
    print("Chào mừng đến với trò chơi: Núi Khỉ Đó - Núi Khỉ Đen!")
    lua_chon = input("Bạn chọn 'núi khỉ đó' hay 'núi khỉ đen'? ").strip().lower()

    if lua_chon not in ['núi khỉ đó', 'núi khỉ đen']:
        print("Lựa chọn không hợp lệ.")
        return

    # Tung 3 viên xúc xắc
    xuc_xac = [tung_xuc_xac() for _ in range(3)]
    tong = sum(xuc_xac)
    print(f"Xúc xắc ra: {xuc_xac} => Tổng: {tong}")

    ket_qua = "núi khỉ đó" if tong >= 11 else "núi khỉ đen"

    if lua_chon == ket_qua:
        print("Bạn đã thắng!")
    else:
        print("Bạn đã thua!")
    print(f"Kết quả: {ket_qua.upper()}")

choi_nui_khi()

