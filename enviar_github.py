from pathlib import Path
import subprocess

pasta = Path.home() / "OneDrive" / "Área de Trabalho" / "python udemy"

print(pasta)
print(pasta.exists())

readme = pasta / "README.md"

if not readme.exists():
    print("O README não existe.")
else:
    print("O README já existe.")

resultado = subprocess.run(
    ["git", "status"],
    cwd=pasta,
    capture_output=True,
    text=True
)

print(resultado.returncode)
print(resultado.stdout)
print(resultado.stderr)


