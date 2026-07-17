# Databricks notebook source
# COMMAND ----------
# Module 12 Lab 1 - Git Branching Strategy Setup

dbutils.widgets.text("environment", "dev")
dbutils.widgets.text("enable_strict_validation", "false")

environment = dbutils.widgets.get("environment")
enable_strict_validation = dbutils.widgets.get("enable_strict_validation")

print(f"Running in environment: {environment}")
print(f"Strict validation enabled: {enable_strict_validation}")

# COMMAND ----------
# Feature flag example

if enable_strict_validation.lower() == "true":
    print("Strict validation path enabled.")
else:
    print("Standard validation path enabled.")
