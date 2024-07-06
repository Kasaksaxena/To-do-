#from functions import get_todos,write_todos
import functions
import time

date=time.strftime("%b %d, %Y %H:%M:%S")
print("It is now" , date)

while True :
   user_function=input("Type add,show,complete,edit,end")
   user_function.strip()

   if user_function.startswith('add'):
        todo= user_function[4:]
        todos=functions.get_todos()
        
        todos.append(todo + "\n")
        functions.write_todos(todos)                 
   elif user_function.startswith('show'):
        todos=functions.get_todos()  
        for index,item in enumerate(todos):
             item=item.strip('\n') 
             row=f"{index+1}--){item}"
             print(row)
          
   elif user_function.startswith('complete'):
       try:
         
           number= int(user_function[9:])
           todos=functions.get_todos()   
           index=number-1
           todo_to_remove=todos[index].strip('\n')   
           todos.pop(index)
           functions.write_todos(todos)
              
           message=f"Todo {todo_to_remove} was removed from the list"   
           print(message)
       except IndexError:
           print("Your command is not valid")   
           continue 
         
   elif user_function.startswith('edit'):
       try:
           number=int(user_function[5:]) 
           number=number-1
           
           todos=functions.get_todos()
           new_todo=input("enter a new todo")
           todos[number]=new_todo +'\n'
           
           functions.write_todos(todos)
       except ValueError:
           print("Your command is not valid")
           continue
             
             
             
   elif user_function.startswith('end'):
           print(todos)
           break
   else:
       print("Command is not valid")  
       
print("Bye!")         
       
       
       