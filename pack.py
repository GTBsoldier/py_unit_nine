# dog.py
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def get_name(self):
        return self.name

    def add_trick(self, trick):
        self.tricks.append(trick)

    def print_tricks(self):
        print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")


# pack.py
from dog import Dog

class Pack:
    def __init__(self, leader):
        self.members = [leader]
        self.leader_index = 0

    def get_leader_name(self):
        return self.members[self.leader_index].get_name()

    def add_member(self, new_member):
        self.members.append(new_member)

    def print_pack(self):
        print("The pack contains:")
        for member in self.members:
            print(f"\t{member.get_name()}")

    def new_leader(self, index):
        if 0 <= index < len(self.members) and index != self.leader_index:
            old_leader_name = self.get_leader_name()
            self.leader_index = index
            new_leader_name = self.get_leader_name()
            print(f"{new_leader_name} deposes {old_leader_name} as the leader of the pack.")
        else:
            print("That is not a valid dog.")
        print(f"Current pack leader: {self.get_leader_name()}")

    def perform_trick(self, trick):
        for member in self.members:
            member.add_trick(trick)

    def all_print_tricks(self):
        for member in self.members:
            member.print_tricks()

    def __str__(self):
        return f"Pack with leader: {self.get_leader_name()}"

# Example usage:
if __name__ == "__main__":
    dog1 = Dog("Fido")
    dog2 = Dog("Spot")
    dog3 = Dog("Rover")

    pack = Pack(dog1)

    pack.add_member(dog2)
    pack.add_member(dog3)

    pack.print_pack()

    pack.new_leader(2)

    pack.perform_trick("sit")
    pack.all_print_tricks()

    print(pack)
    print(dog1)
