import pandas as pd
import great_expectations as gx

df = pd.read_csv("Pokemon.csv", index_col = "Name")

# removing the column # and cleaning data
df = df.drop(columns = ["#"])
df = df.dropna()
print(df.shape)

print(df["Attack"].min())

# set up the data context GX environment
context = gx.get_context()

# Connect to the data source DATA SOURCE --> DATA ASSETS --> BATCH DEFINITION --> DATA BATCH. The Pandas DataFrame is provided to the Batch Definition at runtime to create the Batch.
data_source = context.data_sources.add_pandas("pandas")
data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")
batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

#Create an Expectation.
#Expectations are a fundamental component of GX. They allow you to explicitly define the state to which your data should conform.
#Run the following code to define an Expectation that the contents of the column Attack consist of values ranging from x to y:
expectation = gx.expectations.ExpectColumnValuesToBeBetween(
    column="Attack", min_value=11, max_value=150
)

#Run and get the results!
validation_result = batch.validate(expectation)

print(validation_result)