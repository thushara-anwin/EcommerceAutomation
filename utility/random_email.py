import random
class RandomEmail:
    def random_email(self):
        num = random.randint(10, 900)
        num = str(num)
        return 'amy' + num + '@gmail.com'