emoji = input()

l = len(emoji)
c = emoji.count(':')
u = emoji.count('_')

print(l + c + u * 5)
