#!/usr/bin/env python3
import string
import argparse
import getpass

def pwd_checker(pwd_input):
    score = 0
    feedback = []

    if len(pwd_input) >= 8:
        score += 1
    else:
        feedback.append("Password is too short")

    if any(c.islower() for c in pwd_input):
        score += 1
    else:
        feedback.append("Add some lowercase characters in the password")

    if any(c.isupper() for c in pwd_input):
        score += 1
    else:
        feedback.append("Add some uppercase characters in the password")

    if any(c.isdigit() for c in pwd_input):
        score += 1
    else:
        feedback.append("Add any numbers in the password")

    if any(c in string.punctuation for c in pwd_input):
        score += 1
    else:
        feedback.append("Give some special buddy")

    return score, feedback

def main():
    parser = argparse.ArgumentParser(description="Password Strength Checker CLI")
    parser.add_argument("password", nargs="?", help="Password to check")
    args = parser.parse_args()

    # Use argument if provided, else secure input
    if args.password:
        pwd_input = args.password
    else:
        pwd_input = getpass.getpass("Enter your password: ")

    score, feedback = pwd_checker(pwd_input)

    # Classification
    if score <= 2:
        print("noob pass")
    elif score == 3:
        print("mid rookie")
    elif score == 4:
        print("strong pass")
    else:
        print("ultra strong pass 💪")

    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print("-", f)

if __name__ == "__main__":
    main()
