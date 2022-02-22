import standard_lib
from aufgaben import *

if __name__ == "__main__":
    print("UE_7")

    print("\ncube")
    cube = Cube(5)
    print(cube.volume())
    print(cube.surface())

    print("\nsphere")
    sphere = Sphere(4)
    print(sphere.volume())
    print(sphere.surface())

    print("\n Banking")
    account = Account(1000, 1234)
    account.pay_in(100)
    account.withdraw(1000)
    account.withdraw(1000)








