# ECE4721J Lab 6: LU Decomposition

Implement a simple algorithm **Cholesky Decomposition** in Spark.

Goals:
- Get familiar with Spark
- Investigate new algorithms
- Run simple data analysis

## Cholesky Decomposition algorithm

Run Cholesky Decomposition algorithm with input from file

- Command: `$ python3 cholesky.py`
- Input: all files in `data/`
- Output: none (display output in terminal)

- Input format: `data/2.tsv` as sample

  ```log
    25	15	-5
    15	18	0
    -5	0	11
  ```

- Benchmark: compare results with numpy method `numpy.linalg.cholesk` as reference, and we can see that they are the same, which verifies that our implementation is correct.

- Submit to Spark: `$ spark-submit cholesky.py `
