import copy

# A database of users where the access permissions are stored inside an inner list
original_user = ["Harsha", ["Admin", "Developer"]]
shallow_user = original_user.copy()

# The outer boxes have DIFFERENT addresses
print(id(original_user) == id(shallow_user))  # False

# BUT look at the inner nested list boxes—they share the EXACT SAME room number!
print(id(original_user[1]) == id(shallow_user[1]))  # Trueho
import copy
original_admin = ["Harsha", ["Read", "Write"]]
deep_admin = copy.deepcopy(original_admin)

# Both the outer boxes AND the inner lists have completely unique addresses
print(id(original_admin[1]) == id(deep_admin[1]))  # False

# Modifying the deep copy has ZERO effect on the original data
deep_admin[1].append("Execute")

print(original_admin)  # Output: ['Harsha', ['Read', 'Write']] (Safe!)
print(deep_admin)      # Output: ['Harsha', ['Read', 'Write', 'Execute']]


# =====================================================================
# MASTER MEMORY CHEAT SHEET (DAY 2 SUMMARY)
# =====================================================================
# 
# 1. THE id() FUNCTION
#    - Every variable points to a specific memory slot (room number) in RAM.
#    - Use id(variable_name) to see its exact digital street address.
#
# 2. IMMUTABLE DATA TYPES (Strings, Ints, Floats, Tuples, Booleans)
#    - Locked in memory. They can NEVER be changed in place.
#    - Modifying them forces Python to create a BRAND NEW memory room.
#    - Example: text = "harsha" -> text += "1" changes its id().
#
# 3. MUTABLE DATA TYPES (Lists, Dictionaries, Sets)
#    - Flexible in memory. They CAN be altered in place.
#    - Modifying them keeps the exact same memory address.
#    - Example: list.append("item") does NOT change its id().
#
# 4. MUTING AND THE EQUAL SIGN REASSIGMENT TRAP
#    - Setting list_b = list_a does NOT copy the data! 
#    - It copies the memory pointer. Altering list_b will ruin list_a.
#
# 5. SHALLOW COPY (.copy()) vs. DEEP COPY (copy.deepcopy())
#    - .copy(): Only clones the outer shell. Nested objects (lists inside lists)
#               still share the exact same inner memory pointers. (Unsafe for nested data!)
#    - copy.deepcopy(): A heavy module function that recursively replicates 
#                       EVERY layer, separating all inner arrays completely.
#
# =====================================================================s