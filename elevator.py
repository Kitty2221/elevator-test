import random


class Passenger:

    def __init__(self, from_floor=1, to_floor=None):
        self.from_floor = from_floor
        self.to_floor = to_floor

    def __repr__(self):
        return f"{self.to_floor}"


class Elevator:

    def __init__(self):
        self.passenger_waiting = random.randint(0, 10)
        self.total_passengers = 0
        self.passengers_dict = {}
        self.direction = None
        self.max_floor = random.randint(5, 20)
        self.min_floor = 1
        self.capacity = 5
        self.current_floor = 1
        self.elevator_list = []
        self.generate_passengers()
        self.print_information()

        if self.current_floor > self.max_floor:
            raise ValueError(
                'The current floor cannot be greater than the maximum floor.')

    def random_floor(self, floor):
        return random.choice([k for k in range(1, self.max_floor - 1) if k != floor + 1])

    def people_on_the_current_floor(self):
        return self.passengers_dict.get(self.current_floor)

    def generate_passengers(self):
        for floor in range(1, self.max_floor + 1):
            for passenger in range(random.randint(0, 10)):
                self.passengers_dict.setdefault(floor, []).append(Passenger(floor, self.random_floor(floor), ))
                self.total_passengers += 1

    def passengers_enter_elevator(self):
        if self.direction:
            if self.people_on_the_current_floor():
                print(f'Passengers on the floor - {self.people_on_the_current_floor()}')
                for passenger in self.people_on_the_current_floor():
                    if (passenger.to_floor > self.current_floor
                            and len(self.elevator_list) < self.capacity):
                        print(f'+ Passenger {passenger} is coming in elevator  +')
                        self.elevator_list.append(passenger)
                        self.passengers_dict[self.current_floor] = list(filter(lambda p: p != passenger,
                                                                               self.passengers_dict[
                                                                                   self.current_floor]))

            if self.elevator_list:
                self.max_floor = max([passenger.to_floor for passenger in self.elevator_list])

            else:
                print('There are no passengers on the floor')

        else:
            if self.people_on_the_current_floor():
                print(f'Passengers on the floor - {self.people_on_the_current_floor()}')
                for passenger in self.people_on_the_current_floor():
                    if (passenger.to_floor < self.current_floor
                            and len(self.elevator_list) < self.capacity):
                        print(f'+ Passenger {passenger} is coming in elevator  +')
                        self.elevator_list.append(passenger)
                        self.passengers_dict[self.current_floor] = list(filter(lambda p: p != passenger,
                                                                               self.passengers_dict[
                                                                                   self.current_floor]))

                if self.elevator_list:
                    self.min_floor = min([passenger.to_floor for passenger in self.elevator_list])
            else:
                print('There are no passengers on the floor')

    def passengers_exit_elevator(self):
        for passenger in self.elevator_list:
            if passenger.to_floor == self.current_floor:
                print(f'- Passenger {passenger} is leaving elevator -')
                self.elevator_list = list(filter(lambda p: p != passenger, self.elevator_list))
                self.passengers_dict.setdefault(self.current_floor, []).append(
                    Passenger(self.current_floor,
                              self.random_floor(self.current_floor)))

    def move_up(self):
        self.direction = True
        print(f'*** Floor {self.current_floor} ***')
        print(' ▲  ', *self.elevator_list, '  ▲ ')

        if self.current_floor <= self.max_floor:
            self.passengers_exit_elevator()
            self.passengers_enter_elevator()
        else:
            raise ValueError('Can not move!')

        if self.current_floor != self.max_floor:
            self.current_floor += 1
        else:
            print("⭱ This is the maximum floor ⭱")

        print(' ▲  ', *self.elevator_list, '  ▲ ')

    def move_down(self):
        self.direction = False
        print(f'*** Floor {self.current_floor} ***')
        print('┃▼  ', *self.elevator_list, '  ▼┃')

        if self.current_floor >= 1:
            self.passengers_exit_elevator()
            self.passengers_enter_elevator()
        else:
            raise ValueError('Can not move!')

        print('┃▼  ', *self.elevator_list, '  ▼┃')
        if self.current_floor != self.min_floor:
            self.current_floor -= 1
        else:
            print("⤓ This is the minimal floor ⤓")

    def move_up_to_max(self):
        while self.current_floor != self.max_floor:
            self.move_up()
        self.move_up()

    def move_down_to_min(self):
        while self.current_floor != self.min_floor:
            self.move_down()
        self.move_down()

    def print_information(self):
        print(f'All passengers - {self.total_passengers}')
        print(f'Floors - {self.max_floor} ')
        for floor, passengers in self.passengers_dict.items():
            if self.current_floor == floor:
                print(f"{floor} floor: passengers - {passengers}  ⟸ Elevator")
            else:
                print(f"{floor} floor: passengers - {passengers}")

