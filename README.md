# Hệ thống Truy xuất Hình ảnh bằng Nội dung dựa trên CNN và Hash

## Mục lục
1. [Giới thiệu tổng quan](#giới-thiệu-tổng-quan)
2. [Mô hình đề xuất](#mô-hình-đề-xuất)
3. [Thực nghiệm](#thực-nghiệm)
4. [Kết luận và hướng phát triển](#kết-luận-và-hướng-phát-triển)
5. [Tài liệu tham khảo](#tài-liệu-tham-khảo)

## 1. Giới thiệu tổng quan
Trong thực tế hiện nay, với sự phát triển của công nghệ thông tin, nhu cầu tìm kiếm và truy xuất thông tin đang tăng cao, đặc biệt là truy xuất hình ảnh. Trong nghiên cứu này, nhóm đề xuất sử dụng phương pháp học sâu - Mạng nơ-ron tích chập (CNN), kết hợp với hàm Hash để xử lí bài toán truy xuất hình ảnh. Mô hình đề xuất đã đạt được độ chính xác phân loại là 0.95 và với truy xuất đạt độ đo MAP200 lên tới 0.93. Dựa trên kết quả đó, nhóm đã xây dựng hệ thống truy xuất hình ảnh.

## 2. Mô hình đề xuất
### 2.2. Quá trình truy xuất ảnh


<img src="https://github.com/DuyTam01/cbir_cnn_and_hash/assets/92566983/8ef1857e-5788-46e9-9117-2b0050ee5524" alt="image" width="300" height="auto"/>

### 2.1. Kiến trúc mô hình đề xuất
Trong đề xuất của nhóm, hệ thống sử dụng phương pháp học sâu CNN để thực hiện phân loại và truy xuất hình ảnh. Mô hình kiến trúc được mô tả:

<img src="https://github.com/DuyTam01/cbir_cnn_and_hash/assets/92566983/1c49e3ca-cfc7-4721-95a4-f67c356af4cf" alt="image" width="600" height="auto"/>

## 3. Thực nghiệm
Trong quá trình thực nghiệm, nhóm đã tiến hành huấn luyện và kiểm tra mô hình đề xuất trên các tập dữ liệu phù hợp. Kết quả và các chi tiết thực nghiệm được trình bày trong phần này ở poster.

## 4. Kết luận và hướng phát triển

 - Mô hình đề xuất có độ chính xác tốt cùng với tốc độ truy vấn nhanh, có thể ứng dụng vào xây dựng vào trang web thương mại điện tử phục vụ mục đích tìm kiếm của khách hàng
 - Ứng dụng phương pháp tìm kiếm hình ảnh và mã nhị phân vào lĩnh vực y khoa, như phân loại hay tìm kiếm ảnh y tế.

## 5. Tài liệu tham khảo

![image](https://github.com/DuyTam01/cbir_cnn_and_hash/assets/92566983/4e31d17e-c3d2-480d-a96c-f7cb9db42826)


