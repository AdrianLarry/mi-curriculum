import hashlib
import subprocess
import os

HTML_FILE = "paper_ai_hype.html"

OTS_PATH = r"C:\Users\Dell\AppData\Roaming\Python\Python313\Scripts\ots.exe"

# 1️⃣ Calcular hash SHA-256
with open(HTML_FILE, "rb") as f:
    sha256_hash = hashlib.sha256(f.read()).hexdigest()

print(f"✅ Hash SHA-256 calculado: {sha256_hash}")

# 2️⃣ Guardar hash
hash_file = HTML_FILE + ".hash"
with open(hash_file, "w") as f:
    f.write(sha256_hash)

# 3️⃣ Ejecutar ots.exe con ruta absoluta
subprocess.run([OTS_PATH, "stamp", HTML_FILE], check=True)

# 4️⃣ Enlace de verificación
verification_link = "https://opentimestamps.org/verify.html"

# 5️⃣ Insertar footer
html_footer = f"""
<footer style="margin-top:50px;padding:15px;background:#f8f9fa;color:#333;font-size:0.9em;border-top:1px solid #ddd;">
  <p><strong>Huella digital (SHA-256):</strong> {sha256_hash}</p>
  <p>Certificado de fecha emitido por <a href="{verification_link}" target="_blank">OpenTimestamps</a></p>
  <p>Archivo .ots generado en esta carpeta.</p>
</footer>
</body>
</html>
"""

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html_content = f.read()

if "</body>" in html_content:
    html_content = html_content.replace("</body>", html_footer)

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"🎯 Paper actualizado con huella digital y certificado OpenTimestamps.")