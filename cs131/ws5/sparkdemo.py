import sys
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

spark = SparkSession.builder.appName("ws5-regression").getOrCreate()

df = spark.read.option("header", True).option("inferSchema", True).csv(sys.argv[1])
df.show()

assembler = VectorAssembler(inputCols=["total_bill", "size"], outputCol="features")

train, test = df.randomSplit([0.8, 0.2], seed=42)

lr = LinearRegression(featuresCol="features", labelCol="tip")
pipeline = Pipeline(stages=[assembler, lr])
pipelineModel = pipeline.fit(train)

predictions = pipelineModel.transform(test)

evaluator = RegressionEvaluator(labelCol="tip", predictionCol="prediction", metricName="rmse")
rmse = evaluator.evaluate(predictions)
evaluator.setMetricName("r2")
r2 = evaluator.evaluate(predictions)

lrModel = pipelineModel.stages[-1]
print(f"Coefficients: {lrModel.coefficients}")
print(f"Intercept: {lrModel.intercept}")
print(f"RMSE: {rmse}")
print(f"R2: {r2}")

spark.stop()