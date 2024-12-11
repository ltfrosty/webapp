from org.transcrypt.stubs.browser import *
import random

def on_sliderchange(slider_id, textinput_id):
	slider = document.getElementById(slider_id)
	textinput = document.getElementById(textinput_id)
	textinput.value = slider.value
	
def on_input(textinput_id, slider_id):
	textinput = document.getElementById(textinput_id)
	slider = document.getElementById(slider_id)
	slider.value = textinput.value

def dd_onchange():
	text_inputs = document.getElementsByClassName("text_input")
	for text_input in text_inputs:
		text_input.value = 0
	sliders = document.getElementsByClassName("slider")
	for slider in sliders:
		slider.value = 0


	document.getElementById("predicted").innerHTML = ""

def normalise(feature_value, mean, std):
    return (feature_value-mean)/std

def predict_yield():
	country = document.getElementById("country").value

	energy = document.getElementById("energy_use").value
	water = document.getElementById("water_use").value
	fert_use = document.getElementById("fertilizer_use").value
	pesticide = document.getElementById("pesticide_use").value
	rural_pop = document.getElementById("rural_pop").value
	rural_pop = rural_pop/100
	pesticide_imports = document.getElementById("pesticide_import").value
	air_dep = document.getElementById("nad").value
	y = 0

	if country == "india":
		# beta = [energy, fert_use, rural_pop, water, pesticide_imports, air_dep]
		beta = [3.15493714e+00, 7.68832601e-02, 3.61354433e-02, -1.23142065e-01, -9.34274321e-02, 6.90232281e-02, 2.70080825e-03]
		means = [2.281895, 119.211428, 0.704489, 1218.085592, 0.181360, 17.351733]
		stds = [0.904181, 34.859563, 0.027088, 139.541897, 0.191254, 1.812077]

		energy_n = normalise(energy, means[0],stds[0])
		fert_use_n = normalise(fert_use ,means[1],stds[1])
		rural_pop_n = normalise(rural_pop ,means[2],stds[2]) 
		water_n = normalise(water ,means[3],stds[3])
		pesticide_imports_n = normalise(pesticide_imports, means[4],stds[4])
		air_dep_n = normalise(air_dep, means[5],stds[5])
		y = beta[0] + beta[1]*energy_n + beta[2]*fert_use_n + beta[3]*rural_pop_n + beta[4]*water_n + beta[5]*pesticide_imports_n + beta[6]*air_dep_n

	elif country == "china":
		beta = [6.3336981, 0.1136804 , -0.03267097, -0.03830497, -0.10079726, 0.03945105, 0.05685124, 0.10387031]
		means = [2.207428, 310.492380, 0.585915, 800.666014, 2.020476, 0.356386, 22.493000]
		stds = [0.647942, 70.817356, 0.103549, 58.437812, 0.507163, 0.147310, 5.072590]

		energy_n = normalise(energy, means[0],stds[0])
		fert_use_n = normalise(fert_use ,means[1],stds[1])
		rural_pop_n = normalise(rural_pop ,means[2],stds[2]) 
		water_n = normalise(water ,means[3],stds[3])
		pesticide_n = normalise(pesticide, means[4], stds[4])
		pesticide_imports_n = normalise(pesticide_imports, means[5],stds[5])
		air_dep_n = normalise(air_dep, means[6],stds[6])
		y = beta[0] + beta[1]*energy_n + beta[2]*fert_use_n + beta[3]*rural_pop_n + beta[4]*water_n + beta[5]*pesticide_n + beta[6]*pesticide_imports_n + beta[7]*air_dep_n

	elif country == "thailand":
		beta = [2.73057058, -0.04029616, 0.01690372, -0.03774476, -0.24255145, 0.04837969, 0.09816368]
		means = [0.040198, 87.575715, 0.622444, 2018.722063, 4.316941, 8.309510]
		stds = [0.017489, 22.741275, 0.078222, 369.677924, 2.644196, 0.855591]

		energy_n = normalise(energy, means[0],stds[0])
		fert_use_n = normalise(fert_use ,means[1],stds[1])
		rural_pop_n = normalise(rural_pop ,means[2],stds[2]) 
		water_n = normalise(water ,means[3],stds[3])
		pesticide_imports_n = normalise(pesticide_imports, means[4],stds[4])
		air_dep_n = normalise(air_dep, means[5],stds[5])
		y = beta[0] + beta[1]*energy_n + beta[2]*fert_use_n + beta[3]*rural_pop_n + beta[4]*water_n + beta[5]*pesticide_imports_n + beta[6]*air_dep_n


	elif country == "vietnam":
		beta = [4.61225102, -0.10313642, -0.3306774, -0.25948562, 0.25923982, 0.01632498, 0.16175918]
		means = [216.836666, 0.742317, 921.318308, 2.020476, 6.401125, 9.371133]
		stds = [62.182577, 0.049593, 213.912322, 0.507163, 5.015212, 1.958312]

		fert_n = normalise(fert_use ,means[0],stds[0])
		rural_pop_n = normalise(rural_pop ,means[1],stds[1]) 
		#urban_pop_n = normalise(urban_pop ,means[2],stds[2])
		water_n = normalise(water ,means[2],stds[2])
		pesticide_n = normalise(pesticide, means[3], stds[3])
		pesticide_imports_n = normalise(pesticide_imports, means[4],stds[4])
		air_dep_n = normalise(air_dep, means[5],stds[5])
		y = beta[0] + beta[1]*fert_n + beta[2]*rural_pop_n + beta[3]*water_n + beta[4]*pesticide_n + beta[5]*pesticide_imports_n + beta[6]*air_dep_n


	elif country == "combined":
		beta = [4.1799428, 1.09565331, -0.11111096, -0.33911767, 0.08350755, 0.08676248]
		means = [184.602976, 0.658706, 1247.529373, 3.313240, 14.171850]
		stds = [104.404771, 0.100096, 530.288294, 4.450771, 6.345971]

		fert_use_n = normalise(fert_use ,means[0],stds[0])
		rural_pop_n = normalise(rural_pop ,means[1],stds[1]) 
		water_n = normalise(water ,means[2],stds[2])
		pesticide_imports_n = normalise(pesticide_imports, means[3],stds[3])
		air_dep_n = normalise(air_dep, means[4],stds[4])
		y = beta[0] + beta[1]*fert_use_n + beta[2]*rural_pop_n + beta[3]*water_n + beta[4]*pesticide_imports_n + beta[5]*air_dep_n


	if y < 0:
		y = 0
	document.getElementById("predicted").innerHTML = f"{round(y, 3)} t/ha"
