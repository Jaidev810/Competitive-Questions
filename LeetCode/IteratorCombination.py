class CombinationIterator:

    def __init__(self, character, combinationLength):
        self.character = character
        self.combinationLength = combinationLength
        self.pq = []
        self.helper()

    def factorial(self, number):
        i = 1
        fact = 1
        while i <= number:
            fact = fact*i
            i += 1
        return fact


    def combination(self):
        total = len(self.character)
        com = self.combinationLength

        combination = self.factorial(total)//self.factorial(com)*self.factorial((total-com))
        return combination

    def helper(self):

        for i in range(0, len(self.character)):
            if self.combinationLength > 1:
                temp = self.character[i]
                for j in range(i+1, len()):
                    temp = temp + self.character[j]
                    self.pq.append(temp)
            else:
                self.pq.append(self.character[i])
            

    def next(self):
        return self.pq.pop(0)

    def hasnext(self):
        if len(self.pq) == 0:
            return False
        else:
            return True


obj = CombinationIterator("abc", 2)
print(obj.next())
print(obj.hasnext())
print(obj.next())
print(obj.hasnext())
print(obj.next())
print(obj.hasnext())