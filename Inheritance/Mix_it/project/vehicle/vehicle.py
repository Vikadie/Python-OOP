class Vehicle:

    def __init__(self, available_seats: int):
        self._available_seats = available_seats

    @property
    def available_seats(self):
        return self._available_seats
