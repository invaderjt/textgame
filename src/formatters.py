from constants import *



def center_text(text: str, width: int = L_WIDTH) -> str:
    space_needed = width - len(text)
    left_gap = space_needed//2
    right_gap = space_needed - left_gap
    left_spacer = " " * (left_gap)
    right_spacer = " " * (right_gap)
    return left_spacer + text + right_spacer
    
def center_in_box(text: str, width: int = L_WIDTH) -> None:
    text_space = (9 * width)//10
    lines = []
    line = ""
    words = text.split(" ")
    while len(words) > 0:
        if len(line + " " + words[0]) <= (text_space) and words[0] != "\n":
            line = " ".join([line, words.pop(0)])
        else:
            if words[0] == "\n":
                words.pop(0)
            lines.append(line)
            line = ""   
    if line:
        lines.append(line)
    for line in lines:
        space_needed = width - len(line)
        left_gap = space_needed//2
        right_gap = space_needed - left_gap
        left_spacer = "|" + " " * (left_gap - 1)
        right_spacer = " " * (right_gap - 1) + "|"
        print(left_spacer + line + right_spacer)



def separator(option: str, length: int = L_WIDTH) -> None:
    print(option * length)



def text_box(text: str, width: int = L_WIDTH) -> None:
    print("_" * width)
    print("|" + (" " * (width - 2)) + "|")
    center_in_box(text, width)
    print("|" + ("_" * (width - 2)) + "|")