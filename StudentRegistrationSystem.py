import json


def Registration_status():
    print("Enter Registration Status: ")
    choice = int(input("\tEnter 1 For Registration Status 'Pending'\n\tEnter 2 For Registration Status 'Partially Complete'\n\tEnter 3 For Registration status 'Complete'\n\tEnter Choice: "))
    while choice < 1 or choice > 3:
        choice = int(input("\tEnter 1 For Registration Status 'Pending'\n\tEnter 2 For Registration Status 'Partially Complete'\n\tEnter 3 For Registration Status 'Complete'\n\tEnter Choice: "))

    if choice == 1:
        return 'Pending'
    elif choice == 2:
        return 'Partially Complete'
    elif choice == 3:
        return 'Complete'


def Add_Registration_data():
    with open('Registration.json', 'r') as f:
        Data = json.load(f)

    Data['Student'].append({"Student id": input("Enter Student ID: "),
                            "Student name": input("Enter Student Name: "),
                            "Section": input("Enter Section: "),
                            "Courses": [course for course in input("Enter Course Code Separated By Space (e.g. CSE121 CSE134): ").split()],
                            "Registration status": Registration_status()})

    with open('Registration.json', 'w') as f:
        json.dump(Data, f, indent=4)
    print('~~~~~~~~~~~~~~~~~~~~~~New Registration Data Added Successfully!!!~~~~~~~~~~~~~~~~~~~~~~')
    print(
        '**********************************************************************************************************************************\n')


def Search_and_view():
    with open('Registration.json', 'r') as f:
        Data = json.load(f)

    id = input("Enter Student ID: ")
    print()
    flag = 0
    for data in Data:
        for x in Data[data]:
            if id == x['Student id']:
                flag = 1
                print('Detailed View For {} ID Is: '.format(id), '\n\tName: ' + x['Student name'], '\n\tSection: ', x['Section'], '\n\tCourses:', end=" ")
                [print(s, end=" ") for s in x['Courses']]
                print('\n\tRegistration Status: ' + x['Registration status'])

    if flag != 1:
        print('~~~~~~~~~~~~~~~~~~~~~~ID Not Found!!!~~~~~~~~~~~~~~~~~~~~~~')
        print(
            '**********************************************************************************************************************************\n')
        return
    print(
        '**********************************************************************************************************************************\n')


def Update_registration_status():
    with open('Registration.json', 'r') as f:
        Data = json.load(f)

    id = input('Enter Student ID To Update Registration Status: ')
    print()
    flag = 0
    for data in Data:
        for x in Data[data]:
            if id == x['Student id'] and x['Registration status'] == 'Pending':
                flag = 1
                print('Registration status of {} id is: '.format(id) + x['Registration status'])

                reg_status = int(input("\tEnter 1 For Update To 'Partially Complete'\n\tEnter 2 For Update To 'Complete'\n\tEnter Choice: "))
                if reg_status == 1:
                    x.update({'Registration status': 'Partially Complete'})

                    with open('Registration.json', 'w') as f:
                        json.dump(Data, f, indent=4)

                    print('~~~~~~~~~~~~~~~~~~~~~~Registration Status Successfully Updated!!!!~~~~~~~~~~~~~~~~~~~~~~')
                elif reg_status == 2:
                    x.update({'Registration status': 'Complete'})

                    with open('Registration.json', 'w') as f:
                        json.dump(Data, f, indent=4)

                    print('~~~~~~~~~~~~~~~~~~~~~~Registration Status Successfully Updated!!!!~~~~~~~~~~~~~~~~~~~~~~')

            elif id == x['Student id'] and x['Registration status'] == 'Partially Complete':
                flag = 1
                reg_status = int(input("\tEnter 1 For Update To 'Complete'\n\tEnter Choice: "))

                if reg_status == 1:
                    x.update({'Registration status': 'Complete'})

                    with open('Registration.json', 'w') as f:
                        json.dump(Data, f, indent=4)

                    print('~~~~~~~~~~~~~~~~~~~~~~Registration Status Successfully Updated!!!!~~~~~~~~~~~~~~~~~~~~~~')
            elif id == x['Student id'] and x['Registration status'] == 'Complete':
                flag = 1
                print('~~~~~~~~~~~~~~~~~~~~~~Registration Status Is Complete~~~~~~~~~~~~~~~~~~~~~~')

    if flag != 1:
        print('~~~~~~~~~~~~~~~~~~~~~~ID Not Found!!!~~~~~~~~~~~~~~~~~~~~~~')
        print('**********************************************************************************************************************************\n')
        return
    print('**********************************************************************************************************************************\n')


def Delete_registration_record():
    with open('Registration.json', 'r') as f:
        Data = json.load(f)

    id = input("Enter Student ID To Delete Registration Record: ")
    print()
    flag = 0
    for data in Data:
        for i in range(len(Data[data])):
            if id == Data[data][i]['Student id']:
                flag = 1
                del Data[data][i]

    if flag != 1:
        print('~~~~~~~~~~~~~~~~~~~~~~ID Not Found!!!~~~~~~~~~~~~~~~~~~~~~~')
        print('**********************************************************************************************************************************\n')
        return

    with open('Registration.json', 'w') as f:
        json.dump(Data, f, indent=4)

    print('~~~~~~~~~~~~~~~~~~~~~~Registration Record Successfully Deleted!!!!~~~~~~~~~~~~~~~~~~~~~~')
    print('**********************************************************************************************************************************\n')


def root():
    while True:
        try:
            choice = int(input("Enter 1 To 'ADD NEW REGISTRATION DATA'\nEnter 2 To 'SEARCH BY STUDENT ID AND VIEW DETAIL INFORMATION'\nEnter 3 To 'UPDATE REGISTRATION STATUS'\nEnter 4 To 'DELETE REGISTRATION RECORD'\nEnter 5 To 'EXIT'\nEnter Choice: "))
        except:
            print('~~~~~~~~~~~~~~~~~~~~~~Enter Valid Choice!!!~~~~~~~~~~~~~~~~~~~~~~')
            root()

        while choice < 1 or choice > 5:
            try:
                choice = int(input("Enter 1 To 'ADD NEW REGISTRATION DATA'\nEnter 2 To 'SEARCH BY STUDENT ID AND VIEW DETAIL INFORMATION'\nEnter 3 To 'UPDATE REGISTRATION STATUS'\nEnter 4 To 'DELETE REGISTRATION RECORD'\nEnter 5 To 'EXIT'\nEnter Choice: "))
            except:
                print('~~~~~~~~~~~~~~~~~~~~~~Enter Valid Choice!!!~~~~~~~~~~~~~~~~~~~~~~')
                root()

        if choice == 1:
            print('\n**********************************************************************************************************************************')
            Add_Registration_data()

        elif choice == 2:
            print('\n**********************************************************************************************************************************')
            Search_and_view()

        elif choice == 3:
            print('\n**********************************************************************************************************************************')
            Update_registration_status()

        elif choice == 4:
            print('\n**********************************************************************************************************************************')
            Delete_registration_record()
        elif choice == 5:
            print('\n*****************************************************Program Ended****************************************************************')
            break


root()
