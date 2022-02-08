def factorial(d_58):
   if(d_58==1 or d_58==0):
      return 1
   return d_58*factorial(d_58-1)
def isStrong(n_58):
   num_58=n_58
   sum_58=0
   while(n_58>0):
      digit_58=n_58%10
      sum_58=sum_58+factorial(digit_58)
      n_58=n_58//10
   print("\n Sum of Factorials of a Given Number %d = %d" %(num_58, sum_58))   
   if(sum_58==num_58):
      print(" The given number is a Strong Number")
   else:
      print(" The given number is not a Strong Number")

a_58=int(input("Input a number :"))
isStrong(a_58)
