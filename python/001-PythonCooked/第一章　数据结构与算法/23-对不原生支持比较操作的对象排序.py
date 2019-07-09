from operator import attrgetter

class User:
    def __init__(self,user_id):
        self.user_id = user_id
    def __repr__(self):
        return "User({})".format(self.user_id)

if __name__ == '__main__':
    users = [User(23), User(3), User(99)]
    print("users:",users)
    users_user_id = sorted(users, key=lambda u: u.user_id)
    print('users_user_id:',users_user_id)
    User_att = sorted(users, key= attrgetter('user_id'))#可以根据类内的某个参数对对象排序
    # User_att = sorted(users, key= attrgetter('user_id','first_name')) #也可以接受多个参数排序
    print("User_att",User_att)
    user_min = min(users, key = attrgetter('user_id'))
    user_max = max(users, key = attrgetter('user_id'))
    print("user_min:",user_min, 'user_max:',user_max)