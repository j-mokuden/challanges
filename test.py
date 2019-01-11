#def1整数を引数として受け取り、2で割った整数を出力
def f(x):
    return int(x/2)

#def2 整数に4をかけた整数を返す
def f2():
    return int(f(x)*4)

x = int(input("int: "))
print(f2())
