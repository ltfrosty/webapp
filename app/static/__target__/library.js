// Transcrypt'ed from Python, 2024-12-04 22:09:49
var random = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, _sort, abs, all, any, assert, bin, bool, bytearray, bytes, callable, chr, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, hex, input, int, isinstance, issubclass, len, list, map, max, min, object, oct, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_random__ from './random.js';
__nest__ (random, '', __module_random__);
var __name__ = '__main__';
export var on_sliderchange = function (slider_id, textinput_id) {
	var slider = document.getElementById (slider_id);
	var textinput = document.getElementById (textinput_id);
	textinput.value = slider.value;
};
export var on_input = function (textinput_id, slider_id) {
	var textinput = document.getElementById (textinput_id);
	var slider = document.getElementById (slider_id);
	slider.value = textinput.value;
};
export var dd_onchange = function () {
	var text_inputs = document.getElementsByClassName ('text_input');
	for (var text_input of text_inputs) {
		text_input.value = 0;
	}
	var sliders = document.getElementsByClassName ('slider');
	for (var slider of sliders) {
		slider.value = 0;
	}
	document.getElementById ('predicted').innerHTML = '';
};
export var normalise = function (feature_value, mean, std) {
	return (feature_value - mean) / std;
};
export var predict_yield = function () {
	var country = document.getElementById ('country').value;
	var energy = document.getElementById ('energy_use').value;
	var water = document.getElementById ('water_use').value;
	var fert_use = document.getElementById ('fertilizer_use').value;
	var pesticide = document.getElementById ('pesticide_use').value;
	var rural_pop = document.getElementById ('rural_pop').value;
	var rural_pop = rural_pop / 100;
	var pesticide_imports = document.getElementById ('pesticide_import').value;
	var air_dep = document.getElementById ('nad').value;
	var y = 0;
	if (country == 'india') {
		var beta = [3.15493714, 0.0768832601, 0.0361354433, -(0.123142065), -(0.0934274321), 0.0690232281, 0.00270080825];
		var means = [2.281895, 119.211428, 0.704489, 1218.085592, 0.18136, 17.351733];
		var stds = [0.904181, 34.859563, 0.027088, 139.541897, 0.191254, 1.812077];
		var energy_n = normalise (energy, means [0], stds [0]);
		var fert_use_n = normalise (fert_use, means [1], stds [1]);
		var rural_pop_n = normalise (rural_pop, means [2], stds [2]);
		var water_n = normalise (water, means [3], stds [3]);
		var pesticide_imports_n = normalise (pesticide_imports, means [4], stds [4]);
		var air_dep_n = normalise (air_dep, means [5], stds [5]);
		var y = (((((beta [0] + beta [1] * energy_n) + beta [2] * fert_use_n) + beta [3] * rural_pop_n) + beta [4] * water_n) + beta [5] * pesticide_imports_n) + beta [6] * air_dep_n;
	}
	else if (country == 'china') {
		var beta = [6.3336981, 0.1136804, -(0.03267097), -(0.03830497), -(0.10079726), 0.03945105, 0.05685124, 0.10387031];
		var means = [2.207428, 310.49238, 0.585915, 800.666014, 2.020476, 0.356386, 22.493];
		var stds = [0.647942, 70.817356, 0.103549, 58.437812, 0.507163, 0.14731, 5.07259];
		var energy_n = normalise (energy, means [0], stds [0]);
		var fert_use_n = normalise (fert_use, means [1], stds [1]);
		var rural_pop_n = normalise (rural_pop, means [2], stds [2]);
		var water_n = normalise (water, means [3], stds [3]);
		var pesticide_n = normalise (pesticide, means [4], stds [4]);
		var pesticide_imports_n = normalise (pesticide_imports, means [5], stds [5]);
		var air_dep_n = normalise (air_dep, means [6], stds [6]);
		var y = ((((((beta [0] + beta [1] * energy_n) + beta [2] * fert_use_n) + beta [3] * rural_pop_n) + beta [4] * water_n) + beta [5] * pesticide_n) + beta [6] * pesticide_imports_n) + beta [7] * air_dep_n;
	}
	else if (country == 'thailand') {
		var beta = [2.73057058, -(0.04029616), 0.01690372, -(0.03774476), -(0.24255145), 0.04837969, 0.09816368];
		var means = [0.040198, 87.575715, 0.622444, 2018.722063, 4.316941, 8.30951];
		var stds = [0.017489, 22.741275, 0.078222, 369.677924, 2.644196, 0.855591];
		var energy_n = normalise (energy, means [0], stds [0]);
		var fert_use_n = normalise (fert_use, means [1], stds [1]);
		var rural_pop_n = normalise (rural_pop, means [2], stds [2]);
		var water_n = normalise (water, means [3], stds [3]);
		var pesticide_imports_n = normalise (pesticide_imports, means [4], stds [4]);
		var air_dep_n = normalise (air_dep, means [5], stds [5]);
		var y = (((((beta [0] + beta [1] * energy_n) + beta [2] * fert_use_n) + beta [3] * rural_pop_n) + beta [4] * water_n) + beta [5] * pesticide_imports_n) + beta [6] * air_dep_n;
	}
	else if (country == 'vietnam') {
		var beta = [4.61225102, -(0.10313642), -(0.3306774), -(0.25948562), 0.25923982, 0.01632498, 0.16175918];
		var means = [216.836666, 0.742317, 921.318308, 2.020476, 6.401125, 9.371133];
		var stds = [62.182577, 0.049593, 213.912322, 0.507163, 5.015212, 1.958312];
		var fert_n = normalise (fert_use, means [0], stds [0]);
		var rural_pop_n = normalise (rural_pop, means [1], stds [1]);
		var water_n = normalise (water, means [2], stds [2]);
		var pesticide_n = normalise (pesticide, means [3], stds [3]);
		var pesticide_imports_n = normalise (pesticide_imports, means [4], stds [4]);
		var air_dep_n = normalise (air_dep, means [5], stds [5]);
		var y = (((((beta [0] + beta [1] * fert_n) + beta [2] * rural_pop_n) + beta [3] * water_n) + beta [4] * pesticide_n) + beta [5] * pesticide_imports_n) + beta [6] * air_dep_n;
	}
	else if (country == 'combined') {
		var beta = [4.1799428, 1.09565331, -(0.11111096), -(0.33911767), 0.08350755, 0.08676248];
		var means = [184.602976, 0.658706, 1247.529373, 3.31324, 14.17185];
		var stds = [104.404771, 0.100096, 530.288294, 4.450771, 6.345971];
		var fert_use_n = normalise (fert_use, means [0], stds [0]);
		var rural_pop_n = normalise (rural_pop, means [1], stds [1]);
		var water_n = normalise (water, means [2], stds [2]);
		var pesticide_imports_n = normalise (pesticide_imports, means [3], stds [3]);
		var air_dep_n = normalise (air_dep, means [4], stds [4]);
		var y = ((((beta [0] + beta [1] * fert_use_n) + beta [2] * rural_pop_n) + beta [3] * water_n) + beta [4] * pesticide_imports_n) + beta [5] * air_dep_n;
	}
	if (y < 0) {
		var y = 0;
	}
	document.getElementById ('predicted').innerHTML = '{} t/ha'.format (round (y, 3));
};

//# sourceMappingURL=library.map