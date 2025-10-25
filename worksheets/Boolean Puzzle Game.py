"""
You’re designing a gate access system. Access is granted only if:

The user is verified (verified == True)

The user has an even ID (id & 1 == 0)

The security flag bits contain at least one 1 in the last 3 bits (flags & 0b111 != 0)
"""
verified = input("Is the user verified? (yes/no): ").lower() == "yes"
user_id = int(input("Enter user ID (integer): "))
flags = int(input("Enter security flag bits (integer): "))

if verified and (user_id & 1 == 0) and (flags & 0b111 != 0):
    print("Access Granted")
else:
    print("Access Denied")

print("Debug Info")
print(f"Verified: {verified}")
print(f"User ID (binary): {bin(user_id)}")
print(f"Flags (binary):   {bin(flags)}")
