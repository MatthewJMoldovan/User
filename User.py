class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0


    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        print('\n')
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points += 200
            print(f"{self.first_name}, You've earned 200 points for enrolling! Your new balance is {self.gold_card_points} points!")
            print('\n')
        else:
            print(f"{self.first_name}, You are already a rewards member!")
            print('\n')
        return self

    def spend_points(self, points_spent):
        if points_spent <= self.gold_card_points:
            self.gold_card_points -= points_spent
            print(f"{self.first_name}, You've spent {points_spent} points! You have {self.gold_card_points} points remaining!")
            print('\n')
        else:
            print(f"{self.first_name}, You don't have enough points!")
            print('\n')
        return self




matt = User('Matt', 'Moldovan', 'matthewmoldovan@outlook.com', 24)
jane = User('Jane', 'Doe', 'jane.doe@gmail.com', 32)
john = User('John', 'Doe', 'johndoeisthecoolest@aol.com', 28)




matt.display_info().enroll().spend_points(50).display_info().enroll()
jane.enroll().spend_points(80).display_info()
john.display_info().spend_points(40)

