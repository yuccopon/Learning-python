class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.favnumbers = []

    def greet(self):
        print("はじめまして。私は", self.name,"です。", self.age, "歳です。" )

    def celebrate_birthday(self):
        self.age += 1
        print("誕生日おめでとうございます！", self.name, "は", self.age, "歳になりました。")
    
    def add_favnumbers(self, number):
        self.favnumbers.append(number)
        print("あなたのお気に入りの数字は", self.favnumbers, "です。")
        

        
user = User("John", 20)

user.greet()
user.celebrate_birthday()
user.greet()
user.add_favnumbers(5)
user.add_favnumbers(10)


user = User("Catharine", 50)
user.greet()

