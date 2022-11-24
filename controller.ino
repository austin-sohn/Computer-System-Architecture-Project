//Controller Code
//Ethan Luu
//Austin Sohn

uint8_t buf[8] = { 0 };   //Keyboard report buffer

#define PIN_W 4 // Pin for w
#define PIN_S 5 // Pin for s
#define PIN_O 6 // Pin for o
#define PIN_L 7 // Pin for l

void setup() {
  Serial.begin(9600); // Setup Serial communication

  //Set pinmode of Input pins
  pinMode(PIN_W, INPUT);
  pinMode(PIN_S, INPUT);
  pinMode(PIN_O, INPUT);
  pinMode(PIN_L, INPUT);
}

void loop() {
//When button representing W is pressed  
  if (digitalRead(PIN_W) == HIGH) { 
    buf[2] = 26;   // W keycode
    Serial.write(buf, 8); // Send keypress
   // Serial.println("W");
    releaseKey();
  }
   
//When button representing S is pressed
  if (digitalRead(PIN_S) == HIGH) {
    buf[2] = 22;   // S keycode
    Serial.write(buf, 8); // Send keypress
   // Serial.println("S");
    releaseKey();
  } 
  
//When button representing O is pressed
  if (digitalRead(PIN_O) == HIGH) {
    buf[2] = 18;   // O keycode
    Serial.write(buf, 8); // Send keypress
   // Serial.println("O");
    releaseKey();
  } 
  
//When button representing L is pressed
  if (digitalRead(PIN_L) == HIGH) {
    buf[2] = 15;   // L keycode
    Serial.write(buf, 8); // Send keypress
  //  Serial.println("L");
    releaseKey();
  } 
  
}
// Function for Key Release
void releaseKey() 
{
  buf[0] = 0;
  buf[2] = 0;
  Serial.write(buf, 8); // Send Release key  
}