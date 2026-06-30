# =====================================================================
# TRACK 1 - DAY 5: MASTER REGISTRY COMPOSITE DATA MAP
# =====================================================================
#
# WHAT WE LEARNED TODAY:
# 1. COMPOSITE STRUCTURE MAPS: Combined Lists, Tuples, and Dictionaries 
#    into a unified high-dimensional registry schema tree.
# 2. CONSTANT-TIME ACCESS O(1): Leveraged Dictionary keys for high-speed 
#    metadata lookups utilizing underlying Hash Table architectures.
# 3. FIXED HARDWARE CONTRACTS (Immutability): Enforced strict multi-node 
#    hardware profiles inside an un-mutable Tuple mapping space.
# 4. EXCEPTION BOUNDARY TEST (try/except): Intercepted a runtime TypeError 
#    when the code tried to violate data immutability limits.
#
# =====================================================================
import json

# 1. INITIALIZE MASTER COMPOSITE REGISTER MAP (Dictionary Container)
cluster_profile = {
    "cluster_id": "GPU-CLUSTER-BETA",
    
    # Nested Tuple: Strict hardware limits -> (NODE_COUNT, GPU_CORE_ID)
    "hardware_nodes": (4, 0),
    
    # Nested List: Dynamic tracking space for variable learning rate adjustments
    "learning_rate_history": [0.01, 0.005, 0.001]
}

print("--- [INITIALIZING TRACK 1 DAY 5] Executing Composite Profile Registry ---\n")

# 2. MUTATION TASK A: Target the inner mutable list and append a new optimizer metric
cluster_profile["learning_rate_history"].append(0.0001)
print(f"✅ Dynamic List Mutated: Updated Learning Rates -> {cluster_profile['learning_rate_history']}")


# 3. MUTATION TASK B: Attempt to mutate the immutable tuple profile to verify security
try:
    print("\n⚠️  Attempting illegal modification on hardware tuple parameters...")
    
    # Attempting to overwrite the first position (index 0) of the tuple inside the dict to 8
    cluster_profile["hardware_nodes"][0] = 8

except TypeError:
    # Captures the type execution failure cleanly
    print("🔒 Immutability Confirmed: Cluster hardware profile protected natively by Tuple boundary.")


# =====================================================================
# PIPELINE METADATA VISUALIZATION
# =====================================================================
print("\n--- Final Master Memory Tree Layout ---")
print(json.dumps(cluster_profile, indent=4))