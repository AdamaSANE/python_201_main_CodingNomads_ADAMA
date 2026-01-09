# Create a virtual environment and edit the activation script to add
# the following information:
# 
# - ENVIRONMENT="development"
# - SECRET="i ate your sweets"
# 

import os

env = os.environ.get("ENVIRONMENT")
secret = os.environ.get("SECRET")

print(f"ENVIRONMENT = {env}")
print(f"SECRET = {secret}")
import os

env = os.environ.get("ENVIRONMENT")
secret = os.environ.get("SECRET")

print(f"ENVIRONMENT = {env}")
print(f"SECRET = {secret}")