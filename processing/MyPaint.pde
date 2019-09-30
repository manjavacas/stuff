
// Antonio Manjavacas
// Sistemas Interactivos 2019

// icon selection flags
boolean selLine = false;
boolean selRect = false;
boolean selCirc = false;
boolean selText = false;

// icon colors
color COL_SEL = color(255, 200, 0);
color COL_DEF = color(135, 206, 235);
color COL_CB = color(216, 191, 216);

// point saving variables;
int x1, x2;
int y1, y2;

// input text
String str = " ";

void setup() {
  size(600, 500);
  background(255, 255, 255);
  setupIcons(COL_DEF, COL_DEF, COL_DEF, COL_DEF);
}

void draw() {
  // cursor updating
  updateCursor();

  // text input
  if (selText) {
    fill(0, 0, 0);
    String oldStr = str;
    text(oldStr, x1, y1);
  }
}

void mouseClicked() {
  // update icons
  checkIcons();
}

void mousePressed() {
  // update text variable
  str = "";
  // save current position
  if (mouseX > 100) {
    x1 = mouseX;
    y1 = mouseY;
  }
}

void mouseReleased() {

  // save current position
  if (mouseX > 100) {
    x2 = mouseX;
    y2 = mouseY;
  }

  // painting function
  paint();
}

// text input
void keyPressed() {
    str = str + key;
}

// paints on kanvas
void paint() {
  // if coordinates are in the kanvas...
  if (x1 > 100 && x2 > 100) {
    // DRAW LINE
    if (selLine) {
      fill(0, 0, 0);
      line(x1, y1, x2, y2);
    }
    // DRAW RECTANGLE
    if (selRect) {
      noFill();
      rectMode(CORNERS);
      rect(x1, y1, x2, y2);
    } 
    // DRAW CIRCLE
    if (selCirc) {
      noFill();
      ellipseMode(CORNERS);
      ellipse(x1, y1, x2, y2);
    }
  }
}

// update cursor icon
void updateCursor() {
  if (mouseX <= 100) {
    cursor(HAND);
  } else {
    cursor(CROSS);
  }
}

// check current selected icon
void checkIcons() {
  if (mouseX <= 100) {
    if (0 <= mouseY && mouseY < 100) {
      setupIcons(COL_SEL, COL_DEF, COL_DEF, COL_DEF);
      selLine = true;
      selRect = false;
      selCirc = false;
      selText = false;
    } else if (100 <= mouseY && mouseY < 200) {
      setupIcons(COL_DEF, COL_SEL, COL_DEF, COL_DEF);
      selLine = false;
      selRect = true;
      selCirc = false;
      selText = false;
    } else if (200 <= mouseY && mouseY < 300) {
      setupIcons(COL_DEF, COL_DEF, COL_SEL, COL_DEF);
      selLine = false; 
      selRect = false;
      selCirc = true; 
      selText = false;
    } else if (300 <= mouseY && mouseY < 400) {
      setupIcons(COL_DEF, COL_DEF, COL_DEF, COL_SEL);
      selLine = false;
      selRect = false;
      selCirc = false;
      selText = true;
    } else {
      background(255, 255, 255);
      setupIcons(COL_DEF, COL_DEF, COL_DEF, COL_DEF);
      selLine = false;
      selRect = false;
      selCirc = false;
      selText = false;
    }
  }
}

// set toolbar
void setupIcons(int cLine, int cRect, int cCirc, int cText) {

  rectMode(CORNER);
  ellipseMode(RADIUS);

  // drawing buttons
  fill(cLine);
  rect(0, 0, 100, 100);
  fill(cRect);
  rect(0, 100, 100, 100);
  fill(cCirc);
  rect(0, 200, 100, 100);
  fill(cText);
  rect(0, 300, 100, 100);

  // clean button
  fill(COL_CB);
  rect(0, 400, 100, 100);

  // line icon
  fill(0, 0, 0);
  line(20, 20, 80, 80);

  // rectangle icon
  fill(COL_DEF);
  rect(25, 125, 50, 50);

  // circle icon
  fill(COL_DEF);
  ellipseMode(CENTER);
  circle(50, 250, 40);

  // text icon
  fill(0, 0, 0);
  textSize(24);
  text("Text", 24, 360);

  // clean icon
  fill(0, 0, 0);
  textSize(24);
  text("Clean", 18, 460);
}
