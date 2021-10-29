# -*- coding: utf-8 -*-
# !/usr/bin/env python3

__author__ = "Vicentini Tommaso"
__version__ = "01.01"


import os


def main():
    """
    main
    :return: none
    """
    directory = ".\\"
    audio_format = ["mp3", "wav", "m4a"]
    
    for root, dirs, files in os.walk(directory):
        for i in files:
            if i != __file__:
                try:
                    v_file = i.split(".")
                    try:
                        if v_file[-1] in audio_format:
                            name_song = v_file[0].split(" - ")
                            st = name_song[1]
                            for h in name_song[2:]:
                                st = st + " - " + h
                            print(st)
                            os.rename(os.path.join(root, i), os.path.join(root, v_file[0].replace(v_file[0], st) + "." + v_file[-1]))

                    except OSError:
                        reserved_names = "CON PRN AUX NUL COM1 COM2 COM3 COM4 COM5 COM6 COM7 COM8 COM9 " \
                                        "LPT1 LPT2 LPT3 LPT4 LPT5 LPT6 LPT7 LPT8 LPT9"
                        reserved_characters = '\\ / : * ? " < > |'
                        print("there are invalid characters[" + reserved_characters + "  " + reserved_names + "]")
                        pass
                except IndexError:
                    pass
    exit()


if __name__ == "__main__":
    main()
