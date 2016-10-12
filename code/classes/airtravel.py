"""Model for aircraft flights"""

from pprint import pprint as pp


class Flight:
    """A flight with a particular passenger aircraft."""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code in '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

        # unpack seating plan
        rows, seats = self._aircraft.seating_plan()
        # create list for seat allocation
        # use first entry to account for offset, then
        # one entry for each row in the aircraft, constructed with list comprehension over rows in Aircraft
        # we're not interested  in rows numbers so _ is used to discard them
        # item expression of list comprehension is a dictionary comprehension, maps seat letter to None (empty seat) for each seat in a row
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    # delegate to Aircraft so that callers of Flight don't have to know about Aircraft class
    def aircraft_model(self):
        return self._aircraft.model()

    # implementation detail method starts with underscore by convention
    def _parse_seat(self, seat):
        """Parse a seat designator into a valid row and letter.

        Args:
            seat: A seat designator such as 12F

        Returns:
            A tuple containing an integer and a string for row and seat.
        """
        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        # use string slicing to get all but last character
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        # row_numbers is a range object, which supports the container protocol, so can use `in` operator
        if row not in row_numbers:
            raise ValueError("Invalid row number {}".format(row))

        return row, letter

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        Args:
            seat: A seat designator such as '12C' or '21F'.
            passenger: The passenger name.

        Raises:
            ValueError: If the seat is unavailable.
        """
        row, letter = self._parse_seat(seat)

        # check if seat is occupied with an identity test against None
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger
        # print("Passenger {} allocated to seat {}".format(passenger, seat))

    def relocate_passenter(self, from_seat, to_seat):
        """Relocate a passenger to a different seat.

        Args:
            from_seat: The existing seat designator for the passenger to be moved.

            to_seat: The new seat designator.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} is already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None
        print("Passenger {} relocated from seat {} to seat {}".format(self._seating[to_row][to_letter], from_seat, to_seat))

    # two nested generator expressions:
    # Outer: filters for all rows which are not None (exclude dummy first row)
    # Value of each item in outer expression is sum number of None values in each row
    # Inner expression iterates over values of dictionary and adds 1 for each None found
    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None) for row in self._seating if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passenger seating allocations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield(passenger, "{}{}".format(row, letter))


class Aircraft:

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        # For simplicity, ignore complex seating arrangement in first-class
        return range(1, 56), "ABCDEFHJK"


# module level functions
def make_flights():
    f = Flight("BA758", AirbusA319("G-EUPT"))
    print("Number of available seats on flight {} is {}".format(f.number(), f._aircraft.num_seats()))
    f.allocate_seat("12A", "Guido van Rossum")
    f.allocate_seat("15F", "Bjarne Stroustrup")
    f.allocate_seat("15E", "Anders Hejlsberg")
    f.allocate_seat("1C", "John McCarthy")
    f.allocate_seat("1D", "Richard Hickey")
    f.make_boarding_cards(console_card_printer)

    g = Flight("AF72", Boeing777("F-GSPS"))
    print("Number of available seats on flight {} is {}".format(g.number(), g._aircraft.num_seats()))
    g.allocate_seat("55K", "Larry Wall")
    g.allocate_seat("33J", "Yukihiro Matsumoto")
    g.allocate_seat("4B", "Brian Kernigham")
    g.allocate_seat("4A", "Dennis Ritchie")
    g.make_boarding_cards(console_card_printer)


def console_card_printer(passenger, flight_number, seat, aircraft):
    output = "| Name: {0}"     \
              "  Flight: {1}"   \
              "  Seat: {2}"     \
              "  Aircraft: {3}" \
              " |".format(passenger, flight_number, seat, aircraft)
    banner = "+" + "-" * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()


if __name__ == "__main__":
    make_flights()
