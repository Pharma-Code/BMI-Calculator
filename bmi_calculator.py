import sys
import os

def main():
    #Display Title and Usage Texts
    print("Pharma-Code: BMI Calculator")
    print("Input the Weight (kg) and the Height (m) to calculate the BMI")

    #Receive Inputs
    weight = input("Input the Weight (kg): ")
    height = input("Input the Height (m): ")

    #Convert Inputs to Numerical Formats
    weight = convert_to_float(weight)
    height = convert_to_float(height)

    #Calculate BMI
    bmi = calculate_bmi(weight, height)
    bmi_category = get_bmi_category(bmi)

    #Display Result
    print("BMI: " + str(bmi))
    print("BMI Category: " + bmi_category)
    os.system("PAUSE")

def convert_to_float(value: str) -> float:
    try:
        return float(value)
    except:
        print("Invalid Input. Please, input numbers only.")
        sys.exit()

def calculate_bmi(weight: float, height: float) -> float:
    bmi = weight / height ** 2
    bmi = round(bmi, 1)
    return bmi

def get_bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    main()
