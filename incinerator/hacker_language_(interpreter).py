class HackerLanguage:
    message = ''

    def write(self, text):
        self.message += text

    def read(self, text):
        decoded_message = ''
        return decoded_message

    def send(self):
        encoded_message = ''
        return encoded_message

    def delete(self, n):
        self.message = self.message[:-n]

    @staticmethod
    def encodeSymbol(ch):
        if ch == ' ':
            return '1000000'
        ascii_code = ord(ch)
        encoded_symbol = bin(ascii_code).replace("0b", "")
        return encoded_symbol

    @staticmethod
    def decodeSymbol(bin_ch):
        if bin_ch == '1000000':
            return ' '
        ascii_code = int(bin_ch, 2)
        decoded_symbol = chr(ascii_code)
        return decoded_symbol


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    print("Coding complete? Let's try tests!")
