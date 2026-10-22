# Databricks notebook source
# MAGIC %md
# MAGIC ## Read Excel wtih Default Options

# COMMAND ----------

df=spark.read.excel("/Volumes/training/my_volume/my_volume/excel_input_files/")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Use Headers and Infer Schema

# COMMAND ----------

df=spark.read.\
  option("headerRows", 1).\
  excel("/Volumes/training/my_volume/my_volume/excel_input_files/")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Provide custom sheet name and data range

# COMMAND ----------

df=spark.read.\
  option("headerRows", 1).\
      option("dataAddress", "transactions!D11:M111").\
  excel("/Volumes/training/my_volume/my_volume/excel_input_files/")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## List name of all sheets

# COMMAND ----------

df=spark.read.\
  option("operation", "listSheets").\
  excel("/Volumes/training/my_volume/my_volume/excel_input_files/")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Add File name along with Sheet Name

# COMMAND ----------

df = spark.read.\
  option("operation", "listSheets").\
  excel("/Volumes/training/my_volume/my_volume/excel_input_files/")

df = df.withColumn("filename", df["_metadata"]["file_name"])
display(df)