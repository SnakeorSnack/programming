# generate password

import random

lower_case = "abcdefghijklmnoprqstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPRQSTUVWXYZ"
numbers = "1234567890"
symbols = "!№;%:?*()<"

use_for = lower_case + upper_case + numbers + symbols
length_for_pass = 12

password = "".join(random.sample(use_for, length_for_pass))


print("Your generated password:", password)
