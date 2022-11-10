import sys
from train import train
from process_emotion import process_emotion
import os

def main():
    mode = True
    list = sys.argv
    for arg in list[1:]:
        if arg == "--train":
            mode = False
    if mode == False:
        return train()
    if not os.path.exists(list[1]):
        return print('File not found.')
    return print(process_emotion(list[1]))

main()