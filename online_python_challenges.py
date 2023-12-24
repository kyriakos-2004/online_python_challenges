#def capital_indexes(words):
#    arr = []
#    for x in words:
#       if x.isupper():
#            arr.append(words.index(x))
#    return arr

#words = input("Enter string with capital letters: ")

#print(capital_indexes(words))

#===========================================================================

#def mid(words):
#    if (len(words)%2 == 0):
#        return '""'
#    else:
#        return words[int((len(words)/2))]

#print(mid("dfreg"))

#===========================================================================

#def online_count(statuses):
#    count = 0
#    for x in statuses.values():
#        if x == "online":
#            count+=1
#    return count

#statuse = {
#    "Alice": "online",
#    "Bob": "offline",
#    "Eve": "online",
#}

#print(online_count(statuse))

#===========================================================================

#import random

#def random_number():
#    return random.randint(1,100)

#print(random_number())
#print("\n")
#print(random_number())
#print("\n")
#print(random_number())

#===========================================================================

#def only_ints(a,b):
#    try:
#        for i in a:
#            return False
#    except:
#        try:
#            for i in b:
#                return False
#        except:
#            return True

#print(only_ints("a",2))

#===========================================================================

#def double_letters(words):
#    for i in range(0,len(words)-1):
#        if words[i] == words[i+1]:
#            return True
#    return False

#print(double_letters("hello"))

#===========================================================================

#def add_dots(words):
#    subword = []
#    for i in range(0,len(words)):
#        subword.append(words[i])
#        if (i != len(words)-1):
#            subword.append('.')
#    return ''.join(subword)

#def remove_dots(string_with_dot):
#    subword = []
#    for i in string_with_dot:
#        if i != '.':
#            subword.append(i)
#    return ''.join(subword)

#print(remove_dots(add_dots("test")))

#===========================================================================

#def count(words):
#    hyphens = 0;
#    for i in words:
#        if i == '-':
#            hyphens += 1
#    return hyphens + 1

#print(count("ter-min-a-tor"))

#===========================================================================

#def is_anagram(words1,words2):
#    sortedw1 = ''.join(sorted(words1))
#    sortedw2 = ''.join(sorted(words2))

#    if sortedw1 == sortedw2:
#        return True
#    else:
#        return False


#print(is_anagram("typhoon", "opyhon"))

#===========================================================================

#def flatten(l1):
#    subn = []
#    for i in l1:
#        for j in i:
#            subn.append(j)
#    return subn

#print(flatten([[1, 2], [3, 4]]))

#===========================================================================

#def largest_difference(li):
#    big = max(li)
#    small = min(li)
#    return big-abs(small)

#print(largest_difference([1, 2, 45,78,-30]))

#===========================================================================

#def div_3(num):
#    if (num % 3 == 0):
#        return True
#    else:
#        return False

#print(div_3(7))

#===========================================================================

#def get_row_col(coor):
#    li = []
#    if coor[1] == '3':
#       li.append(2)
#    elif coor[1] == '2':
#       li.append(1)
#    elif coor[1] == '1':
#        li.append(0)

#    if coor[0] == 'A':
#       li.append(0)
#    elif coor[0] == 'B':
#       li.append(1)
#    elif coor[0] == 'C':
#       li.append(2)

#    return tuple(li)   

#print(get_row_col("C1"))

#===========================================================================

#def palindrome(words):
#    lbw = []
#    index = len(words)-1
#    for i in words:
#        lbw.append(words[index])
#        index-=1
#    if ''.join(lbw) == words:
#        return True
#    else:
#        return False

#print(palindrome("aba"))

#===========================================================================

#def up_down(num):
#    l = []
#    l.append(num - 1)
#    l.append(num + 1)

#    return tuple(l)

#print(up_down(5))

#===========================================================================

#def consecutive_zeros(words):
#    countz = 0
#    countmaxz = 0
#    for i in words:
#        if (i == '0'):
#            countz += 1
#        else:
#            if (countz > countmaxz):
#                countmaxz = countz
#            countz = 0
    
#    if (countz > countmaxz):
#                countmaxz = countz
    
#    return countmaxz

#print(consecutive_zeros("10"))

#===========================================================================

#def all_equal(li):
#    l2 = sorted(li)
#    if l2[0] == l2[-1]:
#        return True
#    return False

#print(all_equal([1, 1, 1]))

#===========================================================================

#def triple_end(p1, p2, p3):
#    if (p1 and p2 and p3):
#        return True
#    return False

#print(triple_end(True,False,True))

#===========================================================================

#def convert(li):
#    return list(map(str, li))

#print(convert([1, 2, 3]))

#===========================================================================

#def zap(a, b):
#    big_list = []
#    temp_list = []
#    for i in range(0, len(a)):
#        temp_list.append(a[i])
#        temp_list.append(b[i])
#        big_list.append(tuple(temp_list))
#        temp_list.clear()
    
#    return big_list

#print(zap(
#    [0, 1, 2, 3],
#    [5, 6, 7, 8]
#))

#===========================================================================

#def validate(code):
#    if "def" not in code:
#        return "missing def"

#    if ":" not in code:
#        return "missing :"

#    if ("(" and ")") not in code:
#        return "missing paren"

#    if "    " not in code:
#        return "missing indent"

#    if "validate" not in code:
#        return "wrong name"

#    if "return" not in code:
#        return "missing return"

#    return True

#print(validate('(code):     if "def" not in code:         return "missing def"      if ":" not in code:         return "missing :"      if ("(" and ")") not in code:         return "missing paren"      if "    " not in code:         return "missing indent"      if "valida" not in code:         return "wrong name"      if "return" not in code:         return "missing return"      return True  print(validte())'))

#===========================================================================

#def list_xor(n, list1, list2):
#    return bool((n in list1 and n not in list2) or (n in list2 and n not in list1))

#print(list_xor(1, [1, 2, 3], [4, 1, 6]))

#===========================================================================

#def param_count(*args):
#    return len(args)

#print(param_count())

#===========================================================================

def format_number(n1):
    if len(str(n1)) < 4:
        return str(n1)
    else:
        l1 = []
        pos = 0
        index = len(str(n1))-1
        for i in range(0,len(str(n1))):
            l1.append(str(n1)[index])
            pos+=1
            if pos % 3 == 0:
                l1.append(',')
            index -= 1
        l1.reverse()
        return ''.join(l1)

print(format_number(1234567))
            
