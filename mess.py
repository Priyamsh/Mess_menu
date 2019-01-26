
filename = r'C:\Users\shahp\Downloads\16JANTO31JAN  NEW MENU.csv'

fw = open(filename, 'r')
var = fw.readlines()
word = ",".join(var)
cut = word.split(",")
counter = 0
array2 = cut[::17]
while -1:
    if input("Type 'run' to start and 'stop' to terminate: ") == str("run"):
        date = input("Enter the date(dd-Mon-yy): ")
        while counter < 18:
            if date == str(cut[counter+1]):
                array = cut[int(cut.index(date))::17]
                time = input("BreakFast=0/Lunch=1/Dinner=2: ")
                if int(time) == 0:
                    print("Breakfast" + '\t\t\t\t\t\t\t' + "Items")
                    for items, things in zip(array2[0:12], array[int(time):int(time) + 12]):
                        print('{:<20s}{:>20s}'.format(items, things))
                        print('\n')
                    break
                elif int(time) == 1:
                    print("Lunch" + '\t\t\t\t\t\t\t\t' + "Items")
                    for items, things in zip(array2[12:21], array[int(time) + 11:int(time) + 19]):
                        print('{:<20s}{:>20s}'.format(items, things))
                        print('\n')
                    break
                elif int(time) == 2:
                    print("Dinner" + '\t\t\t\t\t\t\t\t' + "Items")
                    for items, things in zip(array2[21:], array[int(time) + 19:int(time) + 28]):
                        print('{:<20s}{:>20s}'.format(items, things))
                        print('\n')
                    break
                else:
                    print('Enter a valid number')
                    break
            else:
                counter += 1
                if counter == 18:
                    counter -= 18
    else:
        break


