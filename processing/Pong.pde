// Single-player Pong game
// Antonio.Manjavacas

// Start game by clicking or pushing ENTER

float x, y, vx, vy, t;
float r;
float posRecX, posRecY, recLen;
int counter;
boolean end;

void setup() {
  size(600, 600);
  rectMode(CENTER);
  ellipseMode(CENTER);
  background(0, 0, 0);
  noLoop();
  init();
}

void draw() {
  background(0, 0, 0);
  if ((x < 10) || (x > (width - 10))) 
    vx = -vx;

  if ((y < 10) || collision()) 
    vy = -vy;

  // the ball goes down
  if (y > (height - r)) {
    textSize(20);
    text("Score: " + counter, 50, 50);
    textSize(40);
    textAlign(CENTER, CENTER);
    fill(255, 255, 255);
    text("GAME OVER", width/2, height/2);
    textSize(20);
    text("Press ENTER or click to restart", width/2, height/2 + 50);
    end = true;
    noLoop();
  }

  // new position
  x = x + vx * t;
  y = y + vy * t;

  if (!end) {
    text(counter, 50, 50);
  }

  ellipse(x, y, r, r);
  rect(posRecX, posRecY, recLen, 10);
}

// restart game
void mousePressed() {
  init();
  loop();
}

void keyPressed() {
  switch (keyCode) {
  case RIGHT: 
    applyOffset(20);
    break;
  case LEFT:
    applyOffset(-20);
    break;
  case ENTER:
    init();
    loop();
    break;
  }
}

// update rectangle position
void applyOffset(float offset) {
  float newPos = posRecX + offset;
  // check borders
  if (newPos >= recLen/2 && newPos <= width - recLen/2)
    posRecX = newPos;
}

// check if bounce
boolean collision() {
  boolean bounce = false;
  if ((y >= posRecY - r) && (x <= posRecX + recLen) && (x >= posRecX - recLen)) {
    bounce = true;
    counter++;
  }
  return bounce;
}

// initialize variables
void init() {

  textSize(12);

  x = width/2;
  y = 10;
  t = 1;

  // randomize speeds
  do {
    vx = random(3, 5);
    vy = random(3, 5);
  } while (vx == vy);

  // ball
  r = 20;

  // rectangle
  posRecX = width/2;
  posRecY = height - 20;
  recLen = 100;

  // game settings
  counter = 0;
  end = false;
}
