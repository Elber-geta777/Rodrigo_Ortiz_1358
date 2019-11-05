def suma_lista(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        actual = lst.pop()
        return actual + suma_lista(lst)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

def main():
    lst = [3,5,2,1]
    print(suma_lista(lst))
    print(factorial(5))
main()