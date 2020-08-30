

import random,string
num = string.ascii_letters + string.digits
str = "".join(random.sample(num, 20))
print(str)
