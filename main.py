
from faculty import FacultyMember, FacultyLecture


def main():
    # Create an instance of FacultyLecture
    faculty_lecture = FacultyLecture()

    # Create some FacultyMember instances
    member1 = FacultyMember("Dr. John Doe", 45, "Professor", "Marketing")
    member2 = FacultyMember("Dr. Jane Smith", 38, "Associate Professor", "Finance")
    member3 = FacultyMember("Dr. Emily Johnson", 50, "Lecturer", "Management")

    # Add members to the faculty lecture
    faculty_lecture.add_member(member1)
    faculty_lecture.add_member(member2)
    faculty_lecture.add_member(member3)

    # Display all members
    faculty_lecture.display_all_members()


if __name__ == "__main__":
    main()
