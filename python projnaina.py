

def main():
    n = eval(input("Input number of emails:"))
    email_list = []
    email_split = ''
    for i in range(0,n):
        email = input("Enetr Email id:")
        email_list.append(email)
    print("after slicing")
    for j in email_list:
        email_split = j.split('@')
        print("User Name :",email_split[0],"Domain:",email_split[1].upper())

if __name__ == '__main__':
    main()

 

