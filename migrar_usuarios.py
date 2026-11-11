import json
from seguridad import crear_hash
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
USUARIOS = RAIZ / "usuarios.json"
usuarios = json.loads(USUARIOS.read_text(encoding="utf-8"))

for usuario in usuarios:
	clave = usuario["clave"]
	usuario["hash"] = crear_hash(clave)
	del usuario["clave"]

USUARIOS.write_text(json.dumps(usuarios, indent=2), encoding="utf-8") 