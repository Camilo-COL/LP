/*|*
 * Comportamiento: según la intensidad del sonido, se encienden más o menos bombilloss
 * (efecto medidor)
 *
 * Conexiones:
 * - Módulo sensor de sonido (salida analógica) -> A0
 * - LEDs con resistencia 220Ω: pin 2, 3, 4, 5, 6
 */

const int PIN_SENSOR = A0;
const int NUM_LEDS = 5;
const int ledPins[NUM_LEDS] = {2, 3, 4, 5, 6};

// Rango de valores del sensor para los LEDs
const int valorMin = 50;   // mínimo 
const int valorMax = 500;  //  máximo (ajustar según sensor)

void setup() {
  for (int i = 0; i < NUM_LEDS; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
  pinMode(PIN_SENSOR, INPUT);
}

void loop() {
  int sonido = analogRead(PIN_SENSOR);
  
  // Mapear sonido (0-1023) a cantidad de LEDs (0-5)
  int ledsEncendidos = map(sonido, valorMin, valorMax, 0, NUM_LEDS);
  ledsEncendidos = constrain(ledsEncendidos, 0, NUM_LEDS);
  
  // Encender/apagar LEDs según la intensidad
  for (int i = 0; i < NUM_LEDS; i++) {
    if (i < ledsEncendidos) {
      digitalWrite(ledPins[i], HIGH);
    } else {
      digitalWrite(ledPins[i], LOW);
    }
  }
}
