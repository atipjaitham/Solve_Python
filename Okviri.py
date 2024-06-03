text = input()
line = [
    "".join("\b..#.." if (i+1) %
            3 != 0 else "\b..*.." for i in range(len(text))),
    "".join("\b.#.#." if (i+1) %
            3 != 0 else "\b.*.*." for i in range(len(text))),
    "".join(f"\b#.{char}.#" if (i+1) %
            3 != 0 else f"\b*.{char}.*" for i, char in enumerate(text))
]
frame = "\n".join([line[0], line[1], line[2], line[1], line[0]])
print(frame)
