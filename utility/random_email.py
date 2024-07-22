import random
class RandomEmail:
    def random_email(self):
        num = random.randint(100, 9000)
        num = str(num)
        return 'amy' + num + '@gmail.com'