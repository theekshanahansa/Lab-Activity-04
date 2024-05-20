
from faculty import FacultyMember, FacultyLecture


def main():

    faculty_lecture = FacultyLecture()

    # instances
    member1 = FacultyMember("Mr.Supun ", 35, "lecture", "Decision Science")
    member2 = FacultyMember("Dr.Amali", 40, "Department Head", "Management of technology")
    member3 = FacultyMember("Dr.Venura ", 50, "Lecture", "Decision science")

    # Add members to the faculty lecture
    faculty_lecture.add_member(member1)
    faculty_lecture.add_member(member2)
    faculty_lecture.add_member(member3)

    # Display all members
    faculty_lecture.display_all_members()


if __name__ == "__main__":
    main()
