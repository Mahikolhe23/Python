from loguru import logger

# logger.info('"""Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that\nwe are implemeting all the logics by ourself. The aim here is to build our \"4 BHK\" house with the\n \thelp of \'Python programming\'. We have total land is of \\100 ft * 100ft /, to colmplete the house\n \twe have total 6 labours with \'different skill set like \"\\\ building wall or building roof \\\\".\n\t\tI have to print this paragraph as it is given here."""')


# list1 = [1,2,3]
# list2 = [4,5,6,]

# list1 = list1 + list2

# for i in range(5):
#     print('* ' * (i+1))

# for i in range(11):
#     if i%2 == 0:
#         print(i)


# c = 5
# for i in range(c):
#     print((c - i) * '* ')

# paragraph = """Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
# data warehouse and business intelligence industry’s thought leader on the dimen
# sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
# books written by Ralph and his colleagues have been the industry’s best sellers 
# since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
# coinvented the Star workstation, the fi rst commercial product with windows, icons, 
# and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
# electrical engineering from Stanford University"""

# para_list = paragraph.split(' ')
# print(para_list)
# c = 0 
# for i in para_list:
#     if i.lower() == 'the':
#         c += 1
# print(c)


# num_list = [5, 18, 77, 108, 930]
# new_num = 100

# for n in range(len(num_list)):
#     new_list = []
#     if new_num < num_list[n]:
#         new_list = num_list[n:]
#         num_list = num_list[0:n]   
#         num_list.append(new_num)
#         num_list = num_list + new_list 
#         break
         
# print(num_list)


# print('Welcome to calculator')
# ans = int(input("Enter the first number - "))

# while True:
#     oper = int(input('Enter operation want to perform \n1. Addition\n2. Subtraction\n3. Multiply\n4. Divide\n5. Total\n'))
#     if oper == 5:
#         print(f"Final ans - {ans}")
#         break

#     num2 = int(input("Enter the next number - "))
#     if oper == 1:
#         ans +=  num2
#     elif oper == 2:
#         ans -= num2
#     elif oper == 3:
#         ans *= num2
#     elif oper == 4:
#         ans /= num2


    
# num_list = [1,2,3,4,5,6,7,8,9,10]
# new_list = [n for n in num_list if n%2==0]
# new_list = ['Even' if n%2==0 else 'odd' for n in num_list]

# print(new_list)


# name_dict = {"mahi":10,"niku":20,"pk":30}

# for name in name_dict:
#     print(name, name_dict[name])

# for key, value in name_dict.items():
#     print(key,value)


# Mahesh 3 , Ramesh 2 , Ram 4 , total 50 days
# labour_cost = {"Mahesh":500,"Ramesh":400,"Sumesh":300,"Ram":600}

# days = 50
# Mahesh_ab = 3
# Ramesh_ab = 2
# Ram_ab = 4
# Sumesh_ab = 7
# total_cost = 0

# for name in labour_cost:
#     if name == "Mahesh":
#         total_cost += (days - Mahesh_ab) * labour_cost[name] 
#     if name == "Ramesh":
#         total_cost += (days - Ramesh_ab) * labour_cost[name] 
#     if name == "Sumesh":
#         total_cost += (days - Sumesh_ab) * labour_cost[name] 
#     if name == "Ram":
#         total_cost += (days - Ram_ab) * labour_cost[name] 

# # print(total_cost)

# # labour_cost.update({"Manish":550})
# # print(labour_cost)

# # new_cost = labour_cost.copy()
# # print(id(new_cost))
# # print(id(labour_cost))

# labour_cost = {key:labour_cost[key]+100 for key in labour_cost}
# print(labour_cost)

