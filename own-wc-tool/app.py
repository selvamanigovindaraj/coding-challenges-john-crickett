#!/usr/bin/env python3
print("Running custom command!")

def numberOfBytes(content):
    print('Byte Count: ',len(content))

def numberOflines(content):
    text = content.decode('utf-8')
    print( 'Line Count: ' ,len(text.split('\n')))

def numberOfWords(content):
    print('Word Count: ', len(content.decode('utf-8').split()))


def numberOfChar(content):
    print('Char Count: ',len(content.decode('utf-8')))


if __name__ == "__main__":
    with open ("test.txt", "rb") as file:
        content = file.read()
        numberOfBytes(content)
        numberOflines(content)
        numberOfWords(content)
        numberOfChar(content)