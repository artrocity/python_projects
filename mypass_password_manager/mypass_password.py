# Import Libraries
import os
import string
import random
import json

class PasswordManager:
    def __init__(self, website_entry=None, username_entry=None, password_entry=None) -> None:
        self.website_entry = website_entry
        self.username_entry = username_entry
        self.password_entry = password_entry

    def get_website(self) -> str:
        """
        Summary:
            Checks if a value has been entered for: Website
            and then attempts to get the entry
        Returns:
            str: Returns the Website
        """
        self.website_result = ""
        try:
            self.website_result = self.website_entry.get() if self.website_entry else None
            return self.website_result
        except Exception as e:
            print("Error: ", str(e))

    def get_username(self) -> str:
        """
        Summary:
            Checks if a value has been entered for: Username
            and then attempts to get the entry
        Returns:
            str: Returns the Username
        """
        self.username_result = ""
        try:
            self.username_result = self.username_entry.get() if self.username_entry else None
            return self.username_result
        except Exception as e:
            print("Error: ", str(e))

    def get_password(self) -> str:
        """
        Summary: 
            Checks if a value has been entered for: Password
            and then attempts to get the entries
        Returns:
            str: Returns the Password
        """
        self.password_result = ""
        try:
            self.password_result = self.password_entry.get() if self.password_entry else None
            return self.password_result
        except Exception as e:
            print("Error: ", str(e))

    def generate_password(self) -> str:
        """
        Summary:
            Generates a random 16 character password with 4 lowercase, 4 uppercase, 4 numbers and 4 symbols 
        Returns:
            str: Randomly generates password
        """
        new_password = ""
        password_categories = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
        password_list = [random.choice(category) for category in password_categories for _ in range(4)]
        random.shuffle(password_list)
        new_password = "".join(password_list)
        return new_password     

    def save_entries(self) -> None:
        """
        Summary:
            Takes the values for website, username, and password and saves it to a JSON file
        Returns: 
            None
        """
        data_entry = {
            self.website_result : {            
                "Username" : self.username_result,
                "Password" : self.password_result
            }
        }
        # Check if file exists and load its contents
        if os.path.exists("passwords.json"):
            with open("passwords.json", "r") as file:
                data = json.load(file)        
        else:
            data = {}
        
        data[self.website_result] = data_entry[self.website_result]

        # Save updated data to file
        with open("passwords.json", "w") as file:
            json.dump(data, file, indent=4)

    def retrieve_entries(self, search_request:str) -> dict:
        """
        Summary:
            Takes a search request as an argument and attempts to retrieve the values associated 
            with the key from a json file called "passwords.json" and return them
        Args:
            search_request (str): Website to search for
        Returns:
            dict: Dictionary of Username and Password for given website
        """
        self.search_result = search_request
        data = {}

        #Open the file
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError as e:
            print("Error: ", str(e))

        # Attempt to return the dictionary value from the key search request
        if self.search_result not in data:
            raise KeyError(f"No entry found for {search_request}.")
        return data[self.search_result] 