#Single-line version:
with open('source.txt') as src, open('dest1.txt', 'w') as dst1, open('dest2.txt', 'w') as dst2:
    data = src.read()
    dst1.write(data)
    dst2.write(data)

#Nested version:
with open('source.txt') as src:
    with open('dest1.txt', 'w') as dst1:
        with open('dest2.txt', 'w') as dst2:
            data = src.read()
            dst1.write(data)
            dst2.write(data)