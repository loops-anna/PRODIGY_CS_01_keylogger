# Keylogger

A basic keylogger that records keystrokes to a file. **Educational purposes only.**

## ⚠️ Legal and Ethical Warning

**This tool is for educational learning purposes only.** Unauthorized keylogging is illegal in most jurisdictions. Only use this code:
- On your own systems for learning
- In authorized testing environments with explicit permission
- For security research and education

## Features

- Records all keyboard keystrokes
- Includes special keys (shift, ctrl, enter, etc.)
- Saves output to `keylog.txt`
- Stops when ESC key is pressed

## Requirements

```
Python 3.6+
pynput library
Graphical environment (X server) - will NOT work headless
```

## Installation

```bash
pip install pynput
```

## Usage

```bash
python keylogger.py
```

The keylogger will start recording immediately. Press **ESC** to stop.

Output is saved to `keylog.txt` in the current directory.

## How It Works

The script uses the `pynput` library to listen for keyboard events:
- `on_press()`: Called when a key is pressed
- `on_release()`: Called when a key is released (stops on ESC)
- Each keystroke is appended to `keylog.txt`

## Example Output

```
hello[shift]world[enter]this[space]is[space]a[space]test[esc]
```

## Important Notes

1. **Requires GUI Environment**: This script needs a graphical environment and will not work in headless/terminal-only environments
2. **Administrative Privileges**: May require elevated privileges on some systems
3. **Educational Only**: This is a learning tool to understand input monitoring, not for malicious use

## Platform Notes

- **Linux**: Requires X server running
- **macOS**: May require accessibility permissions
- **Windows**: Should work without special permissions

## Learning Concepts

This project demonstrates:
- Keyboard event handling
- File I/O operations
- Python libraries for system monitoring
- Event listener patterns

## License

MIT License - For educational purposes only.
