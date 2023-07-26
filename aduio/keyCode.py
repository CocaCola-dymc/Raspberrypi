import keyboard

def on_key_press(event):
    print('press ok')

keyboard.add_hotkey('a',on_key_press)
keyboard.wait()

