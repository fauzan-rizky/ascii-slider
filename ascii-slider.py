"""
Ascii Slider     
"""

N = ["███    ██ ",
     "████   ██ ",
     "██ ██  ██ ",
     "██  ██ ██ ",
     "██   ████ "]



O = [" ██████  ",
     "██    ██ ",
     "██    ██ ",
     "██    ██ ",
     " ██████  "]



P = ["██████  ",
     "██   ██ ",
     "██████  ",
     "██      ",
     "██      "]



Q = [" ██████  ",
     "██    ██ ",
     "██    ██ ",
     "██ ▄▄ ██ ",
     " ██████  "]

R = ["██████  ",
     "██   ██ ",
     "██████  ",
     "██   ██ ",
     "██   ██ "]



S = ["███████ ",
     "██      ",
     "███████ ",
     "     ██ ",
     "███████ "]



T = ["████████ ",
     "   ██    ",
     "   ██    ",
     "   ██    ",
     "   ██    "]



U = ["██    ██ ",
     "██    ██ ",
     "██    ██ ",
     "██    ██ ",
     " ██████  "]



V = ["██    ██ ",
     "██    ██ ",
     "██    ██ ",
     " ██  ██  ",
     "  ████   "]

W = ["██     ██ ",
     "██     ██ ",
     "██  █  ██ ",
     "██ ███ ██ ",
     " ███ ███  "]



X = ["██   ██ ",
     " ██ ██  ",
     "  ███   ",
     " ██ ██  ",
     "██   ██ "]



Y = ["██    ██ ",
     " ██  ██  ",
     "  ████   ",
     "   ██    ",
     "   ██    "]



Z = ["███████ ",
     "   ███  ",
     "  ███   ",
     " ███    ",
     "███████ "]




M = ["███    ███ ",
     "████  ████ ",
     "██ ████ ██ ",
     "██  ██  ██ ",
     "██      ██ "]

L = ["██      ",
     "██      ",
     "██      ",
     "██      ",
     "███████ "]

K = ["██   ██ ",
     "██  ██  ",
     "█████   ",
     "██  ██  ",
     "██   ██ "]

J = ["     ██ ",
     "     ██ ",
     "     ██ ",
     "██   ██ ",
     " █████  "]

I = ["██ ",
     "██ ",
     "██ ",
     "██ ",
     "██ "]

H = ["██   ██ ",
     "██   ██ ",
     "███████ ",
     "██   ██ ",
     "██   ██ "]

G = [" ██████  ",
     "██       ",
     "██   ███ ",
     "██    ██ ",
     " ██████  "]

F = ["███████ ",
     "██      ",
     "█████   ",
     "██      ",
     "██      "]

E = ["███████ ",
     "██      ",
     "█████   ",
     "██      ",
     "███████ "]

D = ["██████  ",
     "██   ██ ",
     "██   ██ ",
     "██   ██ ",
     "██████  "]

A = [" █████  ",
     "██   ██ ",
     "███████ ",
     "██   ██ ",
     "██   ██ "]

B = ["██████  ",
     "██   ██ ",
     "██████  ",
     "██   ██ ",
     "██████  "]

C = [" ██████ ",
     "██      ",
     "██      ",
     "██      ",
     " ██████ "]

space = ["         ",
         "         ",
         "         ",
         "         ",
         "         "]

alphabet = {

    'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J,

    'K': K, 'L': L, 'M': M, 'N': N, 'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 'T': T,

    'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z, ' ': space

}
import os
import time

font_height = 6
term_width = os.get_terminal_size()
term_columns = term_width.columns

text = input("Enter text to display:")
text = text.upper()

charlist = []
for ch in text:
    try:
        charlist.append(alphabet[ch])
    except:
        charlist.append(alphabet[' '])

buffer = []
# for i in range(font_height):
#     buffer.append([])
#     for j in range(len(text)):
#         try:
#             buffer[i].append(charlist[j][i])
#         except:
#             buffer[i].append("        ")

#     print(*buffer[i], sep="")

def print_buffer():
    for lines in range(font_height):
        print(*buffer[lines], sep="")

for i in range(font_height):
    buffer.append([])
    for j in range(len(text)):
        try:
            buffer[i].append(charlist[j][i])
        except:
            buffer[i].append("        ")

for i in range(len(buffer)):
    buffer[i] = " "*term_columns + "".join(buffer[i]) + " "*20

print(len(buffer[0]))
for frames in range(len(buffer[0])):
    for lines in range(font_height):
            print(*buffer[lines][frames:term_columns+frames], sep="")
    time.sleep(0.005)
    os.system("cls")


# Alphabeticals set