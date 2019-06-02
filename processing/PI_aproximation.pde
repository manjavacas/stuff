// PI aproximation using Monte Carlo method

int N = 0;
int IN = 0;
float BEST = 0;

void setup() {
  size(600, 600);
  noStroke();
  shapeMode(CENTER);
  circle(width/2, height/2, width);
}

void draw() {
  float r = width/2;
  float x0 = random(width);
  float y0 = random(height);

  if (dist(x0, y0, r, r) <= r) {
    fill(0, 0, 255);
    IN++;
  } else {
    fill(255, 0, 0);
  }
  circle(x0, y0, 2);
  N++;
  float pi = 4.0 * (float)IN / (float)N;

  // show the closest aproximation
  if (abs(PI - pi) < abs(PI - BEST)) {
    BEST = pi;
    print(BEST + "\n");
  }
}
