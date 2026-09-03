# Báo cáo traffic ngành hàng Laptop

Trang tĩnh phục vụ nhân sự ngành hàng Laptop, cập nhật hàng tháng. Nguồn số liệu:
Google Search Console, property `thegioididong.com`.

Site: GitHub Pages của repo này.

## Cảnh báo về mức độ công khai

GitHub Pages **luôn công khai** — kể cả khi repo private, URL của site ai có cũng
xem được. `robots.txt` và thẻ `noindex` chỉ ngăn Google liệt kê, **không** làm trang
thành riêng tư:

- Người được chuyển tiếp link vẫn xem được, và không thu hồi được.
- Crawler không tôn trọng robots (Ahrefs, Semrush, Common Crawl) vẫn có thể lấy.
- Wayback Machine vẫn có thể lưu.

Nội dung ở đây là số traffic nội bộ chia theo hãng. Đưa thêm gì lên thì cân nhắc
theo tiêu chí đó. Không đưa giá vốn, tồn kho, kế hoạch hàng, hay dữ liệu cá nhân.

## Cấu trúc

| File | Vai trò |
| --- | --- |
| `src/report.html` | **Nguồn duy nhất.** Fragment không có `<head>`; cũng là file publish lên Claude Artifact |
| `build.py` | Bọc fragment thành `index.html` standalone, thêm noindex |
| `index.html` | File Pages phục vụ — **sinh ra, đừng sửa tay** |
| `robots.txt` | `Disallow: /` |
| `.nojekyll` | Tắt Jekyll, phục vụ file thô |

Sửa `src/report.html`, chạy `python3 build.py`, commit cả hai.

## Cập nhật hàng tháng

Số liệu đến từ workspace `mwg-ai-worker`. Thứ tự đúng:

1. Trong `mwg-ai-worker`: fetch GSC theo scope `nh-laptop-ex-apple`, rồi
   **cập nhật snapshot trước** (`tools/gsc/append-monthly-snapshot.py`).
   Quy trình đầy đủ: `mwg-seo-analytics/docs/recurring-category-review.md`.
2. Sửa số trong `src/report.html` theo snapshot — không gõ số từ chỗ khác, để
   trang và chuỗi lịch sử không lệch nhau.
3. `python3 build.py`
4. Commit + push. Pages tự deploy lại.

## Phạm vi số liệu

`Nhóm NH = Laptop`, 5 sub-ngành: laptop, máy tính để bàn, màn hình máy tính, máy in,
phần mềm. **Đã loại toàn bộ sản phẩm Apple** ở cả 2 chiều URL và keyword. Không gồm
bài `/hoi-dap/` và `/tin-tuc/`.

Định nghĩa filter chính xác: `mwg-ai-worker/mwg-seo-analytics/scopes/nh-laptop-ex-apple.json`.
