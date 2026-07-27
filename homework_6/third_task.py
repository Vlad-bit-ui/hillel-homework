words = ["Maths", "Physics", "Electron", "Flask", "JS", "App"]

for word in words:
    if (length := len(word)) > 4:
        print(f"{word}: {length}")