from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        output = []
        for room in self.rooms:
            exp = room.expenses + room.room_cost
            if exp <= room.budget:
                output.append(f'{room.family_name} paid {exp:.2f}$ and have {room.budget:.2f}$ left.')
                room.budget -= exp
            else:
                output.append(f"{room.family_name} does not have enough budget and must leave the hotel." )
                self.rooms.remove(room)
        return '\n'.join(output)

    def status(self):
        to_output = f'Total population: {sum([room.members_count for room in self.rooms])}\n'
        for room in self.rooms:
            to_output += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            for n, child in enumerate(room.children, 1):
                to_output += f"- Child {n} monthly cost: {child.cost:.2f}$\n"
            to_output += f"--- Appliances monthly cost: {sum([a.get_monthly_cost() for a in room.appliances]):.2f}$\n"
        return to_output
