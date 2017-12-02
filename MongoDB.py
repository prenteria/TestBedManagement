from pymongo import MongoClient

# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost')#27017
db = client.local
print '\n sap sap \n'

def insertUser(name, email, password, orginization, skill_level, user_type):
    try:
        name = raw_input('Enter User name :')
        email = raw_input('Enter email :')
        password = raw_input('Enter password :')
        orginization = raw_input('Enter orginization :')
        skill_level = raw_input('Enter skill_level :')
        user_type = raw_input('Enter user_type :')
        
        print '\Inserting: \n'
        db.User.insert_one(
            {
            "name": name,
            "email":email,
            "password":password,
            "orginization":orginization,
		    "skill_level":skill_level,
            "user_type":user_type
            })
        print '\nInserted data successfully\n'
    
    except Exception, e:
        print str(e)


def deleteUser():
    try:
	    criteria = raw_input('\nEnter users name to delete\n')
	    db.User.delete_many({"name":criteria})
		
	    print '\nDeletion successful\n'
		
    except Exception, e:
	    print str(e)

def main():
    
    while(1):
    # chossing option to do CRUD operations
        selection = raw_input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')
    
        if selection == '1':
           name = raw_input('Enter User name :')
           email = raw_input('Enter email :')
           password = raw_input('Enter password :')
           orginization = raw_input('Enter orginization :')
           skill_level = raw_input('Enter skill_level :')
           user_type = raw_input('Enter user_type :')
           insertUser(name, email, password, orginization, skill_level, user_type)
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            deleteUser()
        else:
            print '\n INVALID SELECTION \n'
			
if __name__ == '__main__':
   main()			
# Function to insert data into mongo db
