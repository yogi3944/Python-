# 1.	Write a Python Program to Find the Factorial of a Number?

import logging

logging.basicConfig(filename="programming_Assignment_4.log", level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
factorial = 1
while True:
    try:
        num = int(input("Enter number for which find the Factorial: "))
        logging.info("entered number successfully: %s",num)
        break
    except Exception as e:
        logging.error("Error has happened")
        print("Please input number only", e)

        continue
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")

elif num == 0:
    print ("factorial of 0 is 1")

else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("factorial of {} is {}".format(num,factorial))
    logging.info("factorial of %s is : %s", num,factorial)
