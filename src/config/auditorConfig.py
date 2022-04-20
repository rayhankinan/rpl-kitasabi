import bcrypt

AUDITOR_USERNAME = "KITASABI"
AUDITOR_HASHED_PASSWORD = bcrypt.hashpw(b"KITASABI", bcrypt.gensalt())