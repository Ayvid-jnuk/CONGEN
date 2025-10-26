import streamlit as st
from be_main import UnitConverter
from base_conv import BaseConverter
import pandas as pd
from BAC import BAC
import numpy as np
import matplotlib.pyplot as plt
from morse import text_to_morse, morse_to_text
from BMI import bmi_estimator 
from calorie import calorie_estimator
from hydration import hydration_estimator
from bencode import bencode_encode, bencode_decode
from caesar import caesar_cipher
from wscraper import scrape_website
from bodyweight import evaluate_weight
import ast


st.set_page_config(
    page_title="CONGEN ToolBox",
    page_icon="CONGEN.png",
    layout="centered"
)
st.title("CONGEN : GSMA ToolBox (v1.0.7)", anchor="center")
st.write("Access various tools easily...")

section = st.sidebar.radio("Select Tool:", ["General Tools", "Security Tools", "Monitor Tools", "Advance Tools", "About & Feedback"])

if section == "General Tools":
    st.sidebar.success("You are in the General Tools section...")
    tab1, tab2, tab3, tab4 = st.tabs(["Unit Conversion", "Base Conversion", "Morse Code", "Bencode"])


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
        units_map = {
            "Celsius to Fahrenheit": ("°C", "°F"),
            "Fahrenheit to Celsius": ("°F", "°C"),
            "Celsius to Kelvin": ("°C", "K"),
            "Kelvin to Celsius": ("K", "°C"),
            "Fahrenheit to Kelvin": ("°F", "K"),
            "Kelvin to Fahrenheit": ("K", "°F"),
            "Meters to Feet": ("m", "ft"),
            "Feet to Meters": ("ft", "m"),
            "Kilometers to Miles": ("km", "mi"),
            "Miles to Kilometers": ("mi", "km"),
            "Kilograms to Pounds": ("kg", "lbs"),
            "Pounds to Kilograms": ("lbs", "kg")
        }

        option = st.selectbox("Select conversion type:", list(conversion_options.keys()))
        input_unit, output_unit = units_map[option]
        a = st.slider("Till how many decimal places you want the output? (0-6)", min_value=0, max_value=6, value=2)
        input_value = st.number_input(f"Enter value to convert: {input_unit}", format=f"%.{a}f")

        if st.button("Convert Unit"):
            try:
                conversion_function = conversion_options[option]
                result = conversion_function(input_value)
                st.success(f"Converted value: {result:.{a}f} {output_unit}")
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
        st.info("Only positive integers are supported")
        st.caption("For binary: use only 0 and 1 | Hex: 0-9 A-F | Octal: 0-7 | Decimal: non-negative integers")

        if st.button("Convert Base"):
            try:
                base_conversion_function = base_conversion_options[base_option]
                result_base = base_conversion_function(input_value_base)
                st.success(f"Converted value: {result_base}")
            except Exception as e:
                st.error(f"Error Occured: {e}")

                
    with tab3:
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
    
    with tab4:
        st.header("Bencode : Encode & Decode")
        st.markdown("""
                    **Bencode** is a simple encoding protocol used primarily on .torrent files for storing and sharing files over peer-to-peer networks. \n
                    It supports four data types: \n
                        - Integers: Encoded as 'i<integer>e'. E.g., i42e represents the integer 42. \n
                        - Strings: Encoded as '<length>:<string>'. E.g., 6:congen represents the string "congen". \n
                        - Lists: Encoded as 'l<item1><item2>...e'. E.g., l4:spam4:eggse represents the list ["spam", "eggs"]. \n
                        - Dictionaries: Encoded as 'd<key1><value1><key2><value2>...e'. E.g., d3:cati42e3:dogi43ee represents the dictionary {"cat": 42, "dog": 43}. \n
                    
                    Bencoding is designed to be simple and efficient, making it suitable for use in distributed systems like BitTorrent. \n
                    *Use this tool to easily encode/decode data using the Bencode format.*
                    """)
        bencode_option = st.selectbox("Select operation:", ["Encode Data", "Decode Data"])
        if bencode_option == "Encode Data":
            input_data = st.text_area("Enter the data to encode (Use Python syntax for lists and dictionaries):", height=150)
            st.caption("E.g., For list: ['spam', 'eggs'] | For dict: {'cat': 42, 'dog': 43} | For string: 'congen' | For integer: 42")
            if st.button("Encode"):
                try:
                    parsed_data = ast.literal_eval(input_data)                  
                    encoded_result = bencode_encode(parsed_data)
                    st.success("Encoded Bencode: ")
                    st.code(encoded_result, language="text")
                except Exception as e:
                    st.error(f"Error Occured: {e}")
        
        elif bencode_option == "Decode Data":
            input_bencode = st.text_area("Enter the Bencode string to decode:", height=150)
            st.caption("E.g., i42e | 6:congen | l4:spam4:eggse | d3:cati42e3:dogi43ee")
            if st.button("Decode"):
                try:
                    decoded_result = bencode_decode(input_bencode)
                    st.success("Decoded Data: ")
                    st.json(decoded_result)
                except Exception as e:
                    st.error(f"Error Occured: {e}")



elif section == "Security Tools":
    st.sidebar.success("You are in the Security Tools section...")
    tab1 = st.tabs(["Caesar Cipher"])

    with tab1[0]:
        st.header("Caesar Cipher")
        st.markdown("Encrypt or decrypt text using the Caesar cipher technique.")
        caesar_option = st.selectbox("Select operation:", ["Encrypt", "Decrypt"])
        input_text = st.text_area("Enter the text:", height=150)
        shift_value = st.number_input("Enter the shift value (integer):", min_value=1, max_value=25, value=3)
        
        if caesar_option == "Encrypt":
            if st.button("Encrypt Text"):
                try:
                    encrypted_text = caesar_cipher(input_text, shift_value, mode='encrypt')
                    st.success("Encrypted Text:")
                    st.code(encrypted_text, language="text")
                except Exception as e:
                    st.error(f"Error Occured: {e}")
        else:
            if st.button("Decrypt Text"):
                try:
                    decrypted_text = caesar_cipher(input_text, shift_value, mode='decrypt')
                    st.success("Decrypted Text:")
                    st.code(decrypted_text, language="text")
                except Exception as e:
                    st.error(f"Error Occured: {e}")


elif section == "Monitor Tools":
    st.sidebar.success("You are in the Monitor Tools section...")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["BAC Calculator", "BMI Calculator", "Calorie Estimator", "Hydration Estimator", "Body Weight Tracker"])

    with tab1:
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
    
    with tab2:
        st.header("Body Mass Index(BMI) Calculator")
        st.markdown("Calculate your Body Mass Index (BMI) based on your height and weight.")

        height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=350.0, key="bmi_height")
        weight = st.number_input("Enter your weight (in kg):", min_value=5.0, max_value=500.0, key="bmi_weight")
        if st.button("Calculate BMI"):
            try:
                bmi_data = bmi_estimator(weight_kg=weight, height_cm=height)
                if "error" in bmi_data:
                    st.error(bmi_data["error"])
                else:
                    st.success(f"Your BMI is: {bmi_data['bmi']}")
                    st.info(f"BMI Category: {bmi_data['category']}")
            except Exception as e:
                st.error(f"Error in BMI calculation (Please enter the details correctly): {e}")


    with tab3:
        st.header("Calorie Estimator")
        st.markdown("Estimate your daily calorie needs based on your activity level and personal characteristics.")

        weight = st.number_input("Enter your weight (in kg):", min_value=5.0, max_value=500.0, key="calorie_weight")
        height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=350.0, key="calorie_height")
        age = st.number_input("Enter your age (in years):", min_value=1.0, max_value=120.0, key="calorie_age")
        gender = st.selectbox("Gender:", options = ["Male", "Female"], key="calorie_gender")

        if st.button("Estimate Calories"):
            try:
                calorie_data = calorie_estimator(weight_kg=weight, height_cm=height, age=age, gender=gender)
                if "error" in calorie_data:
                    st.error(calorie_data["error"])
                else:
                    st.success(f"Your estimated Basal Metabolic Rate (BMR) is: {calorie_data['bmr']} calories/day")
                    st.info("This is the number of calories your body needs at rest to maintain basic physiological functions.")
            except Exception as e:
                st.error(f"Error in calorie estimation (Please enter the details correctly): {e}")

    with tab4:
        st.header("Hydration Estimator")
        st.markdown("Estimate your daily water intake needs based on your activity level and personal characteristics.")

        weight = st.number_input("Enter your weight (in kg):", min_value=5.0, max_value=500.0, key="hydration_weight")
        age = st.number_input("Enter your age (in years):", min_value=1.0, max_value=120.0, key="hydration_age") 
        gender = st.selectbox("Gender:", options=["Male", "Female"], key="hydration_gender")
        activity_level = st.selectbox("Activity Level:", ["Low", "Moderate (some physical activity)", "High (intense physical activity)"])

        if st.button("Estimate Hydration"):
            try:
                hydration_data = hydration_estimator(weight_kg=weight,
                                                        age=age,
                                                        gender=gender,
                                                        activity_level=activity_level)
                if "error" in hydration_data:
                    st.error(hydration_data["error"])
                else:
                    st.success(f"Your estimated daily water intake is: {hydration_data['water_intake_liters']} liters/day")
                    st.info("This is the recommended amount of water to stay adequately hydrated based on your inputs.")
            except Exception as e:
                st.error(f"Error in hydration estimation (Please enter the details correctly): {e}")
    with tab5:
        st.header("Body Weight Tracker")
        st.markdown("""
                    ### Keen on losing or gaining weight?  

                    Enter a few personal traits to:  

                        - Check if your desired weight is healthy for your height.  
                        - Get a recommended weight range for your height.  
                        - Visualize your weight progress over time with a simple graph.  
                        - Receive simple diet advice to reach your goals.  
                    """)
        st.info("Note: This is a basic weight tracker and does not replace professional medical advice.")

        height = st.number_input("Enter your height (in m):", min_value=0.1, max_value=350.0, key="tracker_height")
        current_weight = st.number_input("Enter your current weight (in kg):", min_value=1.0, max_value=500.0, key="tracker_current_weight")
        desired_weight = st.number_input("Enter your desired weight (in kg):", min_value=1.0, max_value=500.0, key="tracker_desired_weight")
        current_age = st.number_input("Enter your age (in years):", min_value=1.0, max_value=120.0, key="tracker_age")
        user_gender = st.selectbox("Gender:", options=["Male", "Female"], key="tracker_gender")
        if user_gender == "Female" and current_age >= 21:
            pregnancy = st.selectbox("Are you pregnant?", options=["Yes", "No"], key="tracker_pregnancy")
        else:
            pregnancy = "No"
        activity_level = st.selectbox("Activity Level:", ["Low", "Moderate", "High", "Extreme"], key="tracker_activity_level")

        if st.button("Evaluate Weight"):
            results = evaluate_weight(height=height,
                                      current_weight=current_weight,
                                      desired_weight=desired_weight,
                                      age=current_age,  
                                      gender=user_gender,
                                      activity_level=activity_level,
                                      pregnancy=pregnancy)
            
            st.subheader("ANALYSIS RESULTS: ")
            st.write(f"**Current BMI:** {results['current_bmi']:.2f} ({results['current_status']})")
            st.write(f"**Desired BMI:** {results['desired_bmi']:.2f} ({results['desired_status']})")
            st.write(f"**Healthy Weight Range for your Height:** {results['healthy_range'][0]:.2f} kg - {results['healthy_range'][1]:.2f} kg")
            st.write(f"**Basal Metabolic Rate (BMR):** {results['bmr']:.2f} calories/day")
            st.write(f"**Total Daily Energy Expenditure (TDEE):** {results['tdee']:.2f} calories/day")
            st.write(f"**Diet Tips:** {results['tips']}")

            st.subheader("Weight Progress Graph:")
            st.info("Available soon in the next version...")
            # x_vals, y_vals = results['graph_data']
            # plt.figure(figsize=(10, 5))
            # plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='green')
            # plt.xlabel('Days')
            # plt.ylabel('Weight (kg)')
            # plt.title('Estimated Weight Progress Over 90 Days')
            # plt.grid(True)
            # st.pyplot(plt)


elif section == "Advance Tools":
    st.sidebar.success("You are in the Advance Tools section...")
    tab1 = st.tabs(["Web Scraper"])
    with tab1[0]:
        st.header("Web Scraper")
        st.markdown("This tool allows you to scrape and extract data from web pages. Enter a URL to fetch and display its content.")
        st.warning("Note: Ensure you have permission to scrape the target website and comply with its terms of service.")

        url = st.text_input("Enter the URL of the webpage to scrape:", "https://")

        st.text("Select the type of data to extract:")
        title_checkbox = st.checkbox("Page Title", value=True)
        headings_checkbox = st.checkbox("Headings (H1-H6)")
        paragraphs_checkbox = st.checkbox("Paragraphs")
        links_checkbox = st.checkbox("Links")
        images_checkbox = st.checkbox("Images")

        if st.button("Scrape Webpage"):
            try:
                results = []
                if title_checkbox:
                    title_result = scrape_website(url, "Title")
                    results.append(f"### Page Title:\n{title_result}\n")

                if headings_checkbox:
                    headings_result = scrape_website(url, "All Headings (H1-H6)")
                    results.append(f"### Headings:\n{headings_result}\n")

                if paragraphs_checkbox:
                    paragraphs_result = scrape_website(url, "All Paragraphs")
                    results.append(f"### Paragraphs:\n{paragraphs_result}\n")

                if links_checkbox:
                    links_result = scrape_website(url, "All Links")
                    results.append(f"### Links:\n{links_result}\n")

                if images_checkbox:
                    images_result = scrape_website(url, "Images")
                    results.append(f"### Images:\n{images_result}\n")

                if results:
                    st.markdown("\n---\n".join(results))
                else:
                    st.info("Please select at least one data type to extract.")

            except Exception as e:
                st.error(f"Error during web scraping: {e}")

elif section == "About & Feedback":
    st.header("About & Feedback")
    st.markdown("""
    :red[**CONGEN ToolBox**] is a reliable, user-friendly web app that contains various tools for daily use, advance use or dev use.
    :green[### Features]
    - Structured section-based navigation via sidebar for easy access to different tools.
    - Temperature, length, weight, volume, area, pressure, and energy unit conversions.  
    - Binary, octal, decimal, and hexadecimal base conversions. 
    - Bencode : Encode & Decode.
    - Blood Alcohol Content (BAC) calculator based on user's personal inputs with *visuals*.
    - BMI, Calorie and Hydration Calculator.
    - Morse code translator (text to Morse and vice-versa).  
    - Intuitive interface with easy-to-use dropdowns and input fields. 
    - Custom decimal precision for unit results.  
    - Clear input validation and error handling.  

    :green[### Accessing the App]
    The app is hosted online and publicly accessible via a web browser. No installation or technical knowledge is needed — simply visit the deployed URL to start converting.

    :green[### Deployment]
    This app is designed for deployment on platforms like Render.com or Streamlit Cloud, ensuring continuous availability and accessibility.

    *If you would like access or discuss permissions for the source code, please contact the developer via email: dbar0052@student.monash.edu.*

    :green[### Feedback]
    I am a first-year student and this is one of my first projects I've launched publicly.
    Any sort of feedback for reporting bugs, suggesting ideas and collaboration will be highly appreciated.

    :green[### Note]
    This project was created purely for fun and as a way to learn Python. If it gains traction, I would love to continue improving and expanding it.

    Built for accuracy and ease of use — your trusted conversion toolbox.
    """)




