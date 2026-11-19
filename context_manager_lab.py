def read_first_n(path, n):
    """Return the first n characters from the file at path."""
    with open(path,"r", encoding="utf-8") as src:
        return src.read(n)


def duplicate_file(src, dst):
    """Copy all text from src into dst using a single with-statement."""
    with open(src, "r", encoding="utf-8") as s, open(dst, "w", encoding="utf-8") as d:
        data = s.read()
        d.write(data)

duplicate_file("nishani.txt","dest1.txt")
print(read_first_n("nishani.txt", 5))