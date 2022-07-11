# Databricks notebook source
display(dbutils.fs.ls('/databricks-datasets'))

# COMMAND ----------

f = open('/dbfs/databricks-datasets/README.md', 'r')
print(f.read())

# COMMAND ----------

display(dbutils.fs.ls('dbfs:/'))

# COMMAND ----------

dbutils.fs.mkdirs("/foobar/")

# COMMAND ----------

dbutils.fs.put("/foobar/baz.txt", "Hello, World!")

# COMMAND ----------

dbutils.fs.head("/foobar/baz.txt")

# COMMAND ----------

dbutils.fs.rm("/foobar/baz.txt")

# COMMAND ----------

# MAGIC %scala
# MAGIC dbutils.fs.rm("/foobar")

# COMMAND ----------

# MAGIC %run ./Filter-baby-names

# COMMAND ----------


