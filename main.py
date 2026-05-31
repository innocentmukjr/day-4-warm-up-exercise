# ================================================
# DAY 4 WARM‑UP – Clinic Dictionary (From Memory)
# ================================================

# 1. Create dictionary with 3 patients (nested age and condition)
clinic = {
    "patient_1": {"age": 20, "condition": "malaria"},
    "patient_2": {"age": 45, "condition": "typhoid"},
    "patient_3": {"age": 64, "condition": "cough"}
}

# 2. Print each patient's name and condition
print("=== Patients and conditions ===")
for patient_id, info in clinic.items():
    print(f"{patient_id}: {info['condition']}")

# 3. Create a set of patients whose age > 30 (using set comprehension)
above_30_set = {patient_id for patient_id, info in clinic.items() if info['age'] > 30}
print("\nPatients above age 30:", above_30_set)

# 4. Tuple with clinic info, unpack and print
clinic_info = ("Josiah Clinic", "Wakiso", "2023")
name, location, year = clinic_info
print("\n--- Clinic Info ---")
print(f"Clinic Name: {name}")
print(f"Location: {location}")
print(f"Year Opened: {year}")

# 5. Collect all conditions, get unique count
all_conditions = [info['condition'] for info in clinic.values()]
unique_conditions = set(all_conditions)
print(f"\nNumber of unique conditions: {len(unique_conditions)}")
