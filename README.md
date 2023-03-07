# Project Toxic Prediction with Detoxify
## Get started
Clone this github repo
```
git clone https://github.com/chihovn/toxic-prediction-with-Detoxify.git
```

Install requirement
```
pip install -r requirements.txt
```
Replace __ and run code
```
# Window
python run_prediction -- mode __ --input_path __ --save_to __ -- model_name __

# Linux
python3 run_prediction -- mode __ --input_path __ --save_to __ -- model_name __

```
## Argument list
### --mode
We have 2 modes:
- Mode "qa": get input and return output score in terminal.If you choose 'qa' mode, don't need to fill --input_path and --save_to arguments.
- Mode "csv": input and output in csv format.

### --input_path
path of input csv file if mode csv

### --save_to
path of output csv file if mode csv

### --model_name
This project works with 3 model: "original" and "unbiased".

##Example
```
python run_prediction.py --mode csv --input_path example.csv --save_to ./results/unbiased_result.csv --model_name unbiased
```

## Log info
All information when running this project will be logged in "log/log.txt"

