hanoi = [[1, 2, 3, 4], [], []]
ROD_MAP = {
  0:"A",
  1:"B",
  2:"C",
  }

def is_move_possible(departure_rod_index, destination_rod_index):
    departure_rod = hanoi[departure_rod_index]
    destination_rod = hanoi[destination_rod_index]

    if len(departure_rod) == 0:
        return False
    
    if len(destination_rod) == 0:
        return True
    
    return destination_rod[0] > departure_rod[0]

def move(departure_rod_index, destination_rod_index):
    if (is_move_possible(departure_rod_index, destination_rod_index)):
        #print(hanoi)
        top_disk = hanoi[departure_rod_index].pop(0)


        # hanoi[destination_rod_index] = hanoi[destination_rod_index] + [top_disk]
        hanoi[destination_rod_index] = [top_disk] + hanoi[destination_rod_index]

        print("с башни", ROD_MAP[departure_rod_index], "диск", top_disk, "перенести на", ROD_MAP[destination_rod_index])
    

def get_intermediate_rod_index(departure_rod_index, destination_rod_index):
    all_rods_indexes = [0, 1, 2]
    rod_indexess_without_departure = [i for i in all_rods_indexes if i != departure_rod_index]
    only_one_rod_index_left = [i for i in rod_indexess_without_departure if i != destination_rod_index ]
    return only_one_rod_index_left[0]


def solve_hanoi(N, departure_rod_index, destination_rod_index):
    if N == 1:
        move(departure_rod_index, destination_rod_index)
    
    else:
        intermediate_rod_index = get_intermediate_rod_index(departure_rod_index, destination_rod_index)
        solve_hanoi(N - 1, departure_rod_index, intermediate_rod_index)
        move(departure_rod_index, destination_rod_index)
        solve_hanoi(N - 1, intermediate_rod_index, destination_rod_index)

solve_hanoi(4, 0, 2)
# print(hanoi)