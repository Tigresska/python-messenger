mas =  [1, 2, 3, 23, 453, 6, 22, 65]

#print(mas)
#print(type(mas))
#print(max(mas))

def mymax(elements):
    if len(elements) == 0:
        return None
    else:
        m = elements[0]

        #for element in elements[1:]:
        #    #print(element, m, element > m)
        #    if element > m:
        #        m = element
        i = 1
        while i < len(elements):
            if elements[i] > m:
                m = elements[i]
            i += 1
        return m

print(mymax(mas))