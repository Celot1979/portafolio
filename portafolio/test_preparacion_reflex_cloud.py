import os

print("\n--- Test de preparación para Reflex Cloud ---\n")

# 1. .env y DATABASE_URL
if os.path.exists(".env"):
    with open(".env") as f:
        env_content = f.read()
    if "DATABASE_URL" in env_content:
        print("✅ .env existe y contiene DATABASE_URL")
    else:
        print("❌ .env existe pero falta DATABASE_URL")
else:
    print("❌ No existe el archivo .env")

# 2. requirements.txt contiene python-dotenv
if os.path.exists("requirements.txt"):
    with open("requirements.txt") as f:
        reqs = f.read()
    if "python-dotenv" in reqs:
        print("✅ requirements.txt contiene python-dotenv")
    else:
        print("❌ requirements.txt NO contiene python-dotenv")
else:
    print("❌ No existe requirements.txt")

# 3. .env y .db en .gitignore
if os.path.exists(".gitignore"):
    with open(".gitignore") as f:
        gi = f.read()
    if ".env" in gi:
        print("✅ .env está en .gitignore")
    else:
        print("❌ .env NO está en .gitignore")
    if ".db" in gi:
        print("✅ .db está en .gitignore")
    else:
        print("❌ .db NO está en .gitignore")
else:
    print("❌ No existe .gitignore")

# 4. No hay archivos .db en el repo
found_db = False
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".db"):
            print(f"❌ Archivo .db encontrado: {os.path.join(root, file)}")
            found_db = True
if not found_db:
    print("✅ No hay archivos .db en el repo")

# 5. rxconfig.py existe
if os.path.exists("rxconfig.py"):
    print("✅ rxconfig.py existe")
else:
    print("❌ No existe rxconfig.py")

# 6. alembic/versions tiene migraciones
if os.path.exists("alembic/versions") and os.listdir("alembic/versions"):
    print("✅ Hay migraciones en alembic/versions")
else:
    print("❌ No hay migraciones en alembic/versions")

# 7. requirements.txt sin duplicados
if os.path.exists("requirements.txt"):
    lines = [l.strip() for l in reqs.splitlines() if l.strip() and not l.startswith('#')]
    if len(lines) == len(set(lines)):
        print("✅ requirements.txt sin dependencias duplicadas")
    else:
        print("❌ requirements.txt tiene dependencias duplicadas")

# 8. README.md existe
if os.path.exists("README.md"):
    print("✅ README.md existe")
else:
    print("❌ No existe README.md")

print("\n--- Fin del test de preparación ---\n") 