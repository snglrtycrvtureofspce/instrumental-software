class Animal:
    def __init__(self, view, weight):
        self.view = view
        self.weight = weight

    def print(self):
        print('Вид: ' + self.view + '\nВес: ' + self.weight)

    def display_into(self):
        print(f'View:{self.view}. Weight:{self.weight}')


firstanimal = Animal('Elephant', str(1212))
firstanimal.print()
firstanimal.display_into()
