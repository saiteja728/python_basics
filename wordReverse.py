class WordReverse:
    def revfun(self,quote):
        words = quote.split()[::-1]
        l =[]
        for iterator in words:
            l.append(iterator)
        return " ".join(l)

quote1 = input("enter  todays quotation:")
obj = WordReverse()
result = obj.revfun(quote1)
print(result[::-1])
