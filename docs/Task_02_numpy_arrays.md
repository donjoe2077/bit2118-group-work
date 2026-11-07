# Task 02 – NumPy Arrays and Numerical Computation

**Concept:** an array stores many numbers together so one operation acts on every element.
**Code:** `code/Task_02_numpy_arrays.py` · **Extension:** `extensions/Task_02_ext_soil_moisture.py`

## B. Inputs and mathematical operations
- **Input:** 24 hourly temperatures in °C (`temperatures_c`).
- **Operations:** mean = sum / 24, minimum, maximum, and the conversion F = 1.8·C + 32 applied to the whole array at once (vectorized, no loop).

## Output of the original program
```
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```

## C. Changing an input
Every reading was raised by 3 °C (sensor moved to a sunnier spot). Result: mean 23.12 → 26.12 °C, minimum 17.50 → 20.50 °C, maximum 29.40 → 32.40 °C. All three moved by exactly 3 °C, while the standard deviation stayed 4.174 °C. Adding a constant shifts the data but does not change how spread out it is.

## D. Interpretation
The day's average is about 23 °C. The coolest hour (17.5 °C) is in the early morning and the warmest (29.4 °C) is around midday, so the temperature swing is about 12 °C. The Fahrenheit values (about 64–66 °F at night) are the same readings on a different scale.

## E. New case – greenhouse soil moisture
- **Assumptions:** 24 hourly moisture readings (%, illustrative values), irrigation at hour 6, crops are stressed below 30 %.
- **Method:** a boolean mask `moisture < 30` selects the stressed hours; min–max normalisation is applied to the whole array.
- **Output:** mean 32.46 %, minimum 25 %, maximum 45 %. 8 hours are below 30 % (hours 16–23), which is 33.3 % of the day.
- **Interpretation:** moisture jumps after irrigation and then dries steadily; the plants spend the last 8 hours of the day stressed, so irrigation should be repeated in the late afternoon.
