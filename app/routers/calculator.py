from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Calculation(BaseModel):
    num1: float
    num2: float
    operation: str


@router.post("/calculate")
def calculate(calc: Calculation):
    if calc.operation == "add":
        result = calc.num1 + calc.num2
    elif calc.operation == "subtract":
        result = calc.num1 - calc.num2
    elif calc.operation == "multiply":
        result = calc.num1 * calc.num2
    elif calc.operation == "divide":
        if calc.num2 == 0:
            return {"error": "Cannot divide by zero"}
        result = calc.num1 / calc.num2
    else:
        return {"error": "Invalid operation"}

    return {"result": result}
