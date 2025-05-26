# FVE Výroba – Graf

Tato Streamlit aplikace umožňuje nahrát CSV soubor s daty výroby z fotovoltaické elektrárny a zobrazit přehledný graf výkonu v čase.

## 🔧 Funkce
- Detekce sloupců s datem a výkonem automaticky
- Podpora českého formátu CSV (kódování Windows-1250 i UTF-8)
- Interaktivní graf pomocí Matplotlib

## 📦 Spuštění lokálně

```bash
pip install -r requirements.txt
streamlit run app.py
```

## ☁️ Nasazení na Streamlit Cloud
1. Vytvoř účet na [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Propoj s GitHubem
3. Vyber tento repozitář a `app.py` jako hlavní soubor
4. Deployni!

## 📁 Formát CSV

```csv
Datum;"-A/60008963 [kW]";Status
01.05.2025 00:15;0,033;naměřená data OK;
```
