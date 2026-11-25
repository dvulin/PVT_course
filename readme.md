# PVT Course

## 1. Preuzimanje datoteka

* **Preko Git CLI-ja:**
  ```powershell
  git clone https://github.com/dvulin/PVT_course.git
  cd PVT_course
  ```
  *(Za kasnije dohvaćanje izmjena u mapi repozitorija pokreni `git pull`.)*

* **Preko web preglednika:**
  1. Na stranici repozitorija klikni **<> Code → Download ZIP**.
  2. Raspakiraj arhivu u svoj radni folder.
  3. Otvori taj folder u File Exploreru, u adresnu traku upiši `powershell` i pritisni `Enter`.

## 2. Aktivacija `reservoir` okruženja i sinkronizacija paketa

Dok si u svom radnom folderu sa skriptama, aktiviraj svoje postojeće `reservoir` okruženje (zamijeni `PUTANJA\DO\reservoir` svojom putanjom do okruženja):

```powershell
PUTANJA\DO\reservoir\Scripts\Activate.ps1
```

*(Ako PowerShell blokira izvršavanje skripte u trenutačnoj sesiji, prvo pokreni `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`.)*

Zatim sinkroniziraj potrebne module u to aktivirano `reservoir` okruženje:

```powershell
uv sync --active
```

*(Ako u folderu koristiš `requirements.txt` umjesto `pyproject.toml`, pokreni `uv pip install -r requirements.txt`.)*
