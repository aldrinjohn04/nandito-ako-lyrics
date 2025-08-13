import time
import sys

def type_line_timed(text, typing_duration, after_delay):
    if len(text) == 0:
        return
    typing_speed = typing_duration / len(text)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(typing_speed)
    print()
    time.sleep(after_delay)

nandito_ako_lyrics = [
    ("nandito ako", 2, 1.3),
    ("umiibig sayo", 2, 1.5),
    ("kahit na nag durugo ang puso", 4, 2.5),
    ("at kung sakaling", 3, 1),
    ("iwanan ka niya", 1.8, 2),
    ("wag kang mag alala", 2, 1),
    ("may nag mamahal sayo", 2, 1.5),
    ("nandito akooooo", 1.8, 1.5)
]

print("\n")
time.sleep(0.5)

for line, typing_duration, after_delay in nandito_ako_lyrics:
    type_line_timed(line, typing_duration, after_delay)
