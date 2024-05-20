

class FacultyModule:
    def __init__(self, module_name, module_code):
        self.module_name = module_name
        self.module_code = module_code

    def display_details(self):
        print(f"Module Name: {self.module_name}")
        print(f"Module Code: {self.module_code}")
        print("-" * 20)


class FacultyMember:
    def __init__(self, name, age, position, department):
        self.name = name
        self.age = age
        self.position = position
        self.department = department
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")
        print(f"Department: {self.department}")
        print("Modules:")
        for module in self.modules:
            module.display_details()
        print("-" * 20)


class FacultyLecture:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def display_all_members(self):
        for member in self.members:
            member.display_details()
