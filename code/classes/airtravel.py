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

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        Args:
            seat: A seat designator such as '12C' or '21F'.
            passenger: The passenger name.

        Raises:
            ValueError: If the seat is unavailable.
        """
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        # use string slicing to get all but last character
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        # rows is a range object, which supports the container protocol, so can use `in` operator
        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))

        # check if seat is occupied with an identity test against None
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger


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
