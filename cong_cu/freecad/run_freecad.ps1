$ErrorActionPreference = "Stop"

$freeCadPath = "C:\Users\abc23\AppData\Local\Programs\FreeCAD 1.1\bin\freecad.exe"
$freeCadCmdPath = Join-Path (Split-Path -Parent $freeCadPath) "freecadcmd.exe"
$scriptPath = Join-Path $PSScriptRoot "edit_tessera.py"

try {
    if (-not (Test-Path -LiteralPath $freeCadPath -PathType Leaf)) {
        throw "Không tìm thấy FreeCAD tại: $freeCadPath"
    }

    if (-not (Test-Path -LiteralPath $scriptPath -PathType Leaf)) {
        throw "Không tìm thấy script chỉnh sửa tại: $scriptPath"
    }

    if (-not (Test-Path -LiteralPath $freeCadCmdPath -PathType Leaf)) {
        throw "Không tìm thấy freecadcmd.exe cạnh FreeCAD tại: $freeCadCmdPath"
    }

    Write-Host "Đang chạy edit_tessera.py bằng trình Python của FreeCAD..."
    $pythonCommand = "__file__ = r'$scriptPath'; __name__ = '__main__'; exec(compile(open(__file__, 'rb').read(), __file__, 'exec'), globals(), globals())"
    & $freeCadCmdPath -c $pythonCommand
    $exitCode = $LASTEXITCODE
    if ($null -ne $exitCode -and $exitCode -ne 0) {
        throw "FreeCAD kết thúc với mã lỗi $exitCode."
    }

    Write-Host "FreeCAD đã chạy thành công script chỉnh sửa."
    exit 0
}
catch {
    Write-Error "Chạy công cụ FreeCAD thất bại: $($_.Exception.Message)"
    exit 1
}