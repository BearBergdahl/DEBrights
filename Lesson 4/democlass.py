class DemoClass:
    class_variable = 'This is everywhere'
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable
    
    def do_anything(self):
        return 'a_string', 'not_a_number' 

    def __str__(self):
        return f'This is a democlass with a class_variable: {self.class_variable} and a instance variable: {self.instance_variable}'
    
    def __repr__(self):
        return f'explained class_variable: {self.class_variable} list of my variables with suggested type if any: {self.instance_variable}'
            
demo_instance = DemoClass(42)
print(demo_instance.class_variable)
print(demo_instance.instance_variable)
print(demo_instance.do_anything())
second_instance = DemoClass(43)
print(second_instance.class_variable)
print(second_instance.instance_variable)
print(second_instance.do_anything())
print(second_instance)