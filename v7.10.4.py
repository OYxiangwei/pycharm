import random
import string
code = []
code.append(random.choice(string.ascii_lowercase))
code.append(random.choice(string.ascii_uppercase))
code.append(random.choice(string.digits))
if len(code) < 6:
    code.append(random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits))
    print(code)
#q_code = "".join(code)
#print(q_code)