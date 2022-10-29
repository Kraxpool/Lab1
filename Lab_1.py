def print_rec(n, k):
    for i in range(0, n):
        for j in range(0, k):
            print("*", end=" ")
        print()
    print()


def lab_1() :
    try:
        print_rec(3, 4)
    except Exception as ex:
        print('Eror information {ex}')

lab_1()