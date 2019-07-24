
// Conway's Game of life
// https://en.wikipedia.org/wiki/Conway's_Game_of_Life

// Antonio.Manjavacas

int l = 5;
int pX, pY;
boolean[][] grid;

void setup() {
  size(900, 900);
  pX = width/l;
  pY = height/l;
  grid = createGrid();
  setPlayground(grid);
  // frameRate(1);
}

void draw() {
  boolean[][] tempGrid = copyGrid(grid);
  for (int i = 0; i < pX; i++) {
    for (int j = 0; j < pY; j++) {
      // Check surrounding squares
      int c = checkNeighbours(i, j, tempGrid);
      if (tempGrid[i][j] == true) {   
        // Check if cell dies
        if (c < 2 || c > 3) {
          grid[i][j] = false;
        }
      } else {
        // Check if cell borns
        if (c == 3) {
          grid[i][j] = true;
        }
      }
    }
  }
  setPlayground(grid);
}

// Creates a random initial grid
boolean[][] createGrid() {
  boolean[][] myGrid = new boolean[pX][pY];
  for (int i = 0; i < myGrid.length; i++) {
    for (int j = 0; j < myGrid[i].length; j++) {
      myGrid[i][j] = random(2) < 0.3;
    }
  } 
  return myGrid;
}

// Prints the grid
void setPlayground(boolean[][] myGrid) {
  background(0, 0, 0);
  for (int i = 0; i < pX; i++) {
    for (int j = 0; j < pY; j++) {
      if (myGrid[i][j]) {
        fill(255, 255, 0);
      } else {
        fill(0, 0, 0);
      }
      rect(i*l, j*l, l, l);
    }
  }
}

// Checks the amount of neighbours of a cell
int checkNeighbours(int i, int j, boolean[][] myGrid) {
  int c = 0;
  for (int p = -1; p <= 1; p++) {
    for (int q = -1; q <= 1; q++) {
      if (i+p >= 0 && j+q >= 0 && i+p < myGrid.length && j+q < myGrid.length) {
        if (myGrid[i+p][j+q] == true) {
          c++;
        }
      }
    }
  }

  // Avoids counting itself
  if (myGrid[i][j] == true) {
    c--;
  }

  return c;
}

// Copies a grid
boolean[][] copyGrid(boolean[][] myGrid) {
  boolean[][] copy = new boolean[myGrid.length][myGrid[0].length];
  for (int i = 0; i < myGrid.length; i++) {
    for (int j = 0; j < myGrid[i].length; j++) {
      copy[i][j] = myGrid[i][j];
    }
  }
  return copy;
}
