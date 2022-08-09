from classStudent import *


def addStudent():
    try:
        fullName = input("Enter the fullname: ")
        while True:
            sex = input("Enter the sex [Male/Female]: ")
            if sex in ["Male", "Female"]:
                break
            else:
                print("We only accpet Male or Female")
        className = input("Enter the classname: ")
        point = int(input("Enter the point: "))
        file = open("dataBase.txt", "a", encoding="utf-8")
        data = classStudent(fullName, sex, className, point)
        file.writelines(data.__str__() + "\n")
        file.close()
        print("Saved your data")
    except:
        print("Sorry!!")


def isExist(fullName):
    file = open("dataBase.txt", "r", encoding="utf-8")
    for row in file:
        if row.split(";")[0] == fullName:
            file.close()
            return True
    file.close()
    return False


def removeStudent():
    fullName = input("Enter full name remove: ")
    if not isExist(fullName):
        print(fullName + " is not exist")
        return
    data = []
    try:
        file = open("dataBase.txt", "r", encoding="utf-8")
        data = map(lambda item: item.split(";"), file)
    except:
        print("Error when read file")
        return
    newData = list(filter(lambda item: item[0] != fullName, data))
    file = open("dataBase.txt", "w", encoding="utf-8")
    for row in newData:
        file.writelines(";".join(row))
    file.close()
    print("Delete student whose name is: " +fullName)


def findStudent():
    fullName = input("Enter the full name find: ")
    if not isExist(fullName):
        print(fullName + " is not exist")
        return
    data = []
    try:
        file = open("dataBase.txt", "r", encoding="utf-8")
        data = map(lambda item: item.split(";"), file.read())
    except:
        print("Error when read file")
        return
    newData = list(filter(lambda item: item[0] != fullName, data))
    file = open("dataBase.txt", "w", encoding="utf-8")
    for row in newData:
        file.writelines(";".join(row))
    file.close()
    print("Find student whose name is: " +fullName)


def updataStudent():
    fullName = input("Enter the full name update: ")
    if not isExist(fullName):
        print(fullName + " is not exist")
        return
    print("Please enter information updat ")
    while True:
        sex = input("[Male/Female]: ")
        if sex in ["Male", "Female"]:
            break
        else:
            print("We only accept [Male/Female]")
    className = input("Enter the class name: ")
    point = str(input("Enter the point: "))
    data = []
    try:
        file = open("dataBase.txt", "r", encoding="utf-8")
        data = list(map(lambda item: item.split(";"), file))
    except:
        print("Error when read file")
        return
    for i in range(len(data)):
        if data[i][0] == fullName:
            data[i][1] = sex if sex != "." else data[i][1]
            data[i][2] = className if className != "." else data[i][2]
            data[i][3] = point if point != "." else data[i][3]
    file = open("dataBase.txt", "w", encoding="utf-8")
    for row in data:
        file.writelines(";".join(row))
    file.close()
    print("Update student whose name: " +fullName)

def viewStudent():
    try:
        file = open("dataBase.txt", "r", encoding="utf-8")
        print("| {} | {} | {} | {} | " .format("fullName".center(20), "Sex".center(10), "className".center(10), "Point".center(10)))
        print(" ".center(70, "*"))
        for row in file:
            data = row.split(";")
            data[3] = int(data[3])
            sv = classStudent(*data)
            sv.showInfo()
        file.close()
    except:
        print("Error when read data.")

    
