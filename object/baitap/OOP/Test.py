from School import School

if __name__ == "__main__":
        strObj = School("Tam ", 20, " tam@gmai.com")
        print(strObj.get__name() + str(strObj.get__age()) + str(strObj.get__email()))
        strObj.print()
        strObj.getPrint()