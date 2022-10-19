import pyautogui
import time


print("\n---------------------------------Warning------------------------------------\n\n")

print("before entering the value plzz first open whatsapp web then after entering value click on chat box where you want to bombing")

print("\n\tIt WORK IN 5 second AFTER CLICKING ON CHATBOX\n\n ")

msg=input("\n\nEnter massege here :- ")

repeat=int(input("\n\nhow many time you want to repeat it:- "))
print("\nnow open whatsapp web ")
time.sleep(5)
count=0
while count<=repeat:
    pyautogui.typewrite(msg+" "+str(count))
    pyautogui.press("enter")
    count=count+1
