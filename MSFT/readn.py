'''
Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.
For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
'''


class FileRead:
    def __init__(self, str):
        self.str = str
        self.offset = 0
        self.buffer = ""

    def read7(self):
        start = self.offset
        end = min(self.offset + 7, len(self.str))
        self.offset = end
        return self.str[start : end].strip()


    def readn(self, n):
        while len(self.buffer) < n:
            add_char = self.read7()
            if not (add_char):
                break
            self.buffer += add_char

        nchars = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return nchars.strip()

str = FileRead("Hello World")
#print(str.read7())
print(str.readn(4))
print(str.readn(4))
print(str.readn(4))



