# tools.py

import ast
import operator
from datetime import datetime

from ddgs import DDGS
from langchain.tools import tool
from pydantic import BaseModel, Field


# ============================================================
# CALCULATOR
# ============================================================

class CalculatorInput(BaseModel):
    expression: str = Field(
        description=(
            "A mathematical expression using numbers, "
            "+, -, *, /, %, **, // and parentheses. "
            "Example: (10 + 20) * 5"
        )
    )


# Allowed mathematical operations
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.FloorDiv: operator.floordiv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def _calculate(node):

    # Number
    if isinstance(node, ast.Constant):

        if isinstance(node.value, (int, float)):
            return node.value

        raise ValueError("Invalid number.")

    # Binary operation
    if isinstance(node, ast.BinOp):

        left = _calculate(node.left)
        right = _calculate(node.right)

        operation = OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Operation not allowed.")

        return operation(left, right)

    # Positive / negative numbers
    if isinstance(node, ast.UnaryOp):

        value = _calculate(node.operand)

        operation = OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Operation not allowed.")

        return operation(value)

    raise ValueError("Invalid mathematical expression.")


@tool(args_schema=CalculatorInput)
def calculator(expression: str) -> str:
    """
    Perform mathematical calculations.

    Supports:
    addition (+)
    subtraction (-)
    multiplication (*)
    division (/)
    modulus (%)
    power (**)
    floor division (//)
    parentheses
    """

    try:

        expression = expression.strip()

        tree = ast.parse(expression, mode="eval")

        result = _calculate(tree.body)

        return str(result)

    except ZeroDivisionError:

        return "Error: Cannot divide by zero."

    except Exception:

        return "Error: Invalid mathematical expression."


# ============================================================
# WEB SEARCH
# ============================================================

class WebSearchInput(BaseModel):
    query: str = Field(
        description=(
            "The exact search query to search on the internet. "
            "Example: latest Nepal flood news"
        )
    )


@tool(args_schema=WebSearchInput)
def web_search(query: str) -> str:
    """
    Search the internet for current or recent information.

    Always provide the search query using the 'query' argument.
    Use this tool for latest news, current events, recent facts,
    and information that requires internet search.
    """

    if not query or not query.strip():
        return "Please provide a search query."

    try:

        search = DDGS()

        results = search.text(
            query=query,
            max_results=5
        )

        if not results:
            return "No search results found."

        output = []

        for result in results:

            title = result.get("title", "No title")
            url = result.get("href", "")
            description = result.get("body", "")

            output.append(
                f"Title: {title}\n"
                f"URL: {url}\n"
                f"Description: {description}"
            )

        return "\n\n".join(output)

    except Exception as e:

        return f"Web search failed: {str(e)}"


# ============================================================
# CURRENT TIME
# ============================================================

@tool
def get_current_time() -> str:
    """
    Return the current date and time.
    """

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


# ============================================================
# CELSIUS → FAHRENHEIT
# ============================================================

class CelsiusInput(BaseModel):
    celsius: float = Field(
        description="Temperature in Celsius."
    )


@tool(args_schema=CelsiusInput)
def celsius_to_fahrenheit(celsius: float) -> str:
    """
    Convert Celsius to Fahrenheit.
    """

    fahrenheit = (celsius * 9 / 5) + 32

    return f"{fahrenheit:.2f} °F"


# ============================================================
# FAHRENHEIT → CELSIUS
# ============================================================

class FahrenheitInput(BaseModel):
    fahrenheit: float = Field(
        description="Temperature in Fahrenheit."
    )


@tool(args_schema=FahrenheitInput)
def fahrenheit_to_celsius(fahrenheit: float) -> str:
    """
    Convert Fahrenheit to Celsius.
    """

    celsius = (fahrenheit - 32) * 5 / 9

    return f"{celsius:.2f} °C"


# ============================================================
# KILOMETERS → MILES
# ============================================================

class KilometerInput(BaseModel):
    kilometers: float = Field(
        description="Distance in kilometers."
    )


@tool(args_schema=KilometerInput)
def kilometers_to_miles(kilometers: float) -> str:
    """
    Convert kilometers to miles.
    """

    miles = kilometers * 0.621371

    return f"{miles:.3f} miles"


# ============================================================
# MILES → KILOMETERS
# ============================================================

class MileInput(BaseModel):
    miles: float = Field(
        description="Distance in miles."
    )


@tool(args_schema=MileInput)
def miles_to_kilometers(miles: float) -> str:
    """
    Convert miles to kilometers.
    """

    kilometers = miles * 1.609344

    return f"{kilometers:.3f} km"


# ============================================================
# TEXT ANALYZER
# ============================================================

class TextInput(BaseModel):
    text: str = Field(
        description="The text that should be analyzed."
    )


@tool(args_schema=TextInput)
def analyze_text(text: str) -> str:
    """
    Analyze text and return word, character and sentence counts.
    """

    words = len(text.split())
    characters = len(text)

    sentences = sum(
        1 for character in text
        if character in ".!?"
    )

    return (
        f"Words: {words}\n"
        f"Characters: {characters}\n"
        f"Sentences: {sentences}"
    )


# ============================================================
# ALL TOOLS
# ============================================================

tools = [
    calculator,
    web_search,
    get_current_time,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kilometers_to_miles,
    miles_to_kilometers,
    analyze_text
]