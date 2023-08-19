#indentation ---> it refers to space that acts as a scope or block of that particular code/conditon
# data type = string,int,boolean,float,array(list) and object(dictionary)
# array or list --> it is a collection of elements
arr = ['one','two','three','four','five']
# it can be access using its index values ( indexes are nothing but it positioning ) it starts from 0 
# print(arr[0])
# -1 indicates that the flow will be reverse
# print(arr[-1])
# if need only some part of the array 
# array[start index:end index]
# print(arr[1:3])
# add some new elements to the existing array
arr.append('six') # it adds the given element in the end of the array or list
# print(arr)
arr.insert(2,'seven') # but insert method adds the given element to the particular postion
# print(arr)
arr.pop() # without passing index pop will remove end element in given array
arr.pop(2) # if we pass an index as a parameter to that pop method it will remove the element in that particular index
# print(arr)

#-------------------------------------------
# OBJECT is nothing but a dictionary 
# it is a collection of key value pairs
ex  =   {
        'key':'value',
        'name':'dhana veera',
        'age':25,
        }

# we can access the object value using its keys
# ex['key']
# print(ex['name'])

# combination of arrays and objects (MULTIPLE DATA TYPE) are known as JSON
# Java script Object Notation

students = [
    {
        'name':'Dhana Veera',
        'Class':'B.Tech',
        'Roll No':1,
        'Fee paid':True,
        'Selected Subjects':[
            'physics',
            'chemistry',
            'maths'
        ],
        'scores':{'physics':20,'maths':30,'chemisty':40}
    },
    {
        'name':'Pavan',
        'Class':'B.Tech',
        'Roll No':2,
        'Fee paid':False,
        'Selected Subjects':[
            'physics',
            'chemistry',
            
        ],
        'scores':{'physics':40,'maths':50,'chemisty':60}
    },
    {
        'name':'Naveen',
        'Class':'B.Tech',
        'Roll No':3,
        'Fee paid':True,
        'Selected Subjects':[
            'physics',
            'chemistry',
            'maths'
        ],
        'scores':{'physics':60,'maths':70,'chemisty':80}
    }
]

# Number of students
# print(len(students))



# finding the length of the array and then using the length as the range and finding the index of the element and using the index to find the element
# for i in range(0,len(students)):
#     print(students[i])

# getting each element from the array
# count=0
# for student in students:
#     if student['Fee paid']==False:
#         count+=1


# print(f"Out of {len(students)} students fee NOT paid only {count} students")


# print(students[0]['scores']['maths'])
# for student in students:
#     maths_score = student['scores']['maths']
#     student_name = student['name']
#     # print('maths score is',maths_score)
#     print("{} maths score is {}".format(student_name,maths_score))
    

# practice JSON handling

#print maths score if student selected maths as his selected subject
def sum(x,y,z):
    result = {
        'total score':x+y+z,
        'percentage':str((x+y+z)/300*100)+' %',
        
    }
    return result
for student in students:
    if 'maths' in student['Selected Subjects']:
        maths_score = student['scores']['maths']
        physics_score = student['scores']['physics']
        chemisty_score = student['scores']['chemisty']
        student_name = student['name']
        
        if student['scores']['maths']>10:
            print("{} maths score is {}".format(student_name,maths_score))
            print(f"{student_name} maths score is {maths_score}")
            print(student_name,"maths score is",maths_score)
            print(sum(maths_score,physics_score,chemisty_score))

            # concatination means adding of same data types
            # string + string 👌
            # array + array 👌
            # object + object 👌
            # string + int 💔
            # string + array 💔
            # string + object 💔
            # int + array 💔






