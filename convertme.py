import streamlit as st
from be_main import UnitConverter
from base_conv import BaseConverter
import pandas as pd
from datetime import datetime
import os
from BAC import BAC
import numpy as np
import matplotlib.pyplot as plt
from morse import text_to_morse, morse_to_text

st.set_page_config(
    page_title="CONGEN ToolBox",
    page_icon="CONGEN.png",
    layout="centered"
)
st.title("CONGEN ToolBox : Unit Converter (v1.0.3)", anchor="center")
st.write("Convert between various units of measurement.")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Unit Conversion", "Base Conversion", "BAC Calculator", "Morse Code","About & Feedback"])


with tab1:
    st.header("Unit Conversion")
    conversion_options = {
        "Celsius to Fahrenheit": UnitConverter.celsius_to_fahrenheit,
        "Fahrenheit to Celsius": UnitConverter.fahrenheit_to_celsius,
        "Celsius to Kelvin": UnitConverter.celsius_to_kelvin,
        "Kelvin to Celsius": UnitConverter.kelvin_to_celsius,
        "Fahrenheit to Kelvin": UnitConverter.fahrenheit_to_kelvin,
        "Kelvin to Fahrenheit": UnitConverter.kelvin_to_fahrenheit,
        "Meters to Feet": UnitConverter.meters_to_feet,
        "Feet to Meters": UnitConverter.feet_to_meters,
        "Kilometers to Miles": UnitConverter.kilometers_to_miles,
        "Miles to Kilometers": UnitConverter.miles_to_kilometers,
        "Kilograms to Pounds": UnitConverter.kilograms_to_pounds,
        "Pounds to Kilograms": UnitConverter.pounds_to_kilograms
    }

    option = st.selectbox("Select conversion type:", list(conversion_options.keys()))
    a = st.slider("Till how many decimal places you want the output? (0-6)", min_value=0, max_value=6, value=2)
    input_value = st.number_input("Enter value to convert:", format=f"%.{a}f")

    if st.button("Convert Unit"):
        try:
            conversion_function = conversion_options[option]
            result = conversion_function(input_value)
            st.success(f"Converted value: {result:.{a}f}")
        except Exception as e:
            st.error(f"Error during conversion: {e}")

with tab2:
    st.header("Base Conversion")
    base_conversion_options = {
        "Decimal to Binary": BaseConverter.decimal_to_binary,
        "Binary to Decimal": BaseConverter.binary_to_decimal,
        "Decimal to Hexadecimal": BaseConverter.decimal_to_hexadecimal,
        "Hexadecimal to Decimal": BaseConverter.hexadecimal_to_decimal,
        "Binary to Hexadecimal": BaseConverter.binary_to_hexadecimal,
        "Hexadecimal to Binary": BaseConverter.hexadecimal_to_binary,
        "Decimal to Octal": BaseConverter.decimal_to_octal,
        "Octal to Decimal": BaseConverter.octal_to_decimal,
        "Binary to Octal": BaseConverter.binary_to_octal,
        "Octal to Binary": BaseConverter.octal_to_binary,
        "Hexadecimal to Octal": BaseConverter.hexadecimal_to_octal,
        "Octal to Hexadecimal": BaseConverter.octal_to_hexadecimal
    }

    base_option = st.selectbox("Select base conversion type:", list(base_conversion_options.keys()))
    input_value_base = st.text_input("Enter the value to convert:")
    st.caption("For binary: use only 0 and 1 | Hex: 0-9 A-F | Octal: 0-7 | Decimal: non-negative integers")

    if st.button("Convert Base"):
        try:
            base_conversion_function = base_conversion_options[base_option]
            result_base = base_conversion_function(input_value_base)
            st.success(f"Converted value: {result_base}")
        except Exception as e:
            st.error(f"Error Occured: {e}")

