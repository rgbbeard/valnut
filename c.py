#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import utils


class C:
	__key: str = None
	__cipher = None
	__tag = None
	__nonce = None

	def __init__(self):
		if utils.fsize("./c") and utils.fsize("./c") > 0:
			try:
				with open("./c", "rb") as c:
					self.__key = c.readline().strip()
			except Exception as e:
				self.generate_key(16)
		else:
			self.generate_key(16)

		self.__cipher = AES.new(self.__key, AES.MODE_EAX)
		self.__nonce = self.__cipher.nonce

	def generate_key(self, bytes: int = None):
		tmp = get_random_bytes(bytes)
		self.__key = tmp
		with open("./c", "wb") as c:
			c.write(tmp)

	def decrypt(self, password: str):
		return self.__cipher.decrypt_and_verify(password, self.__tag, self.__nonce)

	def encrypt(self, password: str):
		text, tag = self.__cipher.encrypt_and_digest(password)
		self.__tag = tag
		return text
