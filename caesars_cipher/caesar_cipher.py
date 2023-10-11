from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
	print(logo)
	while True:
		direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
		text = input("Type your message:\n").lower()
		shift = int(input("Type the shift number:\n"))
		caesar(text, shift, direction)
		repeat = input("Would you like to use the cipher again? Y - Yes / N - No: ").lower()
		if repeat == "y":
			pass
		else:
			break

#Encrypts/Decrypts users text depending on direction
def caesar(text, shift, direction):
	cipher_text = ""
	for letter in text:
		if letter in alphabet:
			letter_index = alphabet.index(letter)
			if direction == "encode":
				new_index = (letter_index + shift) % 26
			elif direction == "decode":
				new_index = (letter_index - shift) % 26
			new_letter = alphabet[new_index]
			cipher_text += new_letter
		else:
			cipher_text += letter
	print(f"Here is the ciphered version of your text: {cipher_text}")
		
if __name__ == "__main__":
	main()

