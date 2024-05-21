from faculty import FacultyMember, FacultyModule, FacultyLecture


def main():
    faculty_lecture = FacultyLecture()

    # Create FacultyMember instances
    member1 = FacultyMember("Mr.Supun", 35, "Lecture", "Decision Science")
    member2 = FacultyMember("Dr.Amali", 40, "Department Head", "Management of Technology")
    member3 = FacultyMember("Dr.Venura", 50, "Lecture", "Industrial Management")
    memeber4 =  FacultyMember("Dr.Mahinda", 43,"Lecturer","Machine Learning")

    # Create FacultyModule instances
    module1 = FacultyModule("Fundamentals of Programming", "DA1254")
    module2 = FacultyModule("Lean Six Sigma", "TM1234")
    module3 = FacultyModule("Corporate Finance", "FIN301")
    module4 = FacultyModule("Machine Learning","DA2111")

    # Add modules to faculty members
    member1.add_module(module1)
    member2.add_module(module2)
    member3.add_module(module3)
    member4.add_module(module4)

    # Add members to the faculty lecture
    faculty_lecture.add_member(member1)
    faculty_lecture.add_member(member2)
    faculty_lecture.add_member(member3)
    faculty_lecture.add_member(member4)

    # Display all members
    faculty_lecture.display_all_members()


if __name__ == "__main__":
    main()