# data = {"DERF":0,"POENKN":10,"DD":7,"MAINDATA":[{"IDD":"d3454355","BDD":"5678hfjhjh","LINKID":4,"HeaderFields":[{"FieldTypeName":"H1","Value":"false"},{"FieldTypeName":"H2","Value":"148877564"},{"FieldTypeName":"H3","Value":"20230930"},{"FieldTypeName":"H4","Value":"20231130"},{"FieldTypeName":"H5","Value":"2441.56"},{"FieldTypeName":"H6","Value":"0.00"},{"FieldTypeName":"H7","Value":"2411.56"},{"FieldTypeName":"H8","Value":"EUR"},{"FieldTypeName":"H9","Value":"00115190035"},{"FieldTypeName":"H10","Value":""},{"FieldTypeName":"H11","Value":"4500575382"},{"FieldTypeName":"H12","Value":"0.00"},{"FieldTypeName":"H13","Value":""},{"FieldTypeName":"H14","Value":""},{"FieldTypeName":"H15","Value":"F0"},{"FieldTypeName":"H16","Value":"87"},{"FieldTypeName":"H17","Value":"0.00"},{"FieldTypeName":"H18","Value":""},{"FieldTypeName":"H19","Value":""},{"FieldTypeName":"H20","Value":"No"}],"CodingLines":[],"Tables":[{"N1":"233553","N2":"3555","N3":"ASDDDD","N4":"334324","N5":"900.00","N6":"1.29","N7":"387.00","N8":"","N9":"0.00","N10":"","N11":"","N12":"","N13":"","N14":""},{"N1":"765765","N2":"67657657","N3":"ADFDFF)","N4":"667657","N5":"1000.00","N6":"1.94","N7":"1940.00","N8":"","N9":"0.00","N10":"","N11":"","N12":"","N13":"","N14":""},{"N1":"67657","N2":"76576576576","N3":"SFDFFDFSDF","N4":"7667676","N5":"1000.00","N6":"0.11456","N7":"114.56","N8":"","N9":"0.00","N10":"","N11":"","N12":"","N13":"","N14":""}],"INININ":"148877564","SDRER":"null"},{"IDD":"frret5","BDD":"5trtry4566","LINKID":4,"HeaderFields":[{"FieldTypeName":"H1","Value":"false"},{"FieldTypeName":"H2","Value":"ICI2300397"},{"FieldTypeName":"H3","Value":"20231219"},{"FieldTypeName":"H4","Value":"20240331"},{"FieldTypeName":"H5","Value":"76.44"},{"FieldTypeName":"H6","Value":"0.00"},{"FieldTypeName":"H7","Value":"76.44"},{"FieldTypeName":"H8","Value":"INR"},{"FieldTypeName":"H9","Value":"56676765"},{"FieldTypeName":"H10","Value":""},{"FieldTypeName":"H11","Value":"0.00"},{"FieldTypeName":"H12","Value":""},{"FieldTypeName":"H13","Value":""},{"FieldTypeName":"H14","Value":"F1"},{"FieldTypeName":"H15","Value":"87"},{"FieldTypeName":"H16","Value":"0.00"},{"FieldTypeName":"H17","Value":""},{"FieldTypeName":"H18","Value":""}],"CodingLines":[{"CODE1":0.0,"CODE2":76.44,"CODE3":"5645654","CODE4":"","CodingFields":[{"FieldName":"COL1","Value":"223DD666"},{"FieldName":"COL2","Value":"3454545"},{"FieldName":"COL3","Value":""},{"FieldName":"COL5","Value":""},{"FieldName":"COL5","Value":""}]}],"Tables":[],"INININ":"DER3434","SDRER":"null"}],"Final":"JKHJKLH0909908"}

# count  = 0
# for main in data.get('MAINDATA'):
#     for header in main.get('HeaderFields'):
#         if 'FieldTypeName' in header:
#             count += 1
# print(count)

# input = ([5,6],[6,7,8,9],[3])
# result = ()

# for item in input:
#     item = tuple(item)
#     result = result + item
 
# print(result)

# tuple1 = (10,2,3,5,6)
# tuple2 = (3,6,4,3,2)
# tuple3 = []
# for i in range(len(tuple1)):
#     ans = tuple1[i] ** tuple2[i] 
#     tuple3.append(ans)

# print(tuple(tuple3))


# set_var = {1,2,3,1,4,1}

# print(set_var)

# list1 = [1,2,3,4,5,6]
# list2 = [4,5,6,7,8]
# list3 = [4,5,9,10]
# list4 = []

# # print(set(list1).intersection(set(list2).intersection(set(list3))))

# for num in list1:
#     if num in list2 and num in list3:
#         list4.append(num)

# print(list4)

# ip_address = [
# "/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/test1.csv",
# "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2/file_path/teams/bin/test1.csv",
# "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path/teams/bin/test1.csv",
# "/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22/file_path/data/bin/test1.csv",
# "/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2/file_path//usr/bin/test1.csv",
# "/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28/file_path//usr/bin/test1.csv",
# "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31/file_path/worklog/bin/test1.csv",
# "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path//tmp/bin/test1.csv"
# ]

# unique_ip = set()

# for ip in ip_address:
#     ips = ip.split('server/')
#     new_ip = ips[1].split('/')[0]
#     unique_ip.add(new_ip)

# print(unique_ip)

# labour_cost = {"Mahesh":500,"Ramesh":400,"Sumesh":300,"Ram":600}

# final_value = ",".join(labour_cost)
# print(final_value)


import os

encryption_key = os.environ.get("ENCRYPTION_KEY")

if encryption_key:
    print(f"Key loaded successfully!  - {encryption_key}")
else:
    print("Encryption key not found!")



