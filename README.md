# 1brc
This is a Python implementation of the wildly popular One Billion Rows challenge, initiated originally to be solved only in Java - https://github.com/gunnarmorling/1brc

## Experimental Setup

* All executions and runtimes have been noted while running on Python 3.8.18 on a Apple M2 Pro machine with a 16 GB RAM and 500 GB hard disk.
* `createMeasurements.py` copied from https://github.com/ifnesi/1brc/blob/main/createMeasurements.py.
* For every iteration, the runtime noted below is the observed best runtime after multiple trials with different batch sizes and other parameter adjustments.  

### Runtime improvements over iterations

| Iteration Number | Runtime (in seconds) |
| ---------------- | -------------------- |
| 1                | 1138.61              |
| 2                |               |

### Implementation Details and improvements done over iterations

##### Iteration 1
* Read the file in batches. Call `batch_calculation()` to do the calculation of average batch by batch, as the file is read. Inside this function - 
* * First the tuple object read is split and converted to a list - [Place, Temperature]
* * This list is then converted to a dict {Place, Temperature} and inserted into an List[Dict] variable - `input_batch_list`.
* * Finally we are passing this `input_batch_list` variable to the `calc_average_over_entire_data()` function.
* The `calc_average_over_entire_data()` achieves two objectives - 
* * When called from within `batch_calculation()`, it iterates over the `input_batch_list` and calculates the average per batch.
* * 



