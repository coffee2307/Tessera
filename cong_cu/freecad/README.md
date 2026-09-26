# Chỉnh sửa mô hình FreeCAD Tessera

## Chạy

- Trong VS Code, chọn **Terminal > Run Task > FreeCAD: Edit Tessera**.
- Hoặc mở PowerShell tại thư mục dự án và chạy:

```powershell
& ".\cong_cu\freecad\run_freecad.ps1"
```

Script được chạy bằng Python tích hợp trong FreeCAD, không cần cài thư viện FreeCAD bằng pip. Với đối tượng `App::Link`, FreeCAD cần chạy trong GUI để có `ViewObject`; `freecadcmd.exe` ở chế độ headless không thể đổi màu riêng cho Link. Khi đó, mở FreeCAD GUI, mở Python console và chạy:

```python
exec(compile(open(r"F:\Tessera\cong_cu\freecad\edit_tessera.py", "rb").read(), r"F:\Tessera\cong_cu\freecad\edit_tessera.py", "exec"))
```

## Tệp

- Tệp đầu vào: `thiet_ke_co_khi/bo_thao_tac_vi_mo/Assembly_MicroManipulator.FCStd`
- Bản sao lưu: `thiet_ke_co_khi/bo_thao_tac_vi_mo/Assembly_MicroManipulator.backup.FCStd`
- Tệp đầu ra: `thiet_ke_co_khi/bo_thao_tac_vi_mo/Assembly_MicroManipulator_edited.FCStd`

Bản sao lưu chỉ được tạo nếu chưa tồn tại. Tệp đầu vào không bị ghi đè.

## Tùy chỉnh

Để đổi đối tượng, sửa giá trị `TARGET_NAME` trong `edit_tessera.py`.
Để đổi màu, sửa `TARGET_COLOR` bằng ba giá trị RGB từ `0` đến `255`, được chuyển thành dạng số thực khi cần. Mặc định là vàng RGB `(255, 191, 0)`.

Tệp `.FCStd` là tệp mô hình nhị phân có cấu trúc riêng; không nên sửa trực tiếp bằng trình soạn thảo văn bản. Hãy chỉnh qua FreeCAD hoặc script này.