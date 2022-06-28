from string import ascii_uppercase
from enchant import Dict

Letters = list(ascii_uppercase)

cipher = "jslnsjjw"#know the right english word whih meet it

d = Dict("en_US")

for K in range(1,26):
    PT = ""
    for ch in cipher:
        PT += Letters[(Letters.index(ch.upper())-K+26)%26]

    if d.check(PT):
        print(f"for key {K} the plain text is {PT}\n")