# Solución para el Cálculo de Tarifa de Estacionamiento (Parking Bill)

Se generaron dos implementaciones para calcular el costo total de un ticket de estacionamiento dadas la hora de entrada y la de salida. Ejercicio de Codility.

## Descripción del Problema

Dadas las cadenas de tiempo de entrada `E` y salida `L` en formato `"HH:MM"` del mismo día:
- Tarifa de entrada: 2
- Primera hora (completa o fracción): 3
- Cada hora sucesiva (completa o fracción): 4

Devuelve el costo total del boleto de estacionamiento.

### Ejemplo

Entrada: `E = "10:00"`, `L = "13:21"`
Tiempo: 3 horas y 21 minutos -> equivale a 4 horas facturables.
Cálculo: Tarifa entrada (2) + 1ª hora (3) + 3 horas siguientes (3 * 4 = 12) = 17.
Salida: `17`
