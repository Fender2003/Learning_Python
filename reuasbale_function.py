def emoji_converter(message):
    words=message.split(' ')
    emojis={
        ":)": "🙂",
        ":(": "😥"
    }
    output=''
    for i in words:
        output= output+emojis.get(i,i) + " "
    return output


message = input(">")
print(emoji_converter(message))
