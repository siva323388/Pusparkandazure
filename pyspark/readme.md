# PySpark
**Use Google Colab to create a notebook and install spark**

1. Open Google Colab
```
https://colab.research.google.com
```
2. Create a new notebook, In the first code cell copy and paste the below code and execute it

**Note:** This will install spark in the current session.


```
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q https://archive.apache.org/dist/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
!tar xf spark-3.5.0-bin-hadoop3.tgz

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.5.0-bin-hadoop3"


!pip install -q findspark
import findspark

findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark DataFrame Example") \
    .getOrCreate()
sc = spark.sparkContext
sc
```
