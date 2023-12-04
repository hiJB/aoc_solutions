def input_num(s,index): # finds the number in question in string, converts to int and returns it
    try:
        if s[index].isnumeric() and s[index+1].isnumeric():
            if s[index].isnumeric() and s[index+1].isnumeric() and s[index+2].isnumeric():
                return int(s[index:index+3])
            return int(s[index:index+2])
    except EOFError or IndexError:
        return int(s[index])
    return int(s[index])

def lowest_cubes():
    res = 0
    while True:
        try:
            #inputting line by line
            record = input()
            
            #find and store id (not needed for this part)
            game_id = int(input_num(record,5))
            record = record[record.index(":")+1:]
            arr = record.split(sep = " ")

            #initialize all color values to zero
            red = 0
            blue = 0
            green = 0
            for index in range(len(arr)-1):
                
                # cleaning strings before converting/comparing
                arr[index] = arr[index].strip(",;")
                arr[index+1] = arr[index+1].strip(",;")
                
                if arr[index].isnumeric():
                    # finding maximum value of corresponding color
                    if arr[index+1] == "blue":
                        blue = max(blue,int(arr[index]))
                    if arr[index+1] == "red":
                        red = max(red,int(arr[index]))
                    if arr[index+1] == "green":
                        green = max(green,int(arr[index]))
        
        except EOFError:
            break

        #adding the product of the colors
        res += (red*blue*green)
    print(res)
if __name__ == "__main__":
    lowest_cubes()