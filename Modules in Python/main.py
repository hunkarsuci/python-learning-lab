from utility import multiply, divide # import the functions
from shopping.shopping_more import shopping_cart # package name then the module name we can add

print(shopping_cart.buy('apple'))
print(divide(5,3))
print(multiply(2,3))
print(max([1,2,3]))

print(__name__) # specificly given the file that we run
if __name__ == '__main__': # dunders
    print('please run this')