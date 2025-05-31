# 1brc
This is a Python implementation of the wildly popular One Billion Rows challenge, initiated originally to be solved only in Java - https://github.com/gunnarmorling/1brc

## Experimental Setup

* All executions and runtimes have been noted while running on Python 3.10 on a Apple M2 Pro machine with a 16 GB RAM and 500 GB hard disk.
* `createMeasurements.py` copied from https://github.com/ifnesi/1brc/blob/main/createMeasurements.py.
* For every iteration, the runtime noted below is the observed best runtime after multiple trials with different batch sizes and other parameter adjustments.  

### Runtime improvements over iterations

| Iteration Number | Runtime (in seconds) |                    Comments                      |
| ---------------- | -------------------- | ------------------------------------------------ |
| 1                | 1138.61              |  Only avg, single proces                         |
| 2                | 1354.95              |  Avg + Min + Max, single process                 |
| 3                |                      |                   |
| 4                |                      |                   |

### Implementation Details and improvements done over iterations

##### Iteration 1
* Declare 4 global variables:
  * `total_temp_per_place_all_batches` - Dict[str, List[str]] - {place: [total_temp_till_prev_batch, number_of_times_place_has_appeared_till_prev_batch]}
  * `avg_temp_per_place_all_batches` - Dict[str, float] - {place: avg_temp_till_prev_batch}
  * `min_temp_per_place_all_batches` - Dict[str, float] - {place: min_temp_till_prev_batch}
  * `max_temp_per_place_all_batches` - Dict[str, float] - {place: max_temp_till_prev_batch}
* Read the file in batches. Call `batch_calculation()` to do the calculation of average batch by batch, as the file is read. Inside this function - 
  * First the tuple object read is split and converted to a list - [Place, Temperature]
  * This list is then converted to a dict {Place, Temperature} and inserted into an List[Dict] variable - `input_batch_list`.
  * Finally we are passing this `input_batch_list` variable to the `calc_average_over_entire_data()` function.
* The `calc_average_over_entire_data()` achieves two objectives - 
  * When called from within `batch_calculation()`, it iterates over the `input_batch_list` and calculates the average per batch. To do this, we iterate over each {place, temp} combo in the `input_batch_list`. 
    * If the place is present: 
      * Add the temp to the `total_temp_per_place_all_batches[place]` and increment its `number_of_times_place_has_appeared_till_prev_batch` by 1. 
      * Compare the temp with the min temp in `min_temp_per_place_all_batches[place]` and if it's less than the existing value, update `min_temp_per_place_all_batches[place]`.
      * Compare the temp with the max temp in `max_temp_per_place_all_batches[place]` and if it's greater than the existing value, update `max_temp_per_place_all_batches[place]`.
    * If the place is not present:
      * Add a new element to `total_temp_per_place_all_batches` with the place as the key, the temp as the `total_temp_till_prev_batch` and set the value of `number_of_times_place_has_appeared_till_prev_batch` to 1. 
      * Add a new element to `min_temp_per_place_all_batches` with the place as the key, the temp as the minimum temp.
      * Add a new element to `max_temp_per_place_all_batches` with the place as the key, the temp as the maximum temp.
    * Finally add/update the avg temp for the place in `avg_temp_per_place_all_batches` by dividing the `total_temp_till_prev_batch` with `number_of_times_place_has_appeared_till_prev_batch`. 
  * So when `calc_average_over_entire_data()` runs iteratively over all batches, the min, max, and avg. for each place will have iteratively been updated in the respective global variables with the place name as the key and the corresponding temp as the value. 



