# Automation Project (UI + API)

Tento projekt obsahuje:
- UI test (Selenium + POM) — Google search pre výraz **"synot games"**
- API testy (requests + pytest):
  - Dog CEO API (https://dog.ceo/api/breeds/image/random)
  - Free Public APIs (https://api.publicapis.org/entries)

## Požiadavky
- Python 3.8+
- Chrome prehliadač (ak spúšťate ne-headless)
- Odporúčané: vytvoriť virtuálne prostredie (venv)

## Inštalácia
```bash
# v koreňovom adresári projektu
python -m venv venv
source venv/bin/activate      # Linux / macOS
# alebo
venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

## Spustenie testov
- Spustiť všetky testy:
```bash
pytest
```

- Spustiť len UI testy:
```bash
pytest -m ui
```

- Spustiť len API testy:
```bash
pytest -m api
```

- Spustiť UI headless (napr. v CI):
```bash
export HEADLESS=1        # Linux / macOS
# alebo pre Windows PowerShell:
# $env:HEADLESS = "1"

pytest -m ui
```

## Štruktúra projektu
```
pages/             # Page Object Model pre UI
tests/ui/          # UI testy
tests/api/         # API testy
conftest.py        # fixtures pre browser (selenium) a requests session
requirements.txt
```

## Poznámky / tipy
- `conftest.py` používa `webdriver-manager`, takže nie je nutné ručne sťahovať chromedriver.
- Google v niektorých regiónoch zobrazí cookie/consent dialog — test sa ho snaží akceptovať automaticky (ak je prítomný).
- Ak v CI nemáte Chrome, použite container s Chrome prehliadačom alebo prispôsobte fixture pre iný driver.

## Ako nahrať na GitHub
1. `git init`
2. `git add .`
3. `git commit -m "Add automation tests (UI + API)"`
4. Vytvor repozitár na GitHub a pushni:
```bash
git remote add origin <URL_TO_YOUR_REPO>
git branch -M main
git push -u origin main
```
