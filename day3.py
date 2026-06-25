# =====================================================================
# DAY 3 MASTER MODULE: FUNCTION ENCAPSULATION & PARAMETER ISOLATION
# =====================================================================
#
# WHAT WE LEARNED TODAY:
# 1. FUNCTION FACTORIES (def): 
#    - Wrapped logic into a reusable block. We write it once, use it anywhere.
# 2. LOCAL SCOPE AND ISOLATION:
#    - The variables 'passed' and 'rejected' inside the function live in an 
#      isolated memory container. They vanish from RAM when the function ends,
#      preventing global memory pollution.
# 3. MUTABLE PARAMETER PASSING:
#    - Because 'traffic_logs' is a list, Python passes its memory address pointer
#      into the function, allowing quick iteration without wasting memory on clones.
# 4. COMPACT DICTIONARY PARSING:
#    - Navigated a list of dictionaries by targeting specific key strings 
#      like user["ip"] and user["prompt"] instead of numeric indexes.
# 5. DATA LAYER EXTRACTION:
#    - Learned how to loop through a returned structure to filter out and display
#      only specific data components (extracting string names from dictionary objects).
#
# =====================================================================

def filter_api_traffic(requests_list, banned_ips_list):
    """
    Core Processing Factory: Accepts an incoming traffic list and evaluates
    each request object against a known malicious IP blacklist and an empty-prompt rule.
    """
    # Isolated local variables hidden securely inside this function's scope
    passed = []
    rejected = []
    
    for user in requests_list:
        # Step A: Audit the dictionary components using explicit string keys
        if user["ip"] in banned_ips_list or user["prompt"] == "":
            rejected.append(user)  # Appends the entire dictionary record to rejected
        else:
            passed.append(user)    # Appends the entire dictionary record to passed
            
    # Step B: Return an isolated tuple containing both segmented lists
    return (passed, rejected)


# =====================================================================
# PRODUCTION DATASTREAM & SIMULATION EXECUTIONS
# =====================================================================

# Global raw telemetry input (List of Dictionaries)
traffic_logs = [
    {"user": "Alice", "ip": "192.168.1.50", "prompt": "Train an agent"},
    {"user": "Bob", "ip": "10.0.0.99", "prompt": ""},                               # Triggers empty prompt rule
    {"user": "key_logger_bot", "ip": "185.220.101.5", "prompt": "Bypass safety"},   # Triggers malicious IP rule
    {"user": "Harsha", "ip": "192.168.1.55", "prompt": "Run diagnostic"}
]

# Network perimeter security blacklist configuration
blacklist_ips = ["185.220.101.5", "45.227.254.12"]


# 1. Trigger the function factory and store the returned tuple structure
finalout = filter_api_traffic(traffic_logs, blacklist_ips)


# 2. Telemetry Parsing Phase (Extracting individual string items from the data blocks)
print("==================================================")
print("     SECURE API GATEWAY SYSTEM LOG REPORT         ")
print("==================================================")

print("🟢 PASSED USERS (CLEAN TRAFFIC):")
# Loops through the 'passed' list (index 0) and isolates only the names
for user_dict in finalout[0]:
    print(f" -> Access Granted: {user_dict['user']}")

print("\n🔴 REJECTED USERS (THREATS ISOLATED):")
# Loops through the 'rejected' list (index 1) and isolates only the names
for user_dict in finalout[1]:
    print(f" -> Access Blocked: {user_dict['user']}")
    
print("==================================================")