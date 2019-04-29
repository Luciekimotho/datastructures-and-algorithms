
class OnlineLibrary:
    
    class User: 
        id = 0
        def __init__(self, id, name, email):
            self.id = id
            self.name = name
            self.email = email


        def users(self):
            return '{} {} {}'.format(self.id, self.name, self.email)
            #return self.id, self.name, self.email

    user1 = User(1, 'Lucy', 'lucy@me.com')


    user_str1 = ('Lucy-lucy@me.com')
    name, email = user_str1.split('-')
    print ('{} {}'.format(name, email))

    print(user1.users())


