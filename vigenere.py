

class VigenereCipher:
	def __init__(self, key, alphabet):
		self.alphabet = alphabet
		self.alphabet = [[i.upper(), i.lower()] for i in alphabet]
		print(self.alphabet)
		self.alphabet_size = len(self.alphabet)
		self.key = key
		self.table = {' ', '\'', '"', '.', ',', '!', '&', '$', ':', ';', '/', '\\', '#', '@', '%', '(', ')'}


	def encode(self, text):
		i_key = 0
		key_size = len(self.key)-1
		result = ""

		for i in text:
			if i in self.table:
				result += i
				continue
			
			isupp = False

			for k in range(len(self.alphabet)):
				upp_letter = self.alphabet[k][0]
				low_letter = self.alphabet[k][1]
				if upp_letter == i:
					text_letter_i = k
					isupp = True
				elif low_letter == i:
					text_letter_i = k

				if upp_letter == self.key[i_key] or low_letter == self.key[i_key]:
					key_letter_i = k


			if text_letter_i + key_letter_i < 26:
				letter = self.alphabet[text_letter_i + key_letter_i][1]
				if isupp:
					letter = word.upper()
				result += letter
			else:
				letter = self.alphabet[(text_letter_i + key_letter_i) % self.alphabet_size][1]
				if isupp:
					letter = word.upper()
				result += letter


			if i_key != key_size:
				i_key += 1
			else:
				i_key = 0
		
		return result



	def decode(self, text):
		i_key = 0
		key_size = len(self.key)-1
		result = ""

		for i in text:
			if i in self.table:
				result += i
				continue

			isupp = False

			for k in range(len(self.alphabet)):
				upp_letter = self.alphabet[k][0]
				low_letter = self.alphabet[k][1]
				if upp_letter == i:
					text_letter_i = k
					isupp = True
				elif low_letter == i:
					text_letter_i = k

				if upp_letter == self.key[i_key] or low_letter == self.key[i_key]:
					key_letter_i = k


			if text_letter_i - key_letter_i >= 0:
				letter = self.alphabet[text_letter_i - key_letter_i][1]
				if isupp:
					letter = word.upper()
				result += letter
			else:
				letter = self.alphabet[(text_letter_i - key_letter_i) + self.alphabet_size][1]
				if isupp:
					letter = word.upper()
				result += letter



			if i_key != key_size:
				i_key += 1
			else:
				i_key = 0
		
		return result



alph = "".join(chr(c) for c in range(97, 123))
o = VigenereCipher("key", alph)
print(o.encode("hello"))
print(o.decode(o.encode("hello")))