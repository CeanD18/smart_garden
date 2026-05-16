# BÁO CÁO CHUYÊN ĐỀ HỌC PHẦN: PHẦN MỀM MÃ NGUỒN MỞ
## ĐỀ TÀI: SỬ DỤNG PHẦN MỀM MÃ NGUỒN MỞ WORDPRESS VÀ NGÔN NGỮ LẬP TRÌNH PHP XÂY DỰNG WEBSITE KINH DOANH CÂY CẢNH

---

# 📝 1. Giới Thiệu Website / Hệ Thống

Hệ thống là một nền tảng thương mại điện tử chuyên biệt cho lĩnh vực kinh doanh cây cảnh với tên thương hiệu hiển thị trên giao diện là **Greenstore**. Dự án hướng tới việc tận dụng tối đa sức mạnh của phần mềm mã nguồn mở để tối ưu hóa chi phí phát triển và nâng cao hiệu quả vận hành cho các mô hình kinh doanh vừa và nhỏ.

Website được xây dựng dựa trên nền tảng **WordPress CMS**, vận hành theo cấu trúc kiến trúc phân lớp (Layered Architecture) nhằm đảm bảo tính module hóa và khả năng mở rộng linh hoạt. Thay vì sử dụng cấu trúc bài viết mặc định phức tạp, nhóm đã chủ động tùy biến cấu trúc dữ liệu chuyên sâu bằng kỹ thuật **Custom Post Type (CPT)** và **Advanced Custom Fields (ACF)** để quản lý sản phẩm, đơn hàng và các biến thể đặc thù của ngành cây cảnh một cách hệ thống và minh bạch.

## Các chức năng nổi bật đã hoàn thành của hệ thống:

- **Quản lý sản phẩm chuyên sâu (CPT):**  
  Triển khai thành công Custom Post Type để tách biệt hoàn toàn dữ liệu hàng hóa cây cảnh khỏi bài viết thông thường.

- **Cấu trúc dữ liệu chi tiết qua ACF:**  
  Thiết lập đầy đủ các trường thông tin động đặc thù bao gồm giá gốc (`base_price`), giá khuyến mãi (`discount_price`), thuộc tính màu sắc (`color`), kích thước (`size`) và quản lý tồn kho (`stock_quantity`).

- **Quy trình giỏ hàng linh hoạt (Guest Checkout):**  
  Cho phép khách hàng thực hiện các thao tác thêm, xóa và cập nhật số lượng sản phẩm trực tiếp từ Frontend mà không bắt buộc phải đăng nhập hệ thống.

- **Bộ lọc và tìm kiếm đa tiêu chí:**  
  Tích hợp bộ lọc thông minh dựa trên danh mục, đặc tính thuộc tính (màu sắc, kích cỡ) và khoảng giá giúp người dùng tiếp cận sản phẩm mong muốn nhanh chóng.

- **Tự động hóa logic nghiệp vụ (Hook):**  
  Sử dụng Action hook `acf/save_post` để can thiệp vào quy trình lưu trữ dữ liệu, thực hiện tự động trừ số lượng hàng trong kho ngay khi đơn hàng được xác nhận thành công.

- **Thanh toán tự động qua mã QR động:**  
  Tích hợp giải pháp gọi API cổng thanh toán (PayOS/SePay) kết hợp Webhook endpoint để sinh mã VietQR chứa chính xác số tiền cùng nội dung chuyển khoản, tự động đồng bộ trạng thái đơn hàng khi giao dịch hoàn tất.

- **Giao diện tương thích (Responsive Design):**  
  Đảm bảo hệ thống hiển thị chỉn chu, đồng nhất và chuyên nghiệp trên cả thiết bị máy tính để bàn và điện thoại di động nhờ sự kết hợp giữa Elementor và CSS tùy chỉnh.

---

# 👥 2. Danh Sách Thành Viên & Phân Công Nhiệm Vụ

Dự án được hoàn thiện bởi **Nhóm 17** - Lớp **D18CNPM1**, Khóa **2023-2028**, Chuyên ngành Công nghệ phần mềm, Khoa Công nghệ thông tin, Trường Đại học Điện lực.

| STT | Họ và Tên | MSSV | Nội Dung Phụ Trách Chính | Mức Độ Đóng Góp |
|-----|------------|------|----------------------------|----------------|
| 1 | **Hoàng Tùng Dương** | 23810310015 | Nghiên cứu tổng quan, thiết kế giao diện UI/UX (Trang chủ, Chi tiết sản phẩm), tối ưu hóa hiển thị Responsive | 100% |
| 2 | **Nguyễn Huy Tiệp** | 23810310005 | Phát triển logic nghiệp vụ (PHP), cấu trúc hệ thống CPT & ACF, xử lý logic giỏ hàng và trừ kho tự động | 100% |
| 3 | **Nguyễn Văn Phong** | 23810310034 | Thiết kế cơ sở dữ liệu MySQL, cấu trúc tệp tin hệ thống, xây dựng chức năng tìm kiếm và lọc sản phẩm đa tầng | 100% |

---

# 🛠 3. Công Nghệ Sử Dụng

Hệ thống kết hợp đồng bộ các giải pháp công nghệ mã nguồn mở tối ưu:

- **Quản lý nội dung:** WordPress CMS.
- **Ngôn ngữ lập trình phía Server:** PHP.
- **Hệ quản trị cơ sở dữ liệu:** MySQL.
- **Thiết kế giao diện Frontend:** Elementor Website Builder kết hợp HTML5 & CSS3 tùy chỉnh.

## Các plugin mã nguồn mở bổ trợ chức năng:

- **Custom Post Type UI (CPT UI) v1.16.x**
  - Tạo cấu trúc loại nội dung riêng biệt bao gồm:
    - `products`
    - `orders`
    - `variants`

- **Advanced Custom Fields (ACF) v6.x**
  - Mở rộng các trường thông tin động:
    - Giá gốc
    - Tồn kho
    - Màu sắc
    - Kích thước

- **PayOS / SePay WordPress Plugin v1.x**
  - Hỗ trợ cấu hình Endpoint xử lý và tích hợp luồng dữ liệu cổng thanh toán qua mã QR.

---

# 💻 4. Hướng Dẫn Cài Đặt & Triển Khai (Localhost)

Để cài đặt và triển khai chạy dự án website thương mại điện tử trên môi trường máy chủ cục bộ, nhóm sử dụng phần mềm giả lập **XAMPP** trên hệ điều hành Windows.

## Bước 4.1: Chuẩn bị mã nguồn dự án

1. Tải về thư mục mã nguồn project của nhóm.
2. Copy toàn bộ thư mục dự án vào:

```plaintext
C:\xampp\htdocs\
```

3. Đổi tên thư mục mã nguồn thành:

```plaintext
wordpress
```

---

## Bước 4.2: Kích hoạt Server Localhost

1. Khởi chạy ứng dụng **XAMPP Control Panel**.
2. Nhấn nút **Start** tại:
   - Apache
   - MySQL

3. Khi hai dịch vụ hiển thị màu xanh nghĩa là môi trường localhost đã hoạt động thành công.

---

## Bước 4.3: Thiết lập và Khởi tạo Cơ sở dữ liệu

1. Mở trình duyệt và truy cập:

```plaintext
http://localhost/phpmyadmin/
```

2. Chọn mục **New** hoặc **Cơ sở dữ liệu**.
3. Tạo database với tên:

```plaintext
db_caycanh
```

4. Chọn Collation:

```plaintext
utf8mb4_general_ci
```

5. Nhấn **Create** để khởi tạo database.
6. Chọn database `db_caycanh` vừa tạo.
7. Chọn tab **Import**.
8. Tải file `.sql` đi kèm project để phục hồi dữ liệu hệ thống.
9. Nhấn **Go** để hoàn tất import cơ sở dữ liệu.

---

## Bước 4.4: Cấu hình kết nối WordPress

Mở file cấu hình:

```plaintext
C:\xampp\htdocs\wordpress\wp-config.php
```

Tìm và chỉnh sửa:

```php
define( 'DB_NAME', 'db_caycanh' );
define( 'DB_USER', 'root' );
define( 'DB_PASSWORD', '' );
define( 'DB_HOST', 'localhost' );
```

Lưu lại tệp sau khi hoàn thành.

---

# 🚀 5. Hướng Dẫn Chạy & Sử Dụng Project

Dự án hỗ trợ vận hành trên:

- Môi trường Online đã Deploy
- Môi trường Localhost

---

## 🌐 5.1. Chạy trên Môi trường Online

### Trang cửa hàng dành cho khách hàng

Truy cập:

```plaintext
https://caycanhon.click/wordpress/shop/
```

### Các chức năng hỗ trợ

- Xem danh sách sản phẩm cây cảnh
- Tìm kiếm sản phẩm theo từ khóa
- Bộ lọc:
  - Khoảng giá
  - Danh mục
  - Màu sắc
  - Kích thước
- Quản lý giỏ hàng
- Đặt hàng không cần đăng nhập (Guest Checkout)
- Thanh toán QR tự động VietQR

---

### Trang quản trị Admin

Truy cập:

```plaintext
https://caycanhon.click/wordpress/wp-admin/
```

### Tài khoản Demo

| Thông tin | Giá trị |
|-----------|----------|
| Username | `phong2005` |
| Password | `phong15122005z` |

---

## 🖥 5.2. Chạy trên Môi trường Localhost

### A. Giao diện Frontend

Sau khi hoàn tất cài đặt, truy cập:

```plaintext
http://localhost/wordpress/
```

Người dùng có thể:
- Tìm kiếm sản phẩm
- Sử dụng bộ lọc
- Thêm sản phẩm vào giỏ hàng
- Thanh toán
- Đặt hàng

---

### B. Giao diện Backend

Đường dẫn truy cập:

```plaintext
http://localhost/wordpress/wp-admin/
```

### Tài khoản Demo

| Thông tin | Giá trị |
|-----------|----------|
| Username | `phong2005` |
| Password | `phong15122005z` |

---

# 🔗 6. Liên Kết Trực Tuyến & Video Minh Họa

## Website Online

```plaintext
https://caycanhon.click/wordpress/shop/
```

## Video Demo

```plaintext
(https://drive.google.com/file/d/1wUc50SZx20ca0n3hxnpUKggRfZuXpWEK/view?usp=drivesdk)
```

---

# 📸 7. Hình Ảnh Minh Họa Hệ Thống

> Lưu ý:
> Tạo thư mục `images` tại thư mục gốc project và đặt các ảnh giao diện vào đó.

---

## 7.1. Giao diện Trang chủ

Trang chủ hiển thị banner chính với phong cách hiện đại, tối giản.

```markdown
![Trang chủ](images/homepage.png)
```

---

## 7.2. Trang danh sách sản phẩm & Bộ lọc

Bao gồm:
- Thanh tìm kiếm
- Bộ lọc khoảng giá
- Bộ lọc thuộc tính

```markdown
![Shop Page](images/shop-page.png)
```

---

## 7.3. Trang chi tiết sản phẩm

Hiển thị:
- Hình ảnh sản phẩm
- Giá bán
- Thông tin chi tiết
- Nút mua hàng

```markdown
![Chi tiết sản phẩm](images/product-detail.png)
```

---

## 7.4. Giao diện Thanh toán QR

QR động VietQR tự sinh theo nội dung đơn hàng.

```markdown
![Thanh toán QR](images/payment-qr.png)
```

---

## 7.5. Dashboard quản trị Backend

Giao diện quản trị dữ liệu tập trung cho Admin.

```markdown
![Dashboard](images/admin-dashboard.png)
```

---

# ✅ 8. Kết Luận

Dự án website thương mại điện tử cây cảnh Greenstore đã hoàn thiện đầy đủ các chức năng cốt lõi của một hệ thống bán hàng trực tuyến hiện đại trên nền tảng mã nguồn mở WordPress.

Thông qua việc áp dụng:
- WordPress CMS
- PHP
- MySQL
- Custom Post Type (CPT)
- Advanced Custom Fields (ACF)
- API thanh toán QR động

Nhóm đã xây dựng thành công hệ thống:
- Quản lý sản phẩm
- Quản lý đơn hàng
- Tìm kiếm & lọc dữ liệu
- Giỏ hàng
- Thanh toán tự động
- Responsive Design

Dự án giúp nhóm củng cố kiến thức về:
- Phát triển web mã nguồn mở
- Quản trị cơ sở dữ liệu
- Xử lý nghiệp vụ bằng PHP
- Kiến trúc hệ thống WordPress
- Triển khai website thực tế

Đồng thời tạo nền tảng để tiếp tục mở rộng thành các hệ thống thương mại điện tử chuyên nghiệp trong tương lai.
