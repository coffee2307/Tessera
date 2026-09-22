# Tessera

## English

### Overview

Tessera is a personal precision motion platform for compact XYZ positioning, alignment, probing, microscopy, and small-scale automation. It combines a parallel-kinematic mechanical structure with closed-loop stepper control, rotary encoders, motion planning, and a serial command interface.

The design aims to provide a low-cost and reproducible motion platform with practical sub-micron positioning capability for laboratory, research, and prototyping workflows. The software stack is divided between embedded firmware and a Python control layer so the hardware can be configured, calibrated, and operated through a clean API.

### Main features

- 3-axis XYZ motion using a parallel-kinematic mechanism
- Closed-loop control with stepper motors and encoder feedback
- Sub-micron positioning for precision alignment and inspection work
- USB serial communication with G-code-style command handling
- Firmware-side path planning and interpolation for smooth motion
- Homing and calibration routines for repeatable setup
- External tool control support for device actuation
- Open hardware and software structure for experimentation and customization

### Project architecture

The repository is organized into several functional domains:

- Mechanical design: CAD and manufacturing files in construction/
- Electronics: PCB and schematics in electronics/
- Firmware: embedded C++ controller in firmware/MotionControllerRP/
- Python API: device communication and helper scripts in software/PythonAPI/
- Documentation: build notes, setup guidance, and BOM in documentation/

### Repository structure

- construction/ - CAD models, assemblies, and mechanical parts
- electronics/ - KiCad PCB schematics and board files
- firmware/MotionControllerRP/ - firmware project and embedded source code
- firmware/MotionControllerRP/src/ - C++ firmware implementation
- software/PythonAPI/ - Python API, utilities, and usage examples
- documentation/ - technical documentation, setup references, and BOM

### Mechanical design

The mechanical platform uses a parallel geometry to achieve compact motion with high stiffness and repeatability. The structure is designed around a three-axis motion system, with linkage and ball-joint behavior tuned for controlled end-effector motion. Mechanical files are stored in the FreeCAD-based construction package and are intended to be modified and adapted for custom builds.

### Electronics design

The electronics layer includes the control board and related hardware configuration. The system relies on stepper drives, encoder interfaces, logic/control circuitry, and power distribution arranged to support the motion controller and its real-time feedback loops. These design files are located under electronics/ and provide the hardware reference for the embedded controller.

### Firmware architecture

The firmware is written in C++ and is organized around the real-time device controller. It implements the logic required for motion execution, servo regulation, calibration, and serial communication.

Core firmware responsibilities:

- Kinematic model: workspace and geometry calculations
- Motion controller: command execution and trajectory planning
- Servo control: feedback loops and actuator regulation
- Homing and calibration: initialization and system alignment
- Communication layer: command parsing and response handling

Main firmware components:

- firmware/MotionControllerRP/src/main.cpp - startup and system initialization
- firmware/MotionControllerRP/src/robot.cpp - coordinated device behavior
- firmware/MotionControllerRP/src/motion_control/ - path planning and movement logic
- firmware/MotionControllerRP/src/servo_control/ - closed-loop control loops
- firmware/MotionControllerRP/src/kinematic_models/ - geometry and kinematic calculations
- firmware/MotionControllerRP/src/hw_config.h - hardware configuration such as pin map and motor settings

### Control and communication model

The system is intended to be commanded over a serial connection. The firmware accepts motion and control instructions and returns status information to the host. This makes it compatible with higher-level control software, automation workflows, and Python-based experimentation.

Typical capabilities include:

- moving to target coordinates
- homing the axes
- enabling or disabling motors
- querying device state
- calibrating joints
- setting tool output values

### Python API

The Python layer wraps the serial connection and exposes a simplified interface for controlling the platform. It is intended to reduce the amount of low-level command handling required when testing motion, calibration, or automated procedures.

Relevant Python files:

- software/PythonAPI/tessera_api.py
- software/PythonAPI/usage_example.py
- software/PythonAPI/calibration_plotter.py

The API generally supports:

- connection management
- homing and motion commands
- calibration routines
- device status queries
- asynchronous logging and communication feedback

### Quick start

1. Review the mechanical and electrical documentation in documentation/.
2. Build the hardware according to the project instructions.
3. Adjust the hardware configuration in firmware/MotionControllerRP/src/hw_config.h.
4. Flash the firmware using PlatformIO.
5. Connect the device over serial.
6. Use the Python API or a terminal client to home the platform and begin motion testing.

### Example usage

```python
from software.PythonAPI.tessera_api import TesseraInterface

api = TesseraInterface(show_communication=True, show_log_messages=True)
api.connect('/dev/ttyACM0')

api.home()
api.move_to(0.0, 0.0, 0.0, f=10)
api.move_to(3.1, 4.1, 5.9, f=26)
api.wait_for_stop()
```

### Notes

- The project is designed for open experimentation and reproducible builds.
- The firmware and mechanical system are the primary technical foundations of the repository.
- The Python layer is meant to simplify communication, testing, calibration, and operational workflows.

---

## Tiếng Việt

### Tổng quan

Tessera là một nền tảng chuyển động XYZ kiểu compact, mã nguồn mở, được thiết kế cho các nhiệm vụ căn chỉnh, dò kiểm tra, kính hiển vi và tự động hóa quy mô nhỏ. Hệ thống này kết hợp cơ cấu cơ khí song song, bộ điều khiển động cơ vòng kín, và giao diện điều khiển thân thiện với Python để tạo ra một giải pháp di chuyển chính xác với chi phí thấp và khả năng tái tạo tốt.

### Tính năng chính

- Chuyển động 3 trục XYZ theo cơ cấu song song
- Điều khiển vòng kín bằng động cơ bước và bộ mã hóa quay
- Khả năng định vị ở mức dưới micromet cho công việc căn chỉnh và kiểm tra
- Giao tiếp qua cổng serial USB với lệnh kiểu G-code
- Lập lịch đường đi và nội suy chuyển động ở phần firmware
- Chức năng homing và hiệu chuẩn để khởi tạo hệ thống lặp lại
- Hỗ trợ điều khiển đầu công cụ ngoài để kích hoạt thiết bị phụ trợ
- Cấu trúc phần cứng và phần mềm mở, dễ tùy biến và thử nghiệm

### Kiến trúc dự án

Kho mã nguồn được tổ chức theo các tầng chức năng chính:

- Thiết kế cơ khí: mô hình CAD và file gia công trong construction/
- Điện tử: bo mạch và sơ đồ trong electronics/
- Firmware: bộ điều khiển nhúng C++ trong firmware/MotionControllerRP/
- Python API: giao tiếp thiết bị và script hỗ trợ trong software/PythonAPI/
- Tài liệu: hướng dẫn xây dựng, thiết lập và BOM trong documentation/

### Cấu trúc thư mục

- construction/ - mô hình CAD, bộ lắp ráp và linh kiện cơ khí
- electronics/ - file sơ đồ PCB KiCad và board layout
- firmware/MotionControllerRP/ - mã nguồn firmware và dự án PlatformIO
- firmware/MotionControllerRP/src/ - phần triển khai firmware C++
- software/PythonAPI/ - API Python, tiện ích và ví dụ sử dụng
- documentation/ - tài liệu kỹ thuật, hướng dẫn lắp đặt và danh mục vật tư

### Thiết kế cơ khí

Cấu trúc cơ khí sử dụng hình học song song để đạt được chuyển động nhỏ gọn, cứng vững và lặp lại tốt. Hệ thống được thiết kế theo mô hình 3 trục với các liên kết và khớp cầu nhằm kiểm soát chuyển động của đầu công cụ. Các file thiết kế cơ khí nằm trong gói CAD FreeCAD và có thể được chỉnh sửa để phù hợp với từng bản dựng cụ thể.

### Thiết kế điện tử

Lớp điện tử bao gồm bo mạch điều khiển và cấu hình phần cứng tương ứng. Hệ thống dùng động cơ bước, giao diện mã hóa, mạch điều khiển logic và phân phối nguồn để hỗ trợ bộ điều khiển chuyển động và vòng phản hồi thời gian thực. Các file này nằm trong electronics/ và là tài liệu tham khảo cho phần firmware.

### Kiến trúc firmware

Firmware được viết bằng C++ và tổ chức theo mô hình bộ điều khiển thiết bị thời gian thực. Nó xử lý các nhiệm vụ cần thiết cho việc thực thi chuyển động, điều khiển servo, hiệu chuẩn và giao tiếp serial.

Các trách nhiệm chính của firmware:

- Mô hình động học: tính toán không gian làm việc và hình học
- Bộ điều khiển chuyển động: thực thi lệnh và lập kế hoạch quỹ đạo
- Điều khiển servo: vòng lặp phản hồi và điều chỉnh actuator
- Homing và hiệu chuẩn: khởi tạo và căn chỉnh hệ thống
- Lớp giao tiếp: phân tích lệnh và xử lý phản hồi

Những thành phần quan trọng:

- firmware/MotionControllerRP/src/main.cpp - khởi động và khởi tạo hệ thống
- firmware/MotionControllerRP/src/robot.cpp - hành vi tổng hợp của thiết bị
- firmware/MotionControllerRP/src/motion_control/ - logic lập kế hoạch đường đi
- firmware/MotionControllerRP/src/servo_control/ - vòng lặp điều khiển đóng
- firmware/MotionControllerRP/src/kinematic_models/ - tính toán hình học và động học
- firmware/MotionControllerRP/src/hw_config.h - cấu hình phần cứng như chân GPIO và cài đặt motor

### Mô hình điều khiển và truyền thông

Hệ thống được thiết kế để điều khiển qua kết nối serial. Firmware nhận lệnh di chuyển và điều khiển từ máy tính và gửi thông tin trạng thái trở lại. Điều này giúp hệ thống tương thích với phần mềm điều khiển cấp cao, quy trình tự động hóa và thử nghiệm dựa trên Python.

Các khả năng điển hình gồm:

- di chuyển đến tọa độ mục tiêu
- homing trục
- bật/tắt động cơ
- truy vấn trạng thái thiết bị
- hiệu chuẩn joint
- đặt giá trị đầu ra của công cụ

### Python API

Lớp Python đóng gói kết nối serial và cung cấp giao diện đơn giản để điều khiển hệ thống. Mục tiêu là giảm khối lượng xử lý lệnh mức thấp khi kiểm tra chuyển động, hiệu chuẩn hoặc quy trình tự động hóa.

Các file Python quan trọng:

- software/PythonAPI/tessera_api.py
- software/PythonAPI/usage_example.py
- software/PythonAPI/calibration_plotter.py

API thường hỗ trợ:

- quản lý kết nối
- lệnh homing và di chuyển
- chức năng hiệu chuẩn
- truy vấn trạng thái thiết bị
- log giao tiếp và phản hồi liên tục

### Bắt đầu nhanh

1. Đọc tài liệu cơ khí và điện tử trong documentation/
2. Lắp ráp phần cứng theo hướng dẫn của dự án
3. Điều chỉnh cấu hình phần cứng trong firmware/MotionControllerRP/src/hw_config.h
4. Nạp firmware bằng PlatformIO
5. Kết nối thiết bị qua serial
6. Dùng Python API hoặc client terminal để homing trục và bắt đầu kiểm tra chuyển động

### Ví dụ sử dụng

```python
from software.PythonAPI.tessera_api import TesseraInterface

api = TesseraInterface(show_communication=True, show_log_messages=True)
api.connect('/dev/ttyACM0')

api.home()
api.move_to(0.0, 0.0, 0.0, f=10)
api.move_to(3.1, 4.1, 5.9, f=26)
api.wait_for_stop()
```

### Lưu ý

- Dự án này thích hợp cho thử nghiệm mở và bản dựng có thể tái sản xuất.
- Firmware và hệ thống cơ khí là nền tảng kỹ thuật chính của kho mã nguồn.
- Lớp Python nhằm đơn giản hóa giao tiếp, thử nghiệm, hiệu chuẩn và quy trình vận hành.
