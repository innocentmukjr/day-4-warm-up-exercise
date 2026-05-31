# day-4-warm-up-exercise
# Day 4 – Warm‑Up Clinic Dictionary (From Memory)

## 📘 The Exercise Instructions

Do everything from memory – no hints, no looking back.

1. Create a dictionary `clinic` with 3 patients. Each patient has `"age"` and `"condition"` as nested keys.
2. Loop through and print each patient's name and condition neatly.
3. Create a set of patients whose age is above 30.
4. Create a tuple `clinic_info` with clinic name, location, and year opened. Unpack and print each value.
5. Collect all conditions from all patients into a list. Convert to a set and print how many unique conditions exist.

---

## 🧠 My Approach

- **#1:** Nested dictionary – outer keys are patient IDs, inner dicts contain `age` and `condition`.
- **#2:** Used `for key, value in clinic.items():` and printed `key` and `value['condition']`.
- **#3:** Created an empty list, looped through items, appended keys where `value['age'] > 30`, then converted list to set.
- **#4:** Created tuple with three values, unpacked into three variables, printed with labels.
- **#5:** Looped through `clinic.values()`, appended each `condition` to a list, then converted list to set and used `len()`.

---

## 🚧 Challenges I Faced

- Remembering the exact syntax for nested dictionary access without looking back – succeeded.
- Deciding whether to use a set directly (e.g., `{key for key, value in clinic.items() if value['age'] > 30}`) – I used a list then converted, which is fine but less concise.
- Unpacking tuple – straightforward once I remembered the number of variables must match.

---

## ✅ What I Learned

- I **can** recall dictionary syntax from memory – confidence boost.
- Converting a list to a set removes duplicates (for conditions).
- Unpacking tuples is intuitive and cleaner than indexing.
- A set comprehension would be more efficient for task 3:  
  `{key for key, value in clinic.items() if value['age'] > 30}` – I'll try next time.

---

## 🖥️ How to Run My Code

1. Save the code as `main.py`.
2. Run `python main.py`.
3. Expected output:
4. 
---

## 📅 Part of My AI/ML Learning Journey

Day 4 warm‑up – testing retention. Dictionaries, sets, tuples, and loops are foundational for data manipulation. In ML, similar structures appear when filtering patient data (e.g., age > 30), counting unique diagnoses, or unpacking configuration tuples. This exercise proves that consistent practice builds muscle memory.

---
*No hints, no looking back – and I did it. Ready for more.*
