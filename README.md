# Mouse Polling Rate Checker

This is a Python script that displays your current mouse polling rate on Windows.

## Requirements

- Python 3.6 or higher
- pyautogui module
- polling module

You can install the modules with:

```bash
pip install pyautogui
pip install polling
```

## Usage

To run the script, simply execute it with Python:

```bash
python mouse_polling_rate.py
```

The script will prompt you to click and move your mouse to start. It will then estimate your mouse polling rate in hertz and print it to the console.

## How it works

The script uses the following steps to estimate the mouse polling rate:

- It uses the pyautogui module to get the current mouse position and speed.
- It uses the polling module to poll the mouse speed function until it returns a value greater than 0, which means the mouse is moving.
- It then polls the mouse position function until it returns a different value than the initial one, which means the mouse position has changed.
- It calculates the time difference between the two mouse position changes in seconds.
- It estimates the polling rate in hertz by taking the inverse of the time difference.

## Limitations

This script is intended for educational purposes only and may not work as expected. Some of the limitations are:

- The script may not be accurate or consistent depending on your mouse settings, hardware, and environment.
- The script may not work well with high-polling rate mice (above 1000 Hz) or low-resolution screens.
- The script may not handle errors or exceptions gracefully.

## License

This script is licensed under the GNU 3.0 License. See [LICENSE](LICENSE) for details.

## Contributing

If you find any bugs or have any suggestions for improvement, feel free to open an issue or a pull request.
