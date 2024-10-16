def read_from_file(filename):
    error=0
    with open(filename,"r") as file:
        for line in file:
            if "ERROR" in line:
                error+=1
    print("Total error in file", error)