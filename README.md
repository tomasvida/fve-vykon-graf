# FVE Výroba – Graf (měsíční členění, označení hodnoty maxima)

Streamlit aplikace pro vizualizaci dat z FVE z CSV souboru:

- Měsíčně členěné grafy
- Zobrazení pouze jednoho měsíčního maxima (červený bod)
- Číselná hodnota maxima zapsaná přímo do grafu
- Přehledné tabulky 10 nejvyšších hodnot za každý měsíc
- Omezení šířky zobrazení na 80 % okna

## 🚀 Lokální spuštění

```bash
pip install -r requirements.txt
streamlit run app.py
```

## ☁️ Streamlit Cloud nasazení

1. Přihlas se na [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Vyber GitHub repozitář se soubory
3. Vyber `app.py` a spusť
