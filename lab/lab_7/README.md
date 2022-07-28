# VE472 Lab 7

## Goal

- Work with a real dataset
- Practice with PCA and Gradient Descent using Spark
- Get familiar with Spark Dataframe and MLLib APIs

## Dataset

Please download the dataset `PBMC.tar.gz` from the data server.

In this lab, we use a pre-processed [table](https://academic.oup.com/bioinformatics/article/36/Supplement_1/i542/5870491#205479414) from the Peripheral blood mononuclear cell (PBMC) dataset. This dataset contains the amount of mRNA each cell is producing. Each cell can do its job using the following steps

1. Produce some mRNA, which are copies of substring of its DNA.
2. The mRNA can then be used to produce certain protein.

We can usually categorize the cells based on the amount of mRNAs they are producing.

## Tasks

### Importing Data and Pre-processing

1. Import the csv file `PBMC_16k_RNA.csv` into a spark dataframe.

     *Hint*: you can use `inferSchema='true'` option so that the number.

     **Answer**:

     ```python
     spark_df = spark.read.options(header='true', inferSchema='true').csv("datasets/PBMC_16k_RNA.csv")
     ```

2. Find the range of data in the first two features `KLHL17` and `HES4` inside the dataframe. Is it necessary to perform data standardization? Explain.

     **Answer**: In pyspark, we can use the following

     ```python
     spark_df.agg({'KLHL17': 'max'}).show()
     ```

     or using SQL language

     ```python
     spark_df.createOrReplaceTempView("data")
     spark.sql("SELECT max(KLHL17) FROM data").show()
     ```

     To get that `KLHL17` ranges from -0.11 to 10, and `HES4` ranges from -1.33 to 9.47. Since the range of data is approximately the same, we can skip the standardization part. However, we can still perform standardization to play safe.

### PCA Analysis

3. Why would PCA be useful when analysing this dataset?

     **Answer**: This is a dataset with 1882 features, we can use PCA to reduce the number of features to make further calculations (such as regression) faster and possibly plot the data in a lower dimensional space.

4. Use `org.apache.spark.mllib.feature.PCA` to perform PCA analysis on the dataset. Use the first 2 principal components.

     **Answer**:

     ```python
     from pyspark.ml.feature import PCA

     pca = PCA(k=2, inputCol='standardized_features', outputCol='pca_features')
     pca_model = pca.fit(standardized_df)
     pca_df = pca_model.transform(standardized_df)
     ```

5. How much does the two principal components explain the dataset? Do you consider the PCA to be useful or not?

     **Answer**:

     ```python
     pca_model.explainedVariance.toArray()
     ```

     We can see that the result gives 0.02942326, 0.01307317 respectively, which is not very large, meaning that there is not much correlation between columns in this dataset. However, considering that there are 1882 features, it is still acceptable that 2% of the variance is explained.

6. Now, import the csv file `PBMC_16k_RNA_label.csv`. This csv contains the type of cell for each index. Plot a scatter plot with the obtained two principal components, with different types of cell in different colours. What can you observe? Now plot another plot using two random columns of the original dataframe. Describe the difference in the two plots.

     **Answer**: After plotting, we can see that the same type of cell generally clustered together (in a gaussian cluster). When using two random columns, the same type of cells are usually separated. This shows that same type of cell will have similar principal components, and it is better at data visualization.

### Categorization using Gradient Descent

We now try to do predictions: given the amount of mRNA a cell produces, predict the type of cell. We can do this using logistic regression. To simplify the case, we split the data into two categories:

- B cell (1)
- non-B cell (0)

Split the dataset into two parts: 70% as training set and 30% as test set. We use only the training set to perform logistic regression

7. To simplify the case, we split the data into two categories. Find the type of cell that has the most data points.

     **Answer**: With

     ```python
     feature_df.groupBy('CITEsort').count().show()
     ```

     The result shows that `CD4+ T` is the type of cell that has the largest population.

     ```log
     +--------+-----+
     |CITEsort|count|
     +--------+-----+
     |  C-mono| 2313|
     |     mDC|  303|
     |  CD8+ T| 2035|
     |  B cell|  414|
     |     ACT| 2952|
     |     iNK|  113|
     | CD4+ DC|  166|
     |     mNK| 1057|
     |     DNT|  178|
     |  CD4+ T| 5262|
     | CD8+ DC|   81|
     | NC-mono|  537|
     +--------+-----+
     ```

8. We call this type be type A, and we split the dataset into two categories:

     - type A (labeled `1`)
     - non-type A (labeled `0`)

     To categorize this, we use `spark.mllib.classification.LogisticRegressionWithLBFGS` with the two principal components $p_1$ and $p_2$. Here the BFGS is an advanced version of gradient descent that utilizes quasi-newton method and Hessian matrix.

     Now, split the dataset into two parts: 70% as training set and 30% as test set. Try to use Logistic Regression with gradient descent on the training dataset, and use your model to predict the label in your test set. What is your findings? Propose ways to improve the model.

     **Answer**: During my experiment the error rate on the test set is 25.59% after 100 iterations. This is still large. Looking at the scatter plot, we can see that `CD4+ T` cell is very close to some other type of cells, making the result also reasonable. Ways of improving include introducing more principal components into the regression instead of only two principal components.
