class Fly():
    def __init__(self, name):
        self.name = name

    def run_foo(self):
        '''A method in class Bar'''
        if self.name == 'Kent':
            print('You are Superman')
        else:
            print('You are not superman {}'.format(self.name))



