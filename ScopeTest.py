class ScopeTest:
    _name="sai"
    _age=34
    _number=5555555

    def _f1(self):
        return self._age
    def f2(self):
        # obj._age=55
        # print(obj._f1())
        return self._name
class Chaild(ScopeTest):
        def _f3(self):
            # obj.f2()
            return self._age

        def _f1(self):
            return self._age
        def f4(self):
            # obj.f2()
           # return self._f1()
            pass

obj2=Chaild()

print(obj2.f2())
print(obj2.f4())

