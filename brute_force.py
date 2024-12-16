import requests
import time

class BruteForceChecker:
    def __init__(self, target_url, username_list, password_list):
        self.target_url = target_url
        self.username_list = username_list
        self.password_list = password_list

    def attempt_login(self, username, password):
        """Attempts to log in with the provided username and password."""
        payload = {
            'username': username,
            'password': password
        }
        response = requests.post(self.target_url, data=payload)
        print(f"Attempting {username}:{password} - Response: {response.text}")  # Debug output
        return response

    def check_vulnerability(self):
        """Checks for brute force vulnerabilities."""
        for username in self.username_list:
            for password in self.password_list:
                print(f"Trying {username}:{password}")
                response = self.attempt_login(username, password)
                
                # Adjust this line based on the actual response
                if "Login successful" in response.text:
                    print(f"[+] Found valid credentials: {username}:{password}")
                    return  # Stop on first successful login

                time.sleep(1)  # Sleep to avoid overwhelming the server

        print("[-] No valid credentials found.")

if __name__ == "__main__":
    target_url = "http://127.0.0.1:5000/login"  # Ensure this is correct
    with open("usernames.txt", "r") as f:
        username_list = f.read().splitlines()
    with open("passwords.txt", "r") as f:
        password_list = f.read().splitlines()

    checker = BruteForceChecker(target_url, username_list, password_list)
    checker.check_vulnerability()
