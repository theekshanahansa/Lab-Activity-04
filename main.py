from faculty import FacultyMember, FacultyModule, FacultyLecture


def main():
    faculty_lecture = FacultyLecture()

    # Create FacultyMember instances
    member1 = FacultyMember("Mr.Supun", 35, "Lecture", "Decision Science")
    member2 = FacultyMember("Dr.Amali", 40, "Department Head", "Management of Technology")
    member3 = FacultyMember("Dr.Venura", 50, "Lecture", "Decision Science")

    # Create FacultyModule instances
    module1 = FacultyModule("Introduction to Marketing", "MKT101")
    module2 = FacultyModule("Advanced Marketing Strategies", "MKT201")
    module3 = FacultyModule("Corporate Finance", "FIN301")

    # Add modules to faculty members
    member1.add_module(module1)
    member2.add_module(module2)
    member3.add_module(module3)

    # Add members to the faculty lecture
    faculty_lecture.add_member(member1)
    faculty_lecture.add_member(member2)
    faculty_lecture.add_member(member3)

    # Display all members
    faculty_lecture.display_all_members()


if __name__ == "__main__":
    main()
