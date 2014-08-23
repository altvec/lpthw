frmt1 = "%r"
frmt2 = "%s"

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\n\ton a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t\v* Cat food
\t\v* Fishies
\t\v* Catnip\n\t\v* Grass
"""

print frmt1 % tabby_cat
print frmt2 % persian_cat
print backslash_cat
print frmt2 % fat_cat