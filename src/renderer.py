from datetime import datetime,timezone
from pathlib import Path
def render(m):
 template=Path("templates/dashboard.html").read_text()
 return template.replace("{{generated}}",datetime.now(timezone.utc).isoformat()).replace("{{metrics}}",str(m))
