"""Model for aircraft flights"""


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
        print("Passenger {} allocated to seat {}".format(passenger, seat))

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

    def num_available_seats(self):
        return sum(sum(1 for s in row, values() if s is None)
                    for row in self._seating
                    if row is not None)


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    # return allowed rows and seats as tuple containing range object and a string of seat letters
    def seating_plan(self):
        return (range(1, self._num_rows + 1), 'ABCDEFGHJK'[:self._num_seats_per_row])


# module level convenience
def make_flight():
    f = Flight("BA7588", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
    f.allocate_seat("12A", "Guido van Rossum")
    f.allocate_seat("15F", "Bjarne Stroustrup")
    f.allocate_seat("15E", "Anders Hejlsberg")
    f.allocate_seat("1C", "John McCarthy")
    f.allocate_seat("1D", "Richard Hickey")

    f.relocate_passenter("12A", "15A")
    f.relocate_passenter("1D", "1C")
    return f

if __name__ == "__main__":
    make_flight()
