#sample dictionary
my_dict = {'banana':3,'apple':1,'cherry':2, 'date':4}
print("orginal list:" ,my_dict)
#sort in ascending order based on keys
asorted_dict = dict(sorted(my_dict.items()))
print("Asending order:", asorted_dict)
#sort in decending order based on keys
desorted_dict = dict(sorted(my_dict.items(),reverse=True))
print("Desorted order:", desorted_dict)
