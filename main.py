#Time interval 
import random
import time
x = [" ","0","1","2","3","4","5","6","7","8","9"]
def lines():
   Hold =""
   for i in range(random.randint(40,200)):
       Hold= Hold + x[random.randint(0,10)]
   return Hold
def main():
        while(True):
            print(lines())
            time.sleep(random.triangular(.033, .08))
main()