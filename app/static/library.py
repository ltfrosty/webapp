from org.transcrypt.stubs.browser import *
import random

def on_sliderchange(slider_id, textinput_id):
    """
    Syncs the value of a text input with a slider.

    Parameters:
    slider_id (str): The ID of the slider element.
    textinput_id (str): The ID of the text input element.
    """
    slider = document.getElementById(slider_id)
    textinput = document.getElementById(textinput_id)
    textinput.value = slider.value

def on_input(textinput_id, slider_id):
    """
    Syncs the value of a slider with a text input.

    Parameters:
    textinput_id (str): The ID of the text input element.
    slider_id (str): The ID of the slider element.
    """
    textinput = document.getElementById(textinput_id)
    slider = document.getElementById(slider_id)
    slider.value = textinput.value

def dd_onchange():
    """
    Resets all text inputs and sliders to 0 and clears the predicted yield.
    """
    text_inputs = document.getElementsByClassName("text_input")
    for text_input in text_inputs:
        text_input.value = 0
    sliders = document.getElementsByClassName("slider")
    for slider in sliders:
        slider.value = 0

    document.getElementById("predicted").innerHTML = ""

def normalise(feature_value, mean, std):
    """
    Normalizes a feature value using the provided mean and standard deviation.

    Parameters:
    feature_value (float): The value to be normalized.
    mean (float): The mean value for normalization.
    std (float): The standard deviation for normalization.

    Returns:
    float: The normalized value.
    """
    return (feature_value - mean) / std

def predict_yield():
    """
    Predicts the agricultural yield based on input parameters and the selected country.
    """
    country = document.getElementById("country").value

    energy = document.getElementById("energy_use").value
    water = document.getElementById("water_use").value
    fert_use = document.getElementById("fertilizer_use").value
    pesticide = document.getElementById("pesticide_use").value
    rural_pop = document.getElementById("rural_pop").value
    rural_pop = rural_pop / 100
    pesticide_imports = document.getElementById("pesticide_import").value
    air_dep = document.getElementById("nad").value
    y = 0

    if country == "india":
        # beta = [energy, fert_use, rural_pop, water, pesticide_imports, air_dep]
        beta = [3.15493714e+00, 7.68832601e-02, 3.61354433e-02, -1.23142065e-01, -9.34274321e-02, 6.90232281e-02, 2.70080825e-03]
        means = [2.281895, 119.211428, 0.704489, 1218.085592, 0.181360, 17.351733]
        stds = [0.904181, 34.859563, 0.027088, 139.541897, 0.191254, 1.812077]

        energy_n = normalise(energy, means[0], stds[0])
        fert_use_n = normalise(fert_use, means[1], stds[1])
        rural_pop_n = normalise(rural_pop, means[2], stds[2])
        water_n = normalise(water, means[3], stds[3])
        pesticide_imports_n = normalise(pesticide_imports, means[4], stds[4])
        air_dep_n = normalise(air_dep, means[5], stds[5])
        y = beta[0] + beta[1] * energy_n + beta[2] * fert_use_n + beta[3] * rural_pop_n + beta[4] * water_n + beta[5] * pesticide_imports_n + beta[6] * air_dep_n

    elif country == "china":
        beta = [6.3336981, 0.1136804, -0.03267097, -0.03830497, -0.10079726, 0.03945105, 0.05685124, 0.10387031]
        means = [2.207428, 310.492380, 0.585915, 800.666014, 2.020476, 0.356386, 22.493000]
        stds = [0.647942, 70.817356, 0.103549, 58.437812, 0.507163, 0.147310, 5.072590]

        energy_n = normalise(energy, means[0], stds[0])
        fert_use_n = normalise(fert_use, means[1], stds[1])
        rural_pop_n = normalise(rural_pop, means[2], stds[2])
        water_n = normalise(water, means[3], stds[3])
        pesticide_n = normalise(pesticide, means[4], stds[4])
        pesticide_imports_n = normalise(pesticide_imports, means[5], stds[5])
        air_dep_n = normalise(air_dep, means[6], stds[6])
        y = beta[0] + beta[1] * energy_n + beta[2] * fert_use_n + beta[3] * rural_pop_n + beta[4] * water_n + beta[5] * pesticide_n + beta[6] * pesticide_imports_n + beta[7] * air_dep_n

    document.getElementById("predicted").innerHTML = y