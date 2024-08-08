def hello(name="GCA"):
    print('The hello function() has been executed!')
    
    def greet():
        return '\t This is the greet() func inside hello'
    
    def welcome():
        return '\t This is welcome() inside hello'
    
    return greet,welcome


my_new_func = hello("GCA")
print(my_new_func[0]())