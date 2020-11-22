import pypinyin


# 不带声调的(style=pypinyin.NORMAL)
def pinyin(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s


if __name__ == "__main__":
    for word in open("name.txt"):
        print(pinyin(word),end='')

