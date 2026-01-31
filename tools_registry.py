from tools.calculator import add_numbers,mul_numbers
from tools.sentiment_tool import analyze_sentiment
TOOLS={
    "calculator":{
        "function": add_numbers,
        "expected_feilds":["a","b"]
    },
    "multiply":{
        "function":mul_numbers,
        "expected_feilds":["a","b"]
    },
    "sentiment":{
        "function": analyze_sentiment,
        "expected_feild":["text"]
    }
}