#include <Arduino.h>
#include <TFT_eSPI.h>

// Hello-world to prove the board, screen and BOOT button work.
// The Spotify, GIF and touch code come after this builds and flashes.

constexpr uint8_t BOOT_BUTTON = 0;

TFT_eSPI tft;

void setup() {
  Serial.begin(115200);
  pinMode(BOOT_BUTTON, INPUT_PULLUP);

  tft.init();
  tft.setRotation(1);  // landscape, 320x240
  tft.fillScreen(TFT_BLACK);
  tft.setTextColor(TFT_GREEN, TFT_BLACK);
  tft.drawCentreString("jam", 160, 100, 4);
  tft.drawCentreString("hello, desk", 160, 140, 2);
}

void loop() {
  if (digitalRead(BOOT_BUTTON) == LOW) {
    tft.fillCircle(160, 200, 10, TFT_GREEN);
  } else {
    tft.fillCircle(160, 200, 10, TFT_BLACK);
  }
  delay(20);
}
