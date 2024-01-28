import time
from itertools import islice
from typing import Tuple

filename = 'measurements2.txt'

n = 50  # Or whatever chunk size you want


temp_per_place_all_batches = [] # List of dicts i.e. [{'Alexandra': -7.6}, {'Malé': 30.6}, {'Pyongyang': 3.4}]
total_temp_per_place_all_batches = {}
avg_temp_per_place_all_batches = {}

def calc_average_over_entire_data(temp_per_place_all_batches):

    for place_temp_dict in temp_per_place_all_batches:
        for place, temp in place_temp_dict.items():
            if place in total_temp_per_place_all_batches.keys():
                total_temp_per_place_all_batches[place][0] += temp
                total_temp_per_place_all_batches[place][1] += 1
            else:
                temp_with_count_list = [temp, 1]
                total_temp_per_place_all_batches[place] = temp_with_count_list

    for place, total_temp_with_count in total_temp_per_place_all_batches.items():
        avg_temp_per_place_all_batches[place] = total_temp_with_count[0]/total_temp_with_count[1]

    #print(total_temp_per_place_all_batches)
    #print(avg_temp_per_place_all_batches)


def batch_calculation(input_batch: Tuple, batch_counter):
    '''
    Calculate average per batch
    '''
    batch_counter += 1
    print("Processing batch - ", batch_counter)
    input_batch_dict = {}

    for element in input_batch:
        element_list = element.split(';')
        if element_list[0] in input_batch_dict.keys():
            input_batch_dict[element_list[0]] += float(element_list[1])
        else:
            input_batch_dict[element_list[0]] = float(element_list[1])

    #print(len(input_batch_dict.keys()))
    input_batch_list = [{k: v} for k, v in input_batch_dict.items()]
    temp_per_place_all_batches.extend(input_batch_list)
    #print(temp_per_place_all_batches)
    return batch_counter

def main():

    start_time = time.time()
    batch_counter = 0
    temp_with_count_list = []

    with open(filename, 'rb') as f:
        for n_lines in iter(lambda: tuple(line.decode('utf-8').strip() for line in islice(f, n)), ()):    
            batch_counter = batch_calculation(n_lines, batch_counter)

    print(temp_per_place_all_batches)

    """ for place, temp in temp_per_place_all_batches.items():
        if place in total_temp_per_place_all_batches.keys():
            total_temp_per_place_all_batches[place][0] += temp
            total_temp_per_place_all_batches[place][1] += 1
        else:
            temp_with_count_list = [temp, 0]
            total_temp_per_place_all_batches[place] = temp_with_count_list

    print(calc_average_over_entire_data(total_temp_per_place_all_batches)) """

    calc_average_over_entire_data(temp_per_place_all_batches)

    print("Time taken:", (time.time() - start_time), "seconds")
            

if __name__ == '__main__':
    main()
