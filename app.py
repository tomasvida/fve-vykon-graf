
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import io
import calendar

st.set_page_config(page_title="FVE Výroba - Graf", layout="wide")
st.title("📈 Zobrazení profilu výroby FVE z CSV souboru")

uploaded_file = st.file_uploader("Nahraj CSV soubor s daty z FVE:", type="csv")

if uploaded_file is not None:
    try:
        # Načtení dat se správným kódováním
        try:
            df = pd.read_csv(uploaded_file, encoding='windows-1250', sep=';')
        except UnicodeDecodeError:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file, encoding='utf-8', sep=';')

        df.columns = df.columns.str.strip().str.replace('"', '')
        datum_col = next((col for col in df.columns if 'Datum' in col), None)
        vykon_col = next((col for col in df.columns if 'kW' in col), None)

        if not datum_col or not vykon_col:
            st.error("Soubor neobsahuje očekávané sloupce s datem a výkonem.")
        else:
            df = df.rename(columns={datum_col: 'datetime', vykon_col: 'vykon_kW'})

            # Čištění a převod dat
            df['vykon_kW'] = df['vykon_kW'].astype(str)
            df['vykon_kW'] = df['vykon_kW'].str.extract(r'([0-9]+[.,]?[0-9]*)')[0]
            df['vykon_kW'] = df['vykon_kW'].str.replace(',', '.', regex=False).astype(float)
            df['datetime'] = pd.to_datetime(df['datetime'], dayfirst=True, errors='coerce')
            df = df.dropna(subset=['datetime'])
            df.set_index('datetime', inplace=True)

            # Rozdělení po měsících
            for (year, month), df_month in df.groupby([df.index.year, df.index.month]):
                month_name = f"{calendar.month_name[month]} {year}"

                # Určení maximálního výkonu pro každý den v měsíci
                df_daily_max = df_month['vykon_kW'].resample('D').max()
                max_dates = df_month[df_month['vykon_kW'].isin(df_daily_max.values)].index

                # Vykreslení grafu
                st.subheader(f"Graf výkonu FVE (15minutová maxima) – {month_name}")
                fig, ax = plt.subplots(figsize=(14, 6))
                ax.plot(df_month.index, df_month['vykon_kW'], label='Výkon FVE [kW]', color='blue')
                ax.scatter(max_dates, df_month.loc[max_dates, 'vykon_kW'], color='red', label='Denní maximum', zorder=5)
                ax.set_title(f'Profil výroby FVE – {month_name}')
                ax.set_xlabel('Datum a čas')
                ax.set_ylabel('Výkon [kW]')
                ax.grid(True)
                ax.legend()
                st.pyplot(fig)

                # Tabulka 10 nejvyšších hodnot v měsíci
                st.subheader(f"🔟 Nejvyšší hodnoty výkonu – {month_name}")
                top10 = df_month['vykon_kW'].nlargest(10).reset_index()
                top10.index += 1  # začít číslování od 1
                top10.columns = ['Datum a čas', 'Výkon [W]']
                top10['Výkon [W]'] = (top10['Výkon [W]'] * 1000).round(2)  # převod na watty
                st.dataframe(top10)

    except Exception as e:
        st.error(f"Chyba při zpracování souboru: {str(e)}")
else:
    st.info("Prosím nahraj CSV soubor pro zobrazení grafu.")
