import random

lower_case="abcdefghijklmnopqrstuvwxyz"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="1234567890"
symbols="!.@#$%^&*()"

Use_for = lower_case + upper_case + number + symbols
password_length = 8

password = "".join(random.sample(Use_for, password_length))

print("Your Generated Password is:", password)



