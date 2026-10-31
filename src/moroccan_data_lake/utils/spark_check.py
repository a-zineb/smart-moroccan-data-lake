from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("____")
    .master("local[*]")
    .getOrCreate()
)

cities = [
        ("Rabat", 34.02, -6.83),
    ("Casablanca", 33.57, -7.59),
    ("Marrakech", 31.63, -8.01),
]

df = spark.createDataFrame(cities, ["city", "latitude", "longitude"])
df.show()

spark.stop()