def greeting (name):
    print('hello'+ name.title()+'!')

    def greeting_2(name):
        print('hello {}!'.format(name.title()))
        print(f'helllo again{name.title()}!')
    
    greeting_2('Joel')