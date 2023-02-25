import array

def range_array(start=0, end=10, step=1):

    an_array = array.array("i", [start])

    index = start + step

    length = end

    while index <= length: #both included in array
        an_array.append(index)
        index += step

    return an_array

def reverse_array_cool(an_array):

    return print_array(an_array[::-1])

def print_array(an_array):

    output = "["

    for index in range(len(an_array)):
        
        if index == 0:
            output = output + str(an_array[index])
        else:
            output = output + ", " + str(an_array[index])

    output = output + "]"

    return output

def main():
    #print(range_array(1,10))
    array = range_array(1, 10)
    print(reverse_array_cool(array))

if __name__ == "__main__":
    main()