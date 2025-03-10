'''Task 12: Import the modules utils and visual'''

from utils import *
from graphs import *

'''Task 13: Create an empty list named 'pokedex'.
    This will be used to store your pokemon. '''

pokedex = []

def run():
   
    '''
    Task 14: Call the function startup from the module utils.
    '''

    startup()

    '''
    Task 15: Populate the pokedex list from pokedex.csv file, using an appropriate 
    function from utils module.
    '''

    pokedex = load_pokes("pokedex.csv")

    while True:
        '''
        Task 16: Using an appropriate function in the module utils, display
        a menu of options for the different operations that can be performed on the data.
        Assign the selected option to a suitable local variable
        '''

        option = options()
        
        '''
        Task 17: Check if the user selected the option to check Pokemon. If so,
        then do the following:
        - Use the appropriate function in the module utils to display a submenu 
        of suitable options.
        '''

        if option == 1:
            option2 = check_poke()
            if option2 == 1:
                by_name(pokedex)
            elif option2 == 2:
                by_type(pokedex)
            else:
                print("Invalid option!")
        elif option == 2:
            option2 = add_poke()
            if option2 == 1:
                pokemon = add_specific_poke()
                if pokemon is not None:
                    pokedex.append(pokemon)
            elif option2 == 2:
                pokedex.append(add_random_poke())
        elif option == 3:
            show_all(pokedex)
        elif option == 5:
            save_pokes(pokedex)
        elif option == 6:
            break
        elif option == 4:
            option2 = visualise()
            if option2 == 1:
                pie_chart(pokedex)
            elif option2 == 2
                pie_chart(pokedex)
        else:
            print("Invalid option! Try again")

        '''
            Task 18: If user chooses to show pokemon by name, then diplay all 
            information about this particular pokemon. If user chooses to show pokemon
            by type, display all pokemon of that type (full details)

        '''



        '''
        Task 19: Check if user selected option to add pokemon. If so, then do the following:
        - Use the appropriate function in the module utils to display a submenu of suitable options.
        '''
        '''
            Task 20: If user chooses to add specific pokemon, then search pokemon_database
            and add that pokemon to pokedex (if it exists). If user chooses to add pokemon
            at random, use appropriate function to add a random pokemon to their database
        '''
        '''
        Task 21: Check if user selected option to show all pokemon. If so, then print out the
        entire pokedex.
        '''
        '''
        Task 22: Check if user selected option to visualise their pokemon. If so, then do
        the following:
        - Use the appropriate function in the module utils to display a submenu of suitable
        options.
        '''
        '''
            Task 23: If user chooses to plot a pie chart, call appropriate function from 
            graphs module. Similarly, if user chooses to plot a bar chart, call an 
            appropriate function from graphs module.
        '''
        '''
        Task 24: Check if user selected option to save pokedex. If so, then save it to
        a suitable file.
        '''
        '''
        Task 25: Check if user selected option to exit. If so, finish the loop.
        '''
        '''
        Task 26: If the user selected an invalid option then display an error message
        '''

