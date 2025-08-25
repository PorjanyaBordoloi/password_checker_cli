# Password Checker CLI 🔒

A simple command-line tool to check password strength and provide actionable feedback.

## Features

- Checks for length, lowercase, uppercase, digits, and special characters
- Provides suggestions to improve password strength
- Works interactively or via CLI argument

## Installation

Clone the repo and install locally:

```bash
git clone https://github.com/PorjanyaBordoloi/password_checker_cli.git
cd password_checker_cli
pip install -e .
```
## Usage
Check a password directly:

```bash

pwd_checker "Abc12345!"
```
Or run interactively:

```bash

pwd_checker
# Enter your password securely
```
## Feedback Example

```sql
mid rookie
Suggestions:
- Add some uppercase characters in the password
- Give some special buddy
```
