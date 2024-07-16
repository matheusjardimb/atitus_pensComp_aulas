import time
import sys

text = "Hello, world! This is a marquee animation in Python."
width = 50
speed = 0.1

text = text.strip()
text_length = len(text)
padding = " " * width  # Add initial padding equal to width of the console
shifted_text = padding + text + padding  # Initial position of the text

while True:
    for i in range(text_length + width):  # Shift text by one character at a time
        sys.stdout.write(
            "\r" + shifted_text[i : i + width]
        )  # Print shifted portion of text
        sys.stdout.flush()  # Flush the buffer to make sure the text is immediately printed
        time.sleep(speed)  # Adjust the speed of animation by changing this value
