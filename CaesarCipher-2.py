# File: CaesarCipher.py
# Description of Program: Shifts the given letters a certain value fowards or backwards in the alphabet with non letters staying the same.

answer = input("Enter Caesar cipher command (encrypt/decrypt): ")
answer = answer.lower()
if answer != "encrypt" and answer != "decrypt":
    print("Unrecognized command:", answer, end = "")
elif answer == "encrypt":
    print("You've asked to encrypt.")
    shiftValue = int(input("Please enter shift value (0 .. 25): "))
    if shiftValue < 0 or shiftValue > 25:
        print("Illegal shift value:", shiftValue, end = "")
    else:
        text = input("Please enter text to encrypt: ")
        newtext = "" 
        for ch in text:
            if ord(ch) >= 65 and ord(ch) <= 90:
                W = ord(ch) - ord('A') # shifts to range [0 .. 25]
                X = (W + shiftValue) % 26 # (W + shift) modulo 26
                Y = X + ord('A') # shift back to range [65 .. 90]
                Z = chr(Y)
                newtext = newtext + Z
            if ord(ch) >= 97 and ord(ch) <= 122:
                A = ord(ch) - ord('a') # shifts to range [0 .. 25]
                B = (A + shiftValue) % 26 # (A + shift) modulo 26
                C = B + ord('a') # shift back to range [97 .. 122]
                D = chr(C)
                newtext = newtext + D
            if ord(ch) < 65 or 90 < ord(ch) < 97 or ord(ch) > 122:
                newtext = newtext + ch
        print("The encrypted text is:", newtext, end = "")
 
elif answer == "decrypt":
    print("You've asked to decrypt.")
    shiftValue = int(input("Please enter shift value (0 .. 25): "))
    if shiftValue < 0 or shiftValue > 25:
        print("Illegal shift value:", shiftValue, end = "")
    else:
        text2 = input("Please enter text to decrypt: ")
        newtext2 = ""
        for ch in text2:
            if ord(ch) >= 65 and ord(ch) <= 90:
                W = ord(ch) - ord('A') # shifts to range [0 .. 25]
                X = (W - shiftValue) % 26 # (W - shift) modulo 26
                Y = X + ord('A') # shift back to range [65 .. 90]
                Z = chr(Y)
                newtext2 = newtext2 + Z
            if ord(ch) >= 97 and ord(ch) <= 122:
                A = ord(ch) - ord('a') # shifts to range [0 .. 25]
                B = (A - shiftValue) % 26 # (A - shift) modulo 26
                C = B + ord('a') # shift back to range [97 .. 122]
                D = chr(C)
                newtext2 = newtext2 + D
            if ord(ch) < 65 or 90 < ord(ch) < 97 or ord(ch) > 122:
                newtext2 = newtext2 + ch  
        print("The decrypted text is:", newtext2, end = "")