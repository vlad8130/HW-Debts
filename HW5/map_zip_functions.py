# lesson5
with open('text.txt') as f:
	text_string = f.read().lower().replace(',', '').replace('.', '').strip().split(' ')

frequency_dict = {}


def frequency(string):
	count = frequency_dict.get(string, 0)
	frequency_dict[string] = count + 1
	return frequency_dict


kol = list(map(frequency, text_string))
print(kol[1])
