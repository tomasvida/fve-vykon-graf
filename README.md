# FVE Výroba – Graf (měsíční členění)

Streamlit aplikace pro vizualizaci dat z FVE z CSV souboru, včetně zobrazení:
- grafů rozdělených po jednotlivých měsících
- tabulek s 10 nejvyššími hodnotami výkonu pro každý měsíc

## 🆕 Co je nového
- Automatické rozdělení grafu po kalendářních měsících
- Každý měsíc má svůj vlastní graf a vlastní top 10 tabulku
- Zvýraznění denních maxim v grafech

## 📦 Lokální spuštění

```bash
pip install -r requirements.txt
streamlit run app.py
```

## ☁️ Nasazení na Streamlit Cloud
1. Přihlas se na [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Vyber tento repozitář a soubor `app.py`
3. Klikni „Deploy“ a je hotovo!
