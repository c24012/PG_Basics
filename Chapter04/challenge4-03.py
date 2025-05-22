def f(j,k,l,x = 12.3,y = 4.56):
    """
    ３つの必須引数と２つのオプション引数を
    すべて加算して返す関数
    
    引数:
        j,k,l : int -必須 
        x,y : float -オプション

    戻り値:
        result
    """

    result = j+k+l+x+y
    return result

print(f(1,2,3,4.2))
