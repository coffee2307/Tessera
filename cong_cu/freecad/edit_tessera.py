"""Edit the Tessera FreeCAD assembly without modifying the source file."""

from pathlib import Path
import shutil
import sys


TARGET_NAME = "MotorHorn004"
TARGET_COLOR = (1.0, 191.0 / 255.0, 0.0)


def find_source_file(project_root):
    matches = sorted(
        path
        for path in project_root.rglob("Assembly_MicroManipulator.FCStd")
        if path.is_file()
    )
    if not matches:
        raise FileNotFoundError(
            "Không tìm thấy Assembly_MicroManipulator.FCStd trong dự án."
        )
    return matches[0]


def set_target_color(target):
    view = getattr(target, "ViewObject", None)
    if view is None:
        raise RuntimeError(
            "MotorHorn004 là App::Link nhưng FreeCAD đang chạy không có giao diện "
            "đồ họa (ViewObject). Hãy chạy script trong FreeCAD GUI có Python console."
        )

    if hasattr(view, "OverrideMaterial"):
        view.OverrideMaterial = True

    view.ShapeColor = TARGET_COLOR
    view.LineColor = TARGET_COLOR


def main():
    project_root = Path(__file__).resolve().parents[2]
    source_path = None
    document = None

    try:
        source_path = find_source_file(project_root)
        print("Đã tìm thấy tệp: {}".format(source_path))

        backup_path = source_path.with_name("Assembly_MicroManipulator.backup.FCStd")
        if not backup_path.exists():
            shutil.copy2(source_path, backup_path)
            print("Đã tạo bản sao lưu: {}".format(backup_path))
        else:
            print("Bản sao lưu đã tồn tại, giữ nguyên: {}".format(backup_path))

        import FreeCAD as App

        try:
            document = App.openDocument(str(source_path))
            if document is None:
                raise RuntimeError("FreeCAD không mở được tệp mô hình.")
            print("Đã mở mô hình bằng FreeCAD.")
        except Exception as error:
            raise RuntimeError("Lỗi ở bước mở mô hình: {}".format(error)) from error

        target = document.getObject(TARGET_NAME)
        if target is None:
            raise LookupError(
                "Không tìm thấy đối tượng '{}' trong mô hình.".format(TARGET_NAME)
            )
        print("Đã tìm thấy đối tượng: {} ({}).".format(TARGET_NAME, target.TypeId))

        try:
            is_link = target.TypeId == "App::Link" or hasattr(target, "LinkedObject")
            set_target_color(target)
            if is_link:
                print("Đã đổi màu riêng cho Link {}.".format(TARGET_NAME))
            else:
                print("Đã đổi màu đối tượng {}.".format(TARGET_NAME))
        except Exception as error:
            raise RuntimeError("Lỗi ở bước đổi màu: {}".format(error)) from error

        try:
            document.recompute()
            output_path = source_path.with_name(
                "Assembly_MicroManipulator_edited.FCStd"
            )
            document.saveAs(str(output_path))
            print("Đã lưu thành công tệp kết quả: {}".format(output_path))
        except Exception as error:
            raise RuntimeError("Lỗi ở bước recompute/lưu tệp: {}".format(error)) from error
    except Exception as error:
        print("LỖI: {}".format(error), file=sys.stderr)
        return 1
    finally:
        if document is not None:
            try:
                import FreeCAD as App

                App.closeDocument(document.Name)
            except Exception:
                pass

    return 0


if __name__ == "__main__":
    sys.exit(main())