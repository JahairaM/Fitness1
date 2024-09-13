class Club:
    def __init__(self, name, address):
        self.name = name
        self.address = address


# Define the base Member class
class Members:
    def __init__(self, member_id, name):
        self.id = member_id
        self.name = name

    def check_in(self, club):
        pass

    def generate_bill(self):
        pass


# Single club members class
class Single(Members):
    def __init__(self, member_id, name, assigned_club):
        super().__init__(member_id, name)
        self.membership = "Single"
        self.club = assigned_club

    def check_in(self):
        while True:
            club_name = input("Please input your club or input Cancel to end the check-in process: ").title()
            if club_name == 'Cancel':
                print("Check-in process cancelled.")
                break
            elif club_name == self.club.name:
                print(f"Welcome to {self.club.name}.")
                break
            else:
                print(f"This is not your assigned club. Your assigned club is {self.club.name}. Please try again.")

    def generate_bill(self):
        print(f"\nBill for {self.name}:")
        print(f"Membership Type: {self.membership} Club")
        print(f"Assigned Club: {self.club.name}")
        print(f"Total Fees: $50.00\n")  # Example fee for single club members


# Multi-club members class
class Multi(Members):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)
        self.membership = "Multi"
        self.member_points = 0

    def check_in(self, club):
        self.member_points += 10  # Adds 10 points for each check-in
        print(f"{self.name} successfully checked into {club.name}. Membership Points: {self.member_points}")

    def generate_bill(self):
        print(f"\nBill for {self.name}:")
        print(f"Membership Type: {self.membership} Club")
        print(f"Total Fees: $75.00")  # Example fee for multi-club members
        print(f"Membership Points: {self.member_points}\n")


# Main function to handle user input and manage the application
def main():
    # Example clubs
    club1 = Club("Data Py Fitness Detroit", "123 Main St")
    club2 = Club("Data Py Fitness Lansing", "456 Park Ave")
    club3 = Club("Data Py Fitness Southfield", "789 Elm St")
    club4 = Club("Data Py Fitness Grand Rapids", "101 Maple Rd")

    members = []

    while True:
        print("\n--- Data Py Fitness Center ---")
        print("1. Add Member")
        print("2. Remove Member")
        print("3. Display Member Information")
        print("4. Check In Member")
        print("5. Generate Bill")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            member_id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            member_type = input("Enter Member Type (Single/Multi): ").lower()

            if member_type == "single":
                club_choice = input("Select Club (A:Detroit/B:Lansing/C:Southfield/D:Grand Rapids): ").upper()
                if club_choice == "Detroit Location":
                    club = club1
                elif club_choice == "Lansing Location":
                    club = club2
                elif club_choice == "Southfield Location":
                    club = club3
                elif club_choice == "Grand Rapids Location":
                    club = club4
                else:
                    print("Invalid club choice. Please try again.")
                    continue

                new_member = Single(member_id, name, club)
                members.append(new_member)

            elif member_type == "multi":
                new_member = Multi(member_id, name)
                members.append(new_member)

            print(f"Member {name} added successfully.")

        elif choice == "2":
            member_id = input("Enter Member ID to Remove: ")
            members = [m for m in members if m.id != member_id]
            print("Member removed successfully.")

        elif choice == "3":
            if not members:
                print("No members to display.")
            else:
                for m in members:
                    print(f"ID: {m.id}, Name: {m.name}, Membership: {m.membership}")

        elif choice == "4":
            member_id = input("Enter Member ID to Check In: ")
            club_choice = input("Enter Club for Check-In (A:Detroit/B:Lansing/C:Southfield/D:Grand Rapids): ").upper()
            club = None
            if club_choice == "A":
                club = club1
            elif club_choice == "B":
                club = club2
            elif club_choice == "C":
                club = club3
            elif club_choice == "D":
                club = club4
            else:
                print("Invalid club choice.")
                continue

            member = next((m for m in members if m.id == member_id), None)

            if member:
                if isinstance(member, Single):
                    member.check_in()
                elif isinstance(member, Multi):
                    member.check_in(club)
            else:
                print("Member not found.")

        elif choice == "5":
            member_id = input("Enter Member ID to Generate Bill: ")
            member = next((m for m in members if m.id == member_id), None)

            if member:
                member.generate_bill()
            else:
                print("Member not found.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
