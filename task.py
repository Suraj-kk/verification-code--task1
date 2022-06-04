
import re
condition = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
terms = '^(?=.*[a-z)])(?=.*[A-Z])(?=.*\d)(?=.*[@$%!*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'

def begin ():
  global option
  option=input('login|reg|forgorpassword: ')
  if option=='login':
    access()
  elif option=='reg':
    register()
  elif option=='forgotpassword':
    retrive()
  else:
    print('please enter an option')


#register
def register():
  file=open('user_details.txt','r')
  username=input('enter your emailid :')
  if (re.search(condition, username)):
      print("Valid Email")
  else:
      print("Invalid Email ,please enter a valid email_id")
      register()

  password=input('enter your password :')
  if (re.search(terms,password)):
      file = open("user_details.txt", "a")
      file.write("\n" + username + "," + password)
      print("Valid password")

  else:
      print("Invalid password,please enter a valid password")
      register()

def access():
  file = open('user_details.txt', 'r')
  print(file)
  username = input('enter your email_id :')
  password = input('enter your password :')

  for i in file:
      a, b = i.split(',')
      b = b.strip()

      if b==password and a==username:
          print('login success')
          break
  else:
     print('username or password wrong')

def retrive():
    file = open('user_details.txt', 'r')
    username = input('enter your email_id :')
    for i in file:
       x = i.split(',')
       if x[0]==username:
           print( x[1] )

begin()