with tab3:
    st.header("Blood Alcohol Content (BAC) Calculator")
    st.markdown("Calculate your estimated Blood Alcohol Content (BAC) based on your drink intake and personal characteristics.")
    weight = st.number_input("Enter your weight (in kg):", min_value=20.0, max_value=300.0)
    gender = st.selectbox("Gender:", ["Male", "Female"])
    alcohol_percent = st.number_input("Alcohol Percentage of Drink (%):", min_value=0.1, max_value=100.0)
    volume = st.number_input("Volume of each drink (in Litres):", min_value=0.01, max_value=6.0)
    st.caption("E.g., 0.33L for a standard beer bottle, 0.15L for a glass of wine, 0.044L for a shot of spirits.")
    quantity = st.number_input("Number of drinks consumed:", min_value=0.1, max_value=40.0)
    hours = st.number_input("Hours since last drink:", min_value=0.0, max_value=48.0)

    show_graph = st.checkbox("Show BAC Level Graph overtime since last drink(Approx.)")

    if st.button("Calculate BAC"):
        try:
            user = BAC(weight=weight, gender=gender)
            bac_result = user.calculate_bac(alc_percent=alcohol_percent, volume=volume, quantity=quantity, hours=hours)
            st.success(f"Estimated BAC: {bac_result:.4f}%")

            if bac_result < 0.03:
                st.success("You are likely sober.")
            elif 0.03 <= bac_result < 0.08:
                st.warning("Mild impairment. Caution advised.")
            elif 0.08 <= bac_result < 0.15:
                st.error("Legally impaired. Do not drive.")
            else:
                st.error("Severe impairment. Seek medical attention if necessary.")

            if show_graph:

                time_points = np.linspace(hours, hours + 24, 100)
                bac_values = [user.calculate_bac(alcohol_percent, volume, quantity, t) for t in time_points]

                plt.figure(figsize=(10, 5))
                plt.plot(time_points, bac_values, label='Estimated BAC', color='blue')
                plt.axhline(y=0.08, color='red', linestyle='--', label='Legal Limit (0.08%)')
                plt.axhline(y=0.03, color='orange', linestyle='--', label='Sober Limit (0.03%)')
                plt.xlabel('Hours since last drink')
                plt.ylabel('Estimated BAC (%)')
                plt.title('Estimated BAC Level Over Time')
                plt.legend()
                plt.grid(True)
                plt.tight_layout()
                st.pyplot(plt)

                st.caption("NOTE: This graph is an approximation [Average metabolism rate: (~0.015% BAC reduction per hour)] and should not be used to absolutely determine fitness to drive or operate machinery. " \
                "Individual metabolism rates vary.")

        except Exception as e:
            st.error(f"Error in BAC calculation (Please enter the details correctly): {e}")
                
with tab4:
    st.header("Morse Code Converter")
    st.markdown("Convert text to Morse code and vice-versa.")
    morse_option = st.selectbox("Select conversion type:", ["Text to Morse", "Morse to Text"])
    input_label = "Enter the value to convert:" if morse_option == "Text to Morse" else "Enter the Morse code to convert:"
    input_value_morse = st.text_area(input_label, height=100)
    st.caption("For Morse to Text: Separate Morse characters with spaces and words with '/'. E.g., .... . .-.. .-.. --- / .-- --- .-. .-..")
    if morse_option == "Text to Morse":
        if st.button("Convert to Morse"):
            try:
                morse_result = text_to_morse(input_value_morse)
                st.success(f"Morse Code: {morse_result}")
            except Exception as e:
                st.error(f"Error Occured: {e}")
    else:
        if st.button("Convert to Text"):
            try:
                text_result = morse_to_text(input_value_morse)
                st.success(f"Text: {text_result}")
            except Exception as e:
                st.error(f"Error Occured: {e}")


def clear_feedback():
    st.session_state.feedback_text = ""

with tab5:
    st.header("About & Feedback")
    st.markdown("""
    **CONGEN ToolBox** is a reliable, user-friendly web app that converts between a wide range of physical units and number bases quickly and accurately.

    ### Features
    - Temperature, length, weight, volume, area, pressure, and energy unit conversions.  
    - Binary, octal, decimal, and hexadecimal base conversions.  
    - Custom decimal precision for unit results.  
    - Clear input validation and error handling.  

    ### Accessing the App
    The app is hosted online and publicly accessible via a web browser. No installation or technical knowledge is needed — simply visit the deployed URL to start converting.

    ### Deployment
    This app is designed for deployment on platforms like Render.com or Streamlit Cloud, ensuring continuous availability and accessibility.

    *If you would like private access or to discuss permissions for the source code, please contact the maintainer via feedback form.*

    ### Feedback
    Any sort of feedback for reporting bugs, suggesting ideas and collaboration will be highly appreciated.

    ### Note
    This project was created purely for fun and as a way to learn Python. If demand or traffic grows, future updates and improvements will definitely be considered.

    Built for accuracy and ease of use — your trusted conversion toolbox.
    """)

    feedback = st.text_area("Your Feedback / Suggestions: (Anything helps!)", height=150, key="feedback_text")

    def save_feedback(feedback_text):
        df = pd.DataFrame([{
            "timestamp": datetime.now().isoformat(),
            "feedback": feedback_text
        }])
        file_exists = os.path.isfile("feedback.csv")
        df.to_csv("feedback.csv", mode="a", header=not file_exists, index=False)

    if st.button("Submit Feedback"):
        if feedback.strip():
            save_feedback(feedback)
            st.success("Thank you for your feedback!")
            st.info(f"Saved feedback:\n\n{feedback}")
            clear_feedback()
        else:
            st.error("Please write something before submission...")



