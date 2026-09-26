# Python API

This folder contains a lightweight Python interface for the Tessera serial protocol, plus two small example scripts:

- `vi_du_su_dung.py`: homes the device, performs a simple move, and prints device state information.
- `ve_bieu_do_hieu_chuan.py`: runs joint calibration for the first three actuators and plots the returned data.

## Requirements

Install the Python dependencies with:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

The public API is exposed by `tessera_api.py`. The original implementation
module remains available for compatibility with existing scripts.

## Serial Port Selection

Both scripts support:

- `--list-ports`: list detected serial devices and exit
- `--port <PORT>`: explicitly select a serial port

If `--port` is not provided, the scripts try to choose a port automatically:

1. If exactly one detected device contains `Pico` in its name, that port is used.
2. Otherwise, if there is exactly one detected serial device, that port is used.
3. Otherwise, the script lists the available ports and exits.

## Running The Example Script

From this folder:

```bash
python vi_du_su_dung.py --list-ports
python vi_du_su_dung.py --port /dev/ttyACM0
```

On Windows, a typical command looks like:

```bash
python vi_du_su_dung.py --port COM3
```

## Running The Calibration Plotter

From this folder:

```bash
python ve_bieu_do_hieu_chuan.py --list-ports
python ve_bieu_do_hieu_chuan.py --port /dev/ttyACM0
```

The calibration script opens a matplotlib window with the measured calibration curves.

## Running From The Repository Root

If you prefer to run the scripts from the repository root, use:

```bash
python software/PythonAPI/vi_du_su_dung.py --port /dev/ttyACM0
python software/PythonAPI/ve_bieu_do_hieu_chuan.py --port /dev/ttyACM0
```

