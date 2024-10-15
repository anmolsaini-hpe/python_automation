# x = 13
# if (x>=13):
    # print("Met the condition")
# else:
    # print("Didn't met the condition")


# print("Zero:",bool(0))
# print("Integer:",bool(23))
# print("Float:",bool(3.142))
# print("Complex:",bool(5+2j))

##############################################################################################################################

#1
Tool = "SONAR"
len1 = len(Tool)
print(len1)
print("Code analysis tool is", Tool, ".Its part of devops")

#2
IAAS = "TERRAFORM"
print(IAAS[:5])      #Slicing from Start
print(IAAS[5:])      #Slicing till End
print(IAAS[2:6])     #Slicing in between

#3
Name = "AMAZON WEB SERVICES"
for i in Name:
    print(i)
