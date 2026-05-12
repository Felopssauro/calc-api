from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class NumberInput(BaseModel):
    a: int
    b: int

class CalculationResult(BaseModel):
    result: float

class Calculator:
    def __init__(self, n1: int, n2: int):
        self.n1 = n1
        self.n2 = n2
    def add(self) -> int:
        return self.n1 + self.n2
    def subtract(self) -> int:
        return self.n1 - self.n2
    def multiply(self) -> int:
        return self.n1 * self.n2
    def divide(self) -> float:
        if self.n2 == 0:
            raise HTTPException(status_code=400, detail="Undefined. You can't divide by zero.")
        else:
            return self.n1 / self.n2

# Endpoints
@app.post("/calculator/add", response_model=CalculationResult)
def add_numbers(input_data: NumberInput):
    calculate = Calculator(input_data.a, input_data.b)
    summation = calculate.add()
    return CalculationResult(result=summation)

@app.post("/calculator/subtract", response_model=CalculationResult)
def subtract_numbers(input_data: NumberInput):
    calculate = Calculator(input_data.a, input_data.b)
    difference = calculate.subtract()
    return CalculationResult(result=difference)

@app.post("/calculator/multiply", response_model=CalculationResult)
def multiply_numbers(input_data: NumberInput):
    calculate = Calculator(input_data.a, input_data.b)
    product = calculate.multiply()
    return CalculationResult(result=product)

@app.post("/calculator/divide", response_model=CalculationResult)
def divide_numbers(input_data: NumberInput):
    calculate = Calculator(input_data.a, input_data.b)
    quotient = calculate.divide()
    return CalculationResult(result=quotient)
