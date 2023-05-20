
from prac09.taxi import Taxi
from prac09.silver_service_taxi import SilverServiceTaxi

MENU = "Q)uit, C)hoose taxi, D)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    user_input = ""
    current_taxi = None
    bill_to_date = 0.00
    print("Let's drive!")
    while user_input.lower() != 'q':
        print(MENU)
        user_input = input()
        if user_input.lower() == 'd':
            if current_taxi is None:
                print('You need to choose a taxi before you can drive')
            else:
                driving_distance = int(input('Drive how far? '))
                current_taxi.start_fare()
                current_taxi.drive(driving_distance)
                bill_to_date = bill_to_date + current_taxi.get_fare()
                print(f'Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}')

        if user_input.lower() == 'c':
            print('Taxis available: ')
            print(display_taxis(taxis))
            chosen_taxi = int(input('Choose taxi: '))

            if chosen_taxi == 0:
                current_taxi = taxis[0]
            elif chosen_taxi == 1:
                current_taxi = taxis[1]
            elif chosen_taxi == 2:
                current_taxi = taxis[2]
            else:
                print('Invalid taxi choice')

        if user_input.lower() != 'q' and user_input.lower() != 'd' and user_input.lower() != 'c':
            print('Invalid option')

        if user_input.lower() == 'q':
            print(f'Total trip cost: ${bill_to_date:.2f}')
            print('Taxis are now: ')
            print(display_taxis(taxis))

        print(f'bill to date: ${bill_to_date:.2f}')


def display_taxis(taxis):
    """Display list of taxis"""
    all_taxis = ""
    count = 0
    for taxi in taxis:
        all_taxis += str(count) + ' ' + taxi.__str__() + '\n'
        count += 1
    all_taxis = all_taxis.strip()
    return all_taxis


main()
