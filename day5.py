#1ST CODE
# =====================================================================
# TRACK 1 - DAY 4: REFACTORED COMPACT DICTIONARY DATA MAPPING
# =====================================================================

def audit_loss_gradients(*metrics):
    """
    Modular Functional Scope: Audits dynamic tensor metric payloads and
    safely maps local lists to explicit string dictionary keys.
    """
    nominal_gradients = []
    anomalous_gradients = []
    
    for val in metrics:
        # FIX 1: Send anomalous values (>= 5.0 or < 0.0) directly to the corrupted list
        if val >= 5.0 or val < 0.0:
            anomalous_gradients.append(val)
        else:
            nominal_gradients.append(val)
            
    # FIX 2: Combine local structures into a single return Dictionary with string keys
    return {
        "clean": nominal_gradients,
        "corrupted": anomalous_gradients
    }

# =====================================================================
# SYSTEM EXECUTION PHASE (GLOBAL SCOPE)
# =====================================================================

# Pass 5 metrics into your dynamic input collector
audit_report = audit_loss_gradients(0.15, 4.82, 5.67, -0.22, 1.09)

print("--- Gradient Audit Report ---")
# The string key lookups now read directly out of the returned dictionary!
print(f"Clean Metrics:     {audit_report['clean']}")
print(f"Corrupted Metrics: {audit_report['corrupted']}")






#2ND CODE

def audit_loss_gradients(*metrics):
    nominal_gradients = []
    anomalous_gradients = []
    
    for val in metrics:
        if val > 5.0 or val < 0.0:
             anomalous_gradients.append(val)
        else:
            nominal_gradients.append(val)

    
      
    return{"clean": nominal_gradients,
        "corrupted": anomalous_gradients
        }

# Pass 5 metrics into your dynamic input collector
audit_report = audit_loss_gradients(0.15, 4.82, 5.67, -0.22, 1.09)

print("--- Gradient Audit Report ---")
print(f"Clean Metrics: {audit_report['clean']}")
print(f"Corrupted Metrics: {audit_report['corrupted']}")