class Student:
    #建構函式 設定物件初值
    def __init__(self, n, e, m):
        self.name = n
        self.eng = e
        self.math = m

    def 總分(self):
        print('-----總分機算------')
        print(self.name)
        tot = self.eng + self.math
        print(tot)
        return tot

    def __str__(self):
        s = f'{self.name} {self.eng} {self.math}'
        return s
# 主程式
#建立學生物件寫法 Studnt() ，自動呼叫 __init__()
#建立一個串列，有兩個學生物件
data = [Student('Robin', 89, 100), Student('Mary', 98, 87)]
print('-----data[1]-----')
print(data[1])
tot = data[1].總分()
print('總分 返回值', tot)