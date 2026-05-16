class AnimalExpertSystem:
    def __init__(self):
        # 1. Mã hóa các quy tắc FOL (First-Order Logic)
        # Cách đọc: Nếu thỏa mãn tất cả 'if', thì kết luận là 'then'
        self.kb_rules = [
    # --- PHÂN LOẠI LỚP (LEVEL 1) ---
    {"if": ["co_vu"], "then": "Lớp Thú"},
    {"if": ["co_long_vu"], "then": "Lớp Chim"},
    {"if": ["co_vay", "de_trung"], "then": "Lớp Bò Sát"},
    {"if": ["biet_boi", "co_mang"], "then": "Lớp Cá"},

    # --- PHÂN LOẠI LỚP THÚ (LEVEL 2) ---
    {"if": ["Lớp Thú", "biet_bay"], "then": "Con Dơi"},
    {"if": ["Lớp Thú", "song_duoi_nuoc"], "then": "Cá Voi"},
    {"if": ["Lớp Thú", "an_thit", "co_long_van"], "then": "Con Hổ"},
    {"if": ["Lớp Thú", "an_thit", "bo_bom"], "then": "Sư Tử"},
    {"if": ["Lớp Thú", "co_tui"], "then": "Kangaroo"},
    {"if": ["Lớp Thú", "co_voi dài"], "then": "Con Voi"},

    # --- PHÂN LOẠI LỚP CHIM (LEVEL 2) ---
    {"if": ["Lớp Chim", "biet_bay", "san_moi"], "then": "Đại Bàng"},
    {"if": ["Lớp Chim", "khong_biet_bay", "song_o_bang_gia"], "then": "Chim Cánh Cụt"},
    {"if": ["Lớp Chim", "khong_biet_bay", "chay_nhanh"], "then": "Đà Điểu"},
    {"if": ["Lớp Chim", "biet_boi", "mo_det"], "then": "Con Vịt"},

    # --- PHÂN LOẠI BÒ SÁT & CÁ (LEVEL 2) ---
    {"if": ["Lớp Bò Sát", "khong_chan"], "then": "Con Rắn"},
    {"if": ["Lớp Bò Sát", "co_mai_cung"], "then": "Con Rùa"},
    {"if": ["Lớp Cá", "hung_du", "kich_thuoc_lon"], "then": "Cá Mập"},
    {"if": ["Lớp Cá", "co_nhieu_mau_sac"], "then": "Cá Vàng"}
]
        self.known_facts = set()

    def run_inference(self, input_facts):
        self.known_facts = set(input_facts)
        new_info = True
        
        print(f"\n[Bắt đầu suy luận từ các sự kiện: {', '.join(input_facts)}]")
        
        while new_info:
            new_info = False
            for rule in self.kb_rules:
                # Kiểm tra xem tất cả điều kiện của quy tắc có nằm trong sự kiện đã biết không
                if all(cond in self.known_facts for cond in rule["if"]):
                    if rule["then"] not in self.known_facts:
                        print(f" => Phát hiện mới: Vì {rule['if']} đúng nên đây là {rule['then']}")
                        self.known_facts.add(rule["then"])
                        new_info = True
        
        return self.known_facts

# 2. Chương trình chính để Demo
if __name__ == "__main__":
    expert = AnimalExpertSystem()
    
    print("--- HỆ THỐNG PHÂN LOẠI ĐỘNG VẬT (FOL) ---")
    print("Nhập các đặc điểm của con vật (cách nhau bằng dấu phẩy).")
    print("Ví dụ: co_vu, de_con, biet_bay")
    
    user_input = input("Đặc điểm: ").strip().lower().split(",")
    facts = [f.strip() for f in user_input]
    
    final_results = expert.run_inference(facts)
    
    # Lọc ra kết quả cuối cùng (thường là cái tên cụ thể nhất)
    final_animal = [item for item in final_results if "Con" in item or "Cá" in item]
    
    print("\n" + "="*30)
    if final_animal:
        print(f"KẾT LUẬN: Đây là {final_animal[-1]}")
    else:
        print("KẾT LUẬN: Chưa đủ dữ liệu để phân loại cụ thể.")
    print("="*30)