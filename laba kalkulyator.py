from fastapi import FastAPI
import pyjokes
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def kalkulyator(znach1: int, znach2: int, operation: str):
    if operation == "+":
        return znach1 + znach2

    if operation == "-":
        return znach1 - znach2

    if operation == "*":
        return znach1 * znach2

    if (operation == "/") and (znach2 == 0):
        return "На ноль делить нельзя"

    if operation == "/":
        return znach1 / znach2
    if operation == "**":
        return znach1**znach2
