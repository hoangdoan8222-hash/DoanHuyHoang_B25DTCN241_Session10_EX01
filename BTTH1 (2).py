# 1. PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
# - Input: 
#   + Lựa chọn menu: Chuỗi ký tự ('1' đến '5').
#   + Dữ liệu nhập: Mã SP (str), Tên SP (str), Số lượng (str -> int), Đơn giá (str -> int).
# - Output: Bảng giỏ hàng trực quan, tổng tiền, tổng SL, thông báo lỗi/thành công.
# - Giải pháp & Bẫy lỗi (Edge Cases):
#   + Dùng vòng lặp 'while True' duy trì chương trình, 'match-case' để phân nhánh.
#   + Dùng '.isdigit()' kiểm tra chuỗi số nguyên dương để chặn cả chữ và số âm.
#   + Dùng 'enumerate()' duyệt danh sách để vừa lấy dữ liệu vừa lấy chỉ số (index).

# - Mô tả luồng chương trình (Flow):
#   Bước 1: Hiển thị giao diện Menu chức năng (1-5) và nhận lựa chọn từ người dùng.
#   Bước 2: Kiểm tra lựa chọn (Menu Validation):
#           - Nếu chọn '1': Duyệt qua giỏ hàng -> Tính tiền từng SP -> Cộng dồn tổng -> In bảng.
#           - Nếu chọn '2': Nhập Mã SP trước -> Kiểm tra trùng:
#                           + Nếu trùng: Chỉ yêu cầu nhập Số lượng mới (kiểm tra hợp lệ) -> Cộng dồn.
#                           + Nếu chưa có: Nhập tiếp Tên, Số lượng, Đơn giá (kiểm tra hợp lệ) -> .append() thêm mới.
#           - Nếu chọn '3': Nhập mã cần sửa -> Tìm vị trí (index) -> Nếu không thấy báo lỗi;
#                           Nếu thấy -> Nhập SL mới (kiểm tra hợp lệ) -> Ghi đè vào danh sách.
#           - Nếu chọn '4': Nhập mã cần xóa -> Tìm vị trí (index) -> Nếu không thấy báo lỗi;
#                           Nếu thấy -> Sử dụng .pop(index) để xóa hoàn toàn khỏi giỏ hàng.
#           - Nếu chọn '5': In thông báo tạm biệt và dùng 'break' để kết thúc chương trình.
#           - Ký tự khác: Báo lỗi nhập sai và quay lại Menu ở Bước 1.

#  2. CODE HOÀN CHỈNH
cart_items = [
    ["P001", "Dien thoai iPhone15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True: 
    print('''
=========================================
    SHOPEE CART MANAGEMENT SYSTEM
=========================================
1. Xem chi tiết giỏ hàng & Tính tổng tiền
2. Thêm Sản phẩm mới / Cộng dồn số lượng
3. Cập nhật số lượng của một sản phẩm
4. Xóa Sản phẩm khỏi giỏ hàng
5. Thoát chương trình
=========================================''')
    choice = input('Mời bạn chọn chức năng (1-5): ').strip()
    print()
    match choice:
        case '1':
            print('--- CHI TIẾT GIỎ HÀNG ---')
            print('-' * 80)
            print(f"{'STT':<5} | {'Mã SP':<7} | {'Tên sản phẩm':<25} | {'SL':<4} | {'Đơn giá':<15} | {'Thành tiền':<15}")
            print('-' * 80)
            
            total_items = 0
            total_amount = 0  
            
            for i, item in enumerate(cart_items):
                total_money = item[2] * item[3]
                total_items += item[2]
                total_amount += total_money
                print(f"{i+1:<5} | {item[0]:<7} | {item[1]:<25} | {item[2]:<4} | {item[3]:<15,} | {total_money:<15,}")
            
            print('-' * 80)
            print(f"Tổng sản phẩm có trong giỏ hàng: {total_items}")
            print(f"Tổng tiền thanh toán: {total_amount:,} VND")
        case '2':
            print('--- THÊM SẢN PHẨM MỚI ---')
            product_id = input("Nhập mã sản phẩm: ").strip().upper()
            found_item = None
            for item in cart_items:
                if item[0] == product_id:
                    found_item = item
                    break
            if found_item is not None:
                print(f"-> Sản phẩm [{product_id} - {found_item[1]}] đã có trong giỏ.")
                qty_str = input("Nhập số lượng muốn cộng dồn thêm: ").strip()
                
                if not qty_str.isdigit():
                    print("[Lỗi] Số lượng phải là số nguyên dương hợp lệ!")
                    continue
                quantity = int(qty_str)
                if quantity == 0:
                    print("[Lỗi] Số lượng thêm phải lớn hơn 0!")
                    continue
                found_item[2] += quantity
                print(f"[Thành công] Đã cộng dồn {quantity} sản phẩm vào mã {product_id}. Số lượng mới: {found_item[2]}")
            else:
                print(f"-> Mã '{product_id}' chưa có. Tiến hành thêm mới sản phẩm.")
                product_name = input("Nhập tên sản phẩm: ").strip()
                qty_str = input("Nhập số lượng: ").strip()
                price_str = input("Nhập đơn giá: ").strip()
                
                if not qty_str.isdigit() or not price_str.isdigit():
                    print("[Lỗi] Số lượng và đơn giá phải là số nguyên dương hợp lệ!")
                    continue   
                quantity = int(qty_str)
                price = int(price_str)
                
                if quantity == 0:
                    print("[Lỗi] Số lượng thêm mới phải lớn hơn 0!")
                    continue
                cart_items.append([product_id, product_name, quantity, price])
                print(f"[Thành công] Đã thêm mới sản phẩm {product_id} vào giỏ hàng.")
        case '3':
            print('--- CẬP NHẬT SỐ LƯỢNG SẢN PHẨM ---')
            product_id = input("Nhập mã sản phẩm cần sửa số lượng: ").strip().upper()
            
            found_index = -1
            for i, item in enumerate(cart_items):
                if item[0] == product_id:
                    found_index = i
                    break
            if found_index == -1:
                print(f"[Lỗi] Mã sản phẩm '{product_id}' không tồn tại trong giỏ hàng.")
            else:
                qty_str = input(f"Nhập số lượng mới cho {product_id}: ").strip()
                
                if not qty_str.isdigit():
                    print("[Lỗi] Số lượng phải là số nguyên dương hợp lệ!")
                    continue 
                new_quantity = int(qty_str)              
                if new_quantity == 0:
                    print("[Lỗi] Số lượng cập nhật phải lớn hơn 0!")
                else:
                    cart_items[found_index][2] = new_quantity
                    print(f"[Thành công] Đã cập nhật số lượng mã {product_id} thành {new_quantity}.")            
        case '4':
            print('--- XÓA SẢN PHẨM KHỎI GIỎ HÀNG ---')
            product_id = input("Nhập mã sản phẩm muốn xóa: ").strip().upper()
            
            found_index = -1
            for i, item in enumerate(cart_items):
                if item[0] == product_id:
                    found_index = i
                    break                
            if found_index == -1:
                print(f"[Lỗi] Mã sản phẩm '{product_id}' không tồn tại trong giỏ hàng.")
            else:
                removed_item = cart_items.pop(found_index)
                print(f"[Thành công] Đã xóa sản phẩm '{removed_item[1]}' ({product_id}) khỏi giỏ hàng.")          
        case '5':
            print('Hệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!')
            break        
        case _:
            print('[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 5!')
