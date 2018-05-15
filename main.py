"""
issues
1.Add record
  1.1.input name and phone number
  1.2 save name and phone number in the storage
2. Show all records
  2.1 get all records of the storage
  2.2 display records
"""
base=[]
def start():
    a = '5'
    while a != '4':
     print('What do you want to do?')
     print('1.Enter a new record')
     print('2.Output all records')
     print('3. Delete abonent')
     print('4.Quit the program')
     a=input()
     if a=='1':
         rec = inpute_name_and_phone_number()
         save_name_and_phone_number_in_the_storage(rec)

     if a=='2':
       print(base)
     if a=='3':
         del_abon()
         print(base)
     if a=='4':
       exit()
def inpute_name_and_phone_number():
    name = input('Enter name: ')
    phone = input('Enter phone: ')
    print("Contact Information: ",name, phone)
    np= {'name': name, 'number': phone}
    return np


def save_name_and_phone_number_in_the_storage(record):
    print("Saving records...")
    print(record["name"])
    base.append(record)
    index=base.index(record)
    print(index,record)

def del_abon():
    print(base)
    ind = int(input('Enter number in the list '))
    print (base[ind])
    del base[ind]
        
def get_all_records():
    print("Get all records...")

def display_records():
    print("Display records...")

def main():
    print("MyPhonebook")
    start()

    print(base)
    get_all_records()
    display_records()
    print(rec)

if __name__ == "__main__":
    main()




