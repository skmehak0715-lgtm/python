class pairofelements:

    def twosum(self,nums,target):
        sum = 0
        Lookup = {}
        for i,num in enumerate(nums):
            sum = sum + num
            if sum >= target:
              print("the index value is",i)
              Lookup[i] = sum
              print(Lookup)
              return
        Lookup[i] = sum

p1 = pairofelements()
p1.twosum((10,20,20,30,40,100),70)