import time
from itertools import islice
from typing import Tuple, List, Dict

filename = 'measurements.txt'

n = 500000  # Or whatever chunk size you want

temp_per_place_all_batches = [] # List of dicts i.e. [{'Alexandra': -7.6}, {'Malé': 30.6}, {'Pyongyang': 3.4}]
total_temp_per_place_all_batches = {}
avg_temp_per_place_all_batches = {}

def calc_average_over_entire_data(temp_per_place_all_batches: List[Dict[str, float]]) -> Dict[str, float]:
    '''
    Function to calculate average of entire data i.e. the parsed data that is returned from `batch_calculation()`

    :param temp_per_place_all_batches: List of dictionaries, each element in the form `{Name of Place: Temp in floating point}`
    :returns: Dict object in the form - `{Name of Place: Calculated avg temp in floating point}`
    '''

    for place_temp_dict in temp_per_place_all_batches:
        for place, temp in place_temp_dict.items():
            if place in total_temp_per_place_all_batches.keys():
                total_temp_per_place_all_batches[place][0] += temp
                total_temp_per_place_all_batches[place][1] += 1
            else:
                temp_with_count_list = [temp, 1]
                total_temp_per_place_all_batches[place] = temp_with_count_list

    for place, total_temp_with_count in total_temp_per_place_all_batches.items():
        avg_temp_per_place_all_batches[place] = round(total_temp_with_count[0]/total_temp_with_count[1], 1)

    return avg_temp_per_place_all_batches


def batch_calculation(input_batch: Tuple, batch_counter: int) -> int:
    '''
    Function to calculate average per batch

    :param input_batch: One input batch containing `n` rows of measurements data
    :returns: Updated batch_counter.
    '''
    batch_counter += 1
    print("Processing batch - ", batch_counter)
    input_batch_list = []

    for element in input_batch:
        element_list = element.split(';')
        input_batch_list.append({element_list[0]: float(element_list[1])})

    calc_average_over_entire_data(input_batch_list)
    return batch_counter


def main():

    start_time = time.time()
    batch_counter: int = 0

    with open(filename, 'rb') as f:
        for n_lines in iter(lambda: tuple(line.decode('utf-8').strip() for line in islice(f, n)), ()):    
            batch_counter = batch_calculation(n_lines, batch_counter)

    calc_average_over_entire_data(temp_per_place_all_batches)

    print(avg_temp_per_place_all_batches)
    print("Time taken:", (time.time() - start_time), "seconds")
            

if __name__ == '__main__':
    main()
