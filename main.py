while True:
    choi_nui_khi()
    choi_tiep = input("Chơi tiếp? (y/n): ").strip().lower()
    if choi_tiep != 'y':
        break
print("="*40)
print("🎲 CHÀO MỪNG ĐẾN NÚI KHỈ ĐÓ - NÚI KHỈ ĐEN 🎲")
print("="*40)
if ket_qua == "núi khỉ đó":
    print("🔥 Khỉ đỏ chiến thắng!")
else:
    print("🖤 Khỉ đen lật kèo!")


