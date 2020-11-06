# Your code here


def expensive_seq(x, y, z):
    # Your code here
   expens(x,y,z) = 0

    if x <= 0:
        y + z
    elif x > 0:
        expens(x - 1, y + 1, z) + expens(x - 2, y + 2, z * 2) + expens(x - 3, y + 3, z * 3)

    return expensive_seq(x,y,z)

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
