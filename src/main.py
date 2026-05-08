from fastapi import FastAPI
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
    def division(self) -> float:
        if self.n2 == 0:
            raise ValueError("Undefined")
        else:
            return self.n1 / self.n2

# Endpoints
@app.post("/calculator/add", response_model=CalculationResult)
def add_numbers(input_data: NumberInput):
    calc = Calculator(input_data.a, input_data.b)
    res = calc.add()
    return CalculationResult(result=res)

@app.post("/calculator/subtract", response_model=CalculationResult)
def subtract_numbers(input_data: NumberInput):
    calc = Calculator(input_data.a, input_data.b)
    res = calc.subtract()
    return CalculationResult(result=res)

@app.post("/calculator/multiply", response_model=CalculationResult)
def multiply_numbers(input_data: NumberInput):
    calc = Calculator(input_data.a, input_data.b)
    res = calc.multiply()
    return CalculationResult(result=res)

@app.post("/calculator/division", response_model=CalculationResult)
def divide_numbers(input_data: NumberInput):
    calc = Calculator(input_data.a, input_data.b)
    res = calc.division()
    return CalculationResult(result=res)
