class FacultyMember:
    def __init__(self, name, age, position, department):
        self.name = name
        self.age = age
        self.position = position
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")
        print(f"Department: {self.department}")
        print("-" * 20)


class FacultyLecture:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def display_all_members(self):
        for member in self.members:
            member.display_details()
