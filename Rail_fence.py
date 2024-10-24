class rail_fence:

    def __init__(self,matn,kalit,flag:bool):

        self.natija_ = ""

        if(flag == True):
            rail = [['\n' for _ in range(len(matn))] for _ in range(kalit)]

            # Fill the rail matrix in a zigzag pattern
            direction_down = False
            row, col = 0, 0

            for char in matn:
                if row == 0 or row == kalit - 1:
                    direction_down = not direction_down

                rail[row][col] = char
                col += 1

                if direction_down:
                    row += 1
                else:
                    row -= 1

            # Construct the cipher text by reading the rail matrix
            cipher_text = []
            for i in range(kalit):
                for j in range(len(matn)):
                    if rail[i][j] != '\n':
                        cipher_text.append(rail[i][j])

            self.natija_ = ''.join(cipher_text)
        elif (flag == False):

            rail = [['\n' for _ in range(len(matn))] for _ in range(kalit)]

            # Determine the positions in the zigzag pattern
            direction_down = None
            row, col = 0, 0

            for i in range(len(matn)):
                if row == 0:
                    direction_down = True
                if row == kalit - 1:
                    direction_down = False

                rail[row][col] = '*'
                col += 1

                if direction_down:
                    row += 1
                else:
                    row -= 1

            # Fill the rail matrix with the cipher text
            index = 0
            for i in range(kalit):
                for j in range(len(matn)):
                    if rail[i][j] == '*' and index < len(matn):
                        rail[i][j] = matn[index]
                        index += 1

            # Construct the original text by reading the rail matrix in a zigzag pattern
            result = []
            row, col = 0, 0
            for i in range(len(matn)):
                if row == 0:
                    direction_down = True
                if row == kalit - 1:
                    direction_down = False

                if rail[row][col] != '*':
                    result.append(rail[row][col])
                    col += 1

                if direction_down:
                    row += 1
                else:
                    row -= 1
            self.natija_ = ''.join(result)

    def natija(self):

        return self.natija_


'''def rail_fence_decrypt(cipher_text, key):
    # Create a 2D array to represent the rails
    rail = [['\n' for _ in range(len(cipher_text))] for _ in range(key)]

    # Determine the positions in the zigzag pattern
    direction_down = None
    row, col = 0, 0

    for i in range(len(cipher_text)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    # Fill the rail matrix with the cipher text
    index = 0
    for i in range(key):
        for j in range(len(cipher_text)):
            if rail[i][j] == '*' and index < len(cipher_text):
                rail[i][j] = cipher_text[index]
                index += 1

    # Construct the original text by reading the rail matrix in a zigzag pattern
    result = []
    row, col = 0, 0
    for i in range(len(cipher_text)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    return ''.join(result)


# Misol uchun foydalanish:
encrypted_text = "smmaohmaalag"
key = 3
decrypted_text = rail_fence_decrypt(encrypted_text, key)
print("Deshifrlangan matn:", decrypted_text)'''
