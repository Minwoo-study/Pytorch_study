PI =3.141592

class Math :
    def solv(self, r) :
        print("클래스 안의 함수")
        return PI * (r**2)
    
def add(a, b) :
    print('클래스 밖의 함수')
    return a +b