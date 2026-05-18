# Proyecto ML — Predicción de viajeros Bizkaibus 2026

Modelo predictivo de series temporales para estimar el número de **viajeros y expediciones
por línea y mes en 2026** en la red de autobuses interurbanos Bizkaibus (Bizkaia, España).

## Datos
- **Fuente**: Open Data Bizkaia (CTB)
- **Período**: enero 2020 – diciembre 2025
- **Granularidad**: mensual por línea (104 líneas)
- **Variables**: viajeros por tipo de título (Creditrans, Gizatrans, Gazte 70, GORO...) + expediciones

## Estructura del proyecto

```
src/
├── notebooks/
│   ├── 01_preprocessing.ipynb          ← Consolidación y feature engineering
│   ├── 02_eda_series_temporales.ipynb  ← EDA, estacionariedad, ACF/PACF
│   ├── 03_modelo_prophet.ipynb         ← Prophet por línea con regressors
│   ├── 04_modelo_sarima.ipynb          ← SARIMA(1,1,1)(1,1,1)[12] por línea
│   ├── 05_modelo_xgboost.ipynb         ← XGBoost con features de lag
│   ├── 06_comparativa_modelos.ipynb    ← Comparativa MAE/RMSE/MAPE + selección
│   └── 07_contrafactual_subsidio.ipynb ← Análisis sin subsidio 50%
├── data/
│   ├── bizkaibus/                      ← CSVs originales de viajeros
│   ├── expediciones/                   ← CSVs originales de expediciones
│   ├── train.csv                       ← 2020–2024 (entrenamiento)
│   ├── test.csv                        ← 2025 (hold-out)
│   ├── train_merged.csv                ← Dataset completo con features
│   └── predicciones_2026_FINAL.csv     ← Predicciones del modelo ganador
├── model/
│   └── production/                     ← Modelo final serializado
└── utils/                              ← Funciones auxiliares
resources/
└── img/                                ← Visualizaciones exportadas
```

## Modelos evaluados
| Modelo | Descripción |
|---|---|
| **Prophet** | Modelo de Facebook, estacionalidad multiplicativa + regressores (COVID, subsidio) |
| **SARIMA(1,1,1)(1,1,1)[12]** | Modelo clásico de series temporales con componente estacional anual |
| **XGBoost** | Regresión con features de lag, rolling means y variables temporales |

**Evaluación**: MAE, RMSE y MAPE sobre hold-out 2025 (enero–diciembre).  
**Selección**: modelo con menor MAPE mediano entre líneas.

## Análisis contrafactual
Se entrena un modelo Prophet **exclusivamente con datos pre-subsidio** (ene 2020 – ago 2022)
y se proyecta hasta 2025 para estimar cómo habrían evolucionado los viajeros **sin el subsidio
del 50%** implantado en septiembre 2022. La diferencia entre la proyección y los datos reales
cuantifica el efecto atribuible al subsidio.

## Requisitos
```bash
pip install pandas numpy matplotlib seaborn prophet statsmodels xgboost scikit-learn nbformat
```

## Ejecución
Ejecutar los notebooks en orden (01 → 07) desde la carpeta `src/`.
