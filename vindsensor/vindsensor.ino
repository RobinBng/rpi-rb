const float VREF = 1.10;   // INTERNAL reference
const float DIV_RATIO = 2.0; // Change depending on voltage divider
int raw;

void setup() {
  Serial.begin(9600);
  analogReference(INTERNAL);      // use the ~1.1V internal reference
  delay(5);
}

void loop() {
  // Read voltage
  raw = analogRead(A0);
  float v_adc = (raw / 1023.0) * VREF;  // voltage at ADC pin (after divider)
  float v_in   = v_adc * DIV_RATIO;     // original input voltage (before divider)

// Wind speed calculation from sensor voltage:
// Sensor outputs 0.4 V at 0 m/s and 2.0 V at 32.4 m/s
// Step size: 0.1 m/s => 32.4 / 0.1 = 324 steps
// Voltage span: 2.0 - 0.4 = 1.6 V
// Voltage per step: 1.6 / 324 ~ 0.00494 V/step ~ 4.94 mV/step
// Factor: 0.1 / 0.00494 ~ 20.25
// Formula: wind_speed = (v_in - 0.4) * 20.25
  float wind_speed = (v_in - 0.4) * 20.25; 



//  Serial.print("raw: "); Serial.print(raw);
//  Serial.print("  Vadc: "); Serial.print(v_adc, 4);
//  Serial.print("  Vin: "); Serial.print(v_in, 4);
  Serial.print("  Wind speed: "); Serial.print(wind_speed, 1); Serial.println(" m/s");

  delay(1000);
}
