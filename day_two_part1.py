def input_num(s,index): # finds the number in question in string, converts to int and returns it
    try:
        if s[index].isnumeric() and s[index+1].isnumeric():
            if s[index].isnumeric() and s[index+1].isnumeric() and s[index+2].isnumeric():
                return int(s[index:index+3])
            return int(s[index:index+2])
    except EOFError or IndexError:
        return int(s[index])
    return int(s[index])

#constants as provided in the question statement
RED = 12
BLUE = 14
GREEN = 13

def cube_conundrum():
    res = 0

    while True:
        ok = True
        try:
            #inputting line by line
            record = input()

            #find and store id
            game_id = int(input_num(record,5))
            record = record[record.index(":")+1:]
            arr = record.split(sep = " ")
            for index in range(len(arr)-1):
                
                # cleaning strings before converting/comparing
                arr[index] = arr[index].strip(",;")
                arr[index+1] = arr[index+1].strip(",;")
                
                if arr[index].isnumeric():

                    # checks
                    if arr[index+1] == "blue" and int(arr[index]) > BLUE:
                        ok = False
                    if arr[index+1] == "red" and int(arr[index]) > RED:
                        ok = False
                    if arr[index+1] == "green" and int(arr[index]) > GREEN:
                        ok = False
        except EOFError:
            break
        if ok:
            res += game_id
    print(res)
if __name__ == "__main__":
    cube_conundrum()