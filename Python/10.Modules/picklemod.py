# Serialization, Deserialization & Pickle — Notes Summary
# 📌 Python Object
# Anything in Python (int, list, dict, etc.)

# 👉 Example:

# x = 10
# li = [1,2,3]
# 📌 Byte Stream
# Data in binary form (0s and 1s)

# 👉 Used for:

# file storage
# data transfer
# 📌 Serialization
# Convert Python object → byte stream

# 👉 Purpose:

# save data
# send data
# 📌 Deserialization
# Convert byte stream → Python object

# 👉 Purpose:

# load saved data
# reconstruct object
# 📌 Pickle Module
# Used for serialization & deserialization
# 📌 Functions (Important)
# pickle.dump(obj, file)   # object → file
# pickle.load(file)        # file → object
# pickle.dumps(obj)        # object → bytes
# pickle.loads(bytes)      # bytes → object
# 📌 Flow (Very Important)
# Object → Serialization → Bytes → File/Network
# Bytes → Deserialization → Object
# 📌 Purpose
# Save data permanently
# Transfer data over network
# Store complex objects
# Reload data later
# ⚠️ Important Notes
# Use "wb" → write binary
# Use "rb" → read binary
# Not safe for untrusted data
# 🧠 One-Line Memory

# Object → Bytes → Store/Send → Bytes → Object

# Main functions
# dump()  → serialize object → store in file
# load()  → deserialize data → get object from file

import pickle
# l=[10,20,30,40,50]
# file=open("writedata.txt","wb");
# pickle.dump(l,file);
# file.close();

file=open("writedata.txt","rb");
l=pickle.load(file);
file.close();
print(l);
