import time
from itertools import islice
from typing import Tuple, List, Dict

filename = 'measurements.txt'

n = 500000  # Or whatever chunk size you want

# Global vars - Declared with the suffix "_all_batches" because these are global variables that start by storing data at batch level but incrementally roll up to store the data for the entire batch. 
# Consider the variable `total_temp_per_place_all_batches` = {}
# E.g. 
# Batch 1 data - [{'Alexandra': -7.6}, {'Malé': 30.6}, {'Pyongyang': 3.4}]
# total_temp_per_place_all_batches = {'Alexandra': [-7.6, 1], 'Malé': [30.6, 1], 'Pyongyang': [3.4, 1]}
# Batch 2 data - [{'Alexandra': -4.6}, {'Malé': 32.2}, {'Alexandra': -1.7}]
# total_temp_per_place_all_batches = {'Alexandra': [-13.9, 3], 'Malé': [62.8, 2], 'Pyongyang': [3.4, 1]}
# Batch 3 data - [{'Alexandra': 3.6}, {'Pyongyang': 4.5}, {'Pyongyang': 2.7}]
# total_temp_per_place_all_batches = {'Alexandra': [-10.3, 4], 'Malé': [62.8, 2], 'Pyongyang': [10.6, 3]}
# 
# Notice how, because it is a global variable, the values for the places are incrementally rolling up, although data is still being processed in batches.

total_temp_per_place_all_batches = {}
avg_temp_per_place_all_batches = {}
min_temp_per_place_all_batches = {}
max_temp_per_place_all_batches = {}

def calc_avg_min_max_over_entire_data(temp_per_place: List[Dict[str, float]]) -> None:
    '''
    Function to calculate avg, min, max of entire data i.e. the parsed data that is returned from `batch_calculation()`

    :param temp_per_place: List of dictionaries, each element in the form `{Name of Place: Temp in floating point}`
    :returns: None
    '''

    # avg_temp_per_place_all_batches, min_temp_per_place_all_batches, max_temp_per_place_all_batches are all global variables, so any changes to these values are persisted across the lifecycle of the execution.
    # For every call of this function from `batch_calculation()`, it operates on the input batch of data having `n` rows defined above. Within the batch, it checks every key against the existing keys in these 
    # variables -> If already present, the value for that key i.e. the temp is either added or compared against the existing value. If not, the key/value pair gets added. 

    for place_temp_dict in temp_per_place:
        for place, temp in place_temp_dict.items():
            
            # Check if place has been recorded before
            if place in total_temp_per_place_all_batches.keys():
                total_temp_per_place_all_batches[place][0] += temp          # Sum of all temperatures recorded for the place. Will be used for avg temp calculation.
                total_temp_per_place_all_batches[place][1] += 1             # Counter to keep track of number of instances the place name is encountered. Will be used for avg temp calculation.

                # Check if temp is less than min temp saved for this place - if yes, update min temp.
                if temp < min_temp_per_place_all_batches[place]:
                    min_temp_per_place_all_batches[place] = temp

                # Check if temp is greater than max temp saved for this place - if yes, update max temp.
                if temp > max_temp_per_place_all_batches[place]:
                    max_temp_per_place_all_batches[place] = temp
            else:
                min_temp_per_place_all_batches[place] = temp
                max_temp_per_place_all_batches[place] = temp

                temp_with_count_list = [temp, 1]
                total_temp_per_place_all_batches[place] = temp_with_count_list

    for place, total_temp_with_count in total_temp_per_place_all_batches.items():
        avg_temp_per_place_all_batches[place] = round(total_temp_with_count[0]/total_temp_with_count[1], 1)


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

    # Once we have the batch data ready in a List[Dict[str, float]] format, we call the below function to calculate the avg, min, and max over this batch.
    calc_avg_min_max_over_entire_data(input_batch_list)
    return batch_counter


def main():

    start_time = time.time()
    batch_counter: int = 0

    with open(filename, 'rb') as f:
        for n_lines in iter(lambda: tuple(line.decode('utf-8').strip() for line in islice(f, n)), ()):    
            batch_counter = batch_calculation(n_lines, batch_counter)

    for place, avg_temp in avg_temp_per_place_all_batches.items():
        print(f"{place}: {min_temp_per_place_all_batches[place]}/{max_temp_per_place_all_batches[place]}/{avg_temp}")
    
    print("Time taken:", (time.time() - start_time), "seconds")
            

if __name__ == '__main__':
    main()
