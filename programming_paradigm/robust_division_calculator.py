def safe_divide(numerator,demoninator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator / denominator

        return f"The result is: {result}"
    except ZeroDivisionError:
        return "Please try a number other than zero."
    except ValueError:
        return "Please used a integer or float value."

