from enum import Enum



class Test(Enum):
   common = 'common'
   

for i in Test:
    print(i.name)