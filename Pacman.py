""" ----------------------------------------------------------------------------
******** Search Code for DFS  and other search methods
******** (expanding front and extending queue)
******** author: Margaris Alexandros, Stefanos Fatsios
********
******** Κώδικας για DFS και άλλες μεθόδους αναζήτησης
******** (επέκταση μετώπου και διαχείριση ουράς)
******** Συγγραφέας: Μάργαρης Αλέξανδρος, Στέφανος Φάτσιος
"""


import copy
import random

""" ----------------------------------------------------------------------------
**** FRONT
**** Διαχείριση Μετώπου
"""

""" ----------------------------------------------------------------------------
**** QUEUE
**** Διαχείριση ουράς
"""


""" ----------------------------------------------------------------------------
**** Basic recursive function to create search tree (recursive tree expansion)
**** Βασική αναδρομική συνάρτηση για δημιουργία δέντρου αναζήτησης (αναδρομική επέκταση δέντρου)
"""


def find_solution(front, queue, closed, method):  # Okay
    if goal_state(front[0]):
        print('_GOAL_FOUND_')
        for i in range(len(queue[0])):
            print(queue[0][i])
    
    elif not front:
        print('_NO_SOLUTION_FOUND_')
            
    elif front[0] in closed:
        new_front = copy.deepcopy(front)
        new_front.pop(0)
        new_queue = copy.deepcopy(queue)
        new_queue.pop(0)
        find_solution(new_front, new_queue, closed, method)

    else:
        closed.append(front[0])
        front_copy = copy.deepcopy(front)
        front_children = expand_front(front_copy, method)
        queue_copy = copy.deepcopy(queue)
        queue_children = extend_queue(queue_copy, method)
        closed_copy = copy.deepcopy(closed)
        find_solution(front_children, queue_children, closed_copy, method)


def find_children(state):  # Okay

    children = []

    eat_state = copy.deepcopy(state)
    child_eat = eat(eat_state)

    right_state = copy.deepcopy(state)
    child_right = move_right(right_state)

    left_state = copy.deepcopy(state)
    child_left = move_left(left_state)

    up_state = copy.deepcopy(state)
    child_up = move_up(up_state)

    down_state = copy.deepcopy(state)
    child_down = move_down(down_state)

    if not child_down == state:
        children.append(child_down)

    if not child_up == state:
        children.append(child_up)

    if not child_left == state:
        children.append(child_left)

    if not child_right == state:
        children.append(child_right)

    if not child_eat == state:
        children.append(child_eat)

    return children


""" ----------------------------------------------------------------------------
** initialization of front
** Αρχικοποίηση Μετώπου
"""


def make_front(state):
    return [state]

""" ----------------------------------------------------------------------------
** initialization of queue
** Αρχικοποίηση ουράς
"""


def make_queue(state):
    return [[state]]


""" ----------------------------------------------------------------------------
**** expanding front
**** επέκταση μετώπου    
"""


def expand_front(front, method):
    if method == 'DFS':
        if front:
            f = open("DFS.txt", "a")
            for i in range(len(front)):
                f.write(str(i) + "\n")
                for j in range(len(front[i])):
                    f.write(str(front[i][j]))
                    f.write("\n")
            f.write("\n")
            f.close()
            node = front.pop(0)
            for child in find_children(node):
                front.insert(0, child)
                
    elif method == 'BFS':
        if front:
            f = open("BFS.txt", "a")
            for i in range(len(front)):
                f.write(str(i) + "\n")
                for j in range(len(front[i])):
                    f.write(str(front[i][j]) + "\n")
            f.write("\n")
            f.close()
            node = front.pop(0)
            for child in find_children(node):
                front.append(child)

    return front

""" ----------------------------------------------------------------------------
**** expanding queue
**** επέκταση ουράς
"""


def extend_queue(queue, method):
    if method == 'DFS':
        f = open("DFS_Queue.txt", "a")
        for i in range(len(queue)):
            f.write(str(i) + "\n")
            for j in range(len(queue[i])):
                f.write(str(queue[i][j]) + "\n")
        f.write("\n")
        f.close()
        node = queue.pop(0)
        queue_copy = copy.deepcopy(queue)
        children = find_children(node[-1])
        for child in children:
            path = copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0, path)

    elif method == 'BFS':
        f = open("BFS", "a")
        f = open("BFS_Queue.txt", "a")
        for i in range(len(queue)):
            f.write(str(i) + "\n")
            for j in range(len(queue[i])):
                f.write(str(queue[i][j]) + "\n")
        f.write("\n")
        f.close()
        node = queue.pop(0)
        queue_copy = copy.deepcopy(queue)
        children = find_children(node[-1])
        for child in children:
            path = copy.deepcopy(node)
            path.append(child)
            queue_copy.append(path)
    return queue_copy

""" ----------------------------------------------------------------------------
****Συναρτήσεις μετακίνησης και αν είναι μπορεί να μετακινηθεί. 
****Δεξιά - Αριστερά - Πάνω - Κάτω - Τρώει
"""


def can_eat(state):  # Okay
    for i in range(len(state)):
        for j in range(len(state[i])):
            for k in range(len(state[i][j])):
                if k == 1:
                    if state[i][j][k].isdigit() and state[i][j][k - 1] == 'p':
                        return 1


def can_move_up(state):
    for j in range(len(state[0])):
        for k in range(len(state[0][j])):
            if state[0][j][k] == 'p':
                return 0
    return 1


def can_move_down(state):
    for j in range(len(state[2])):
        for k in range(len(state[2][j])):
            if state[2][j][k] == 'p':
                return 0
    return 1


def can_move_left(state):
    for i in range(len(state)):
        for k in range(len(state[i][0])):
            if state[i][0][k] == 'p':
                return 0
    return 1


def can_move_right(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if j == len(state[i]) - 1:
                for k in range(len(state[i][j])):
                    if state[i][j][k] == 'p':
                        return 0
    return 1


def move_left(state):  # Okay
    if can_move_left(state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                for k in range(len(state[i][j])):
                    if state[i][j][k] == 'p':
                        state[i][j].pop(k)  # pop() when we move
                        state[i][j - 1].insert(0, 'p')  # insert() to where we move
                        return state
    else:
        return state


def move_right(state):  # Okay
    if can_move_right(state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                for k in range(len(state[i][j])):
                    if state[i][j][k] == 'p':
                        state[i][j].pop(k)  # pop() when we move
                        state[i][j + 1].insert(0, 'p')  # insert(0, 'p') to where we move
                        return state
    else:
        return state


def move_up(state):  # Okay
    if can_move_up(state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                for k in range(len(state[i][j])):
                    if state[i][j][k] == 'p':
                        state[i][j].pop(k)  # pop() when we move
                        state[i - 1][j].insert(0, 'p')  # insert() to where we move
                        return state
    else:
        return state


def move_down(state):
    if can_move_down(state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                for k in range(len(state[i][j])):
                    if state[i][j][k] == 'p':
                        state[i][j].pop(k)  # pop() when we move
                        state[i + 1][j].insert(0, 'p')  # insert() to where we move
                        return state
    else:
        return state


def eat(state):
    if can_eat(state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                for k in range(len(state[i][j])):
                    if state[i][j][k].isdigit():
                        val = int(state[i][j][k])
                        val -= 1
                        state[i][j][k] = str(val)
                        if state[i][j][k] == '0':
                            state[i][j].pop()
                            state[i][j].pop()
                        return state
    else:
        return state

""" ----------------------------------------------------------------------------
**** basic functions
**** βασικές συναρτήσης
**** rand_fruits -> Γεμίζει την λίστα με έναν αριθμό φρούτων που έχει δωθεί από τον χρήστη.
**** rand_names -> Γεμίζει την λίστα με ονόματα φρούτων.
**** rand_pac -> Βάζει το πακ-μαν σε μια τυχαία θέση.
**** empty_state -> Αδειάζει την λίστα όταν βλέπει όνομα φρούτου χωρίς φρούτα.
**** menu -> Ένα μενού με για την επιλογή αλγόριθμου αναζήτησης.
**** goal_state -> Κοιτάει αν το πακ-μαν έχει φτάσει σε goal_state.   
"""


def rand_fruits(state):
    print("Please type the number of fruits you want.(From 1 to 10)")
    fruits = int(input())
    if fruits > 10 or fruits < 1:
        print("Wrong input we will use the default option(5)")
        fruits = 5
    for i in range(len(state)):
        for j in range(len(state[i])):
            state[i][j].append('0')
    for i in range(fruits):

        rand = random.randrange(3)
        rand2 = random.randrange(4)
        val = int(state[rand][rand2][0])
        val += 1
        state[rand][rand2][0] = str(val)
    return state


def rand_names(state):
    temp_list = ['apple', 'orange', 'cherry', 'melon']
    for i in range(len(state)):
        for j in range(len(state[i])):
            state[i][j].append(random.choice(temp_list))


def rand_pac(state):
    rand = random.randrange(3)
    rand2 = random.randrange(4)
    state[rand][rand2].insert(0, 'p')


def empty_state(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            for k in range(len(state[i][j])):
                if state[i][j][k] == '0':
                    state[i][j].pop()  # Empty if fruits are 0.
                    state[i][j].pop()
                    break
    return state


def menu():
    print("Please choose method:\n1.DFS\n2.BFS")
    method = int(input())
    if method == 1:
        method = "DFS"
    elif method == 2:
        method = "BFS"
    else:
        print("Wrong input we will use the default method(DFS)")
        method = "DFS"
    return method


def goal_state(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            for k in range(len(state[i][j])):
                if state[i][j][k].isdigit():
                    return 0
    return 1

"""" ----------------------------------------------------------------------------
** Executing the code
** κλήση εκτέλεσης κώδικα
"""


def main():
    initial_state = [[[], [], [], []],
                     [[], [], [], []],
                     [[], [], [], []]]
    rand_fruits(initial_state)
    rand_names(initial_state)
    rand_pac(initial_state)
    empty_state(initial_state)
    method = menu()

    """ ----------------------------------------------------------------------------
    **** starting search
    **** έναρξη αναζήτησης
    """

    print('____BEGIN__SEARCHING____')
    find_solution(make_front(initial_state), make_queue(initial_state), [], method)


if __name__ == "__main__":
    main()