"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seats = ('A', 'B', 'C', 'D')
    for num in range(number): 
        yield seats[num % 4]

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seats = ('A', 'B', 'C', 'D')
    seats_count = 0
    row_count = 1
    while seats_count < number:
        if row_count != 13:
            for seat in range(4):
                if seats_count >= number: break
                yield f'{row_count}{seats[seat]}'
                seats_count += 1
        row_count += 1
        continue

def assign_seats(passengers:list):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat_numbers = generate_seats(len(passengers))
    return {passenger: next(seat_numbers) for passenger in passengers}

def generate_codes(seat_numbers:list, flight_id:str):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        ticket_id = seat + flight_id
        yield ticket_id + (12 - len(ticket_id)) * '0'