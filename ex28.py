print "01. Should be True  =>",  True and True
print "02. Should be False =>", False and True
print "03. Should be False =>", 1 == 1 and 2 == 1
print "04. Should be True  =>", "test" == "test"
print "05. Should be True  =>", 1 == 1 or 2 != 1 
print "06. Should be True  =>", True and 1 == 1
print "07. Should be False =>", False and 0 != 0
print "08. Should be True  =>", True or 1 == 1
print "09. Should be False =>", "test" == "testing"
print "10. Should be False =>", 1 != 0 and 2 == 1
print "11. Should be True  =>", "test" != "testing"
print "12. Should be False =>", "test" == 1
print "13. Should be True  =>", not (True and False)
print "14. Should be False =>", not (1 == 1 and 0 != 1)
print "15. Should be False =>", not (10 == 1 or 1000 == 1000)
print "16. Should be False =>", not (1 != 10 or 3 == 4)
print "17. Should be True  =>", not ("testing" == "testing" and "Zed" == "Cool Guy")
print "18. Should be True  =>", 1 == 1 and (not ("testing" == 1 or 1 == 0))
print "19. Should be False =>", "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
print "20. Should be False =>", 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))

