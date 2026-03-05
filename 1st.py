n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


n = 5
for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end="")
    for star in range(i):
        print("*", end="")
    print()


n = 5
for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()


n = 5
for i in range(n, 0, -1):
    for space in range(n - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()


n = 5

# Upper pyramid
for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()

# Lower inverted pyramid
for i in range(n - 1, 0, -1):
    for space in range(n - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()


n = 5
for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end="")
    for star in range(1, 2 * i):
        if star == 1 or star == 2 * i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()



