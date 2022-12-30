import utils

s = utils.sumList([5,8,2])
expected = 15

if s == expected:
    print("[-] Test OK, expected result should be %d, got %d" % (expected, s))
else:
    print("[-] Test NOT OK, expected result should be %d, got %d" % (expected, s))