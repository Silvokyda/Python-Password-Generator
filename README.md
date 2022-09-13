# Python-Password-Generator

``` command line
1. import random
2. import logging
3. 
4. lower_case="abcdefghijklmnopqrstuvwxyz"
5. upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
6. number="1234567890"
7. symbols="!.@#$%^&*()"
8.
9. Use_for = lower_case + upper_case + number + symbols
10.password_length = 8
11.
12.password = "".join(random.sample(Use_for, password_length))
13.
14.print("Your Generated Password is:", password)
```
