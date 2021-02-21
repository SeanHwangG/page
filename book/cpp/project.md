# Project

## Tic Tac Toe

### main.cpp

```cpp
#include <iostream>
#include <string>

#include "tictactoe.hpp"

int main() {
  TicTacToe game(1000);
  game.start();
}
```

### CmakeLists.txt

```sh
cmake_minimum_required(VERSION 3.0.0)
project(tictactoe)

find_package( OpenCV REQUIRED )

add_executable(main main.cpp)
include_directories(.)

set(LIBS ${OpenCV_LIBS})
target_link_libraries( main ${LIBS} )
```

### board.hpp

```cpp
#pragma once

#include <functional>
#include <map>
#include <string>

#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"

using namespace cv;
using namespace std;

function<void(int event, int r, int c)> callback;

class Board {
 public:
  static void onMouseClick(int event, int r, int c, int flags, void *) { callback(event, r, c); }

  int grid[3][3] = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
  int SIZE;
  Mat board;

  Board(int SIZE) : SIZE(SIZE) {
    namedWindow("board");
    board = Mat::zeros(SIZE, SIZE, CV_8UC3);
    setMouseCallback("board", onMouseClick, &board);

    line(board, Point(0, SIZE / 3), Point(SIZE, SIZE / 3), LINE_CLR, 2);
    line(board, Point(0, SIZE * 2 / 3), Point(SIZE, SIZE * 2 / 3), LINE_CLR, 2);
    line(board, Point(SIZE / 3, 0), Point(SIZE / 3, SIZE), LINE_CLR, 2);
    line(board, Point(SIZE * 2 / 3, 0), Point(SIZE * 2 / 3, SIZE), LINE_CLR, 2);
  }

  void draw(string message) {
    for (int r = 0; r < 3; r++)
      for (int c = 0; c < 3; c++) {
        if (grid[r][c] == 1)
          circle(board, Point(SIZE * r / 3 + SIZE / 6, SIZE * c / 3 + SIZE / 6), SIZE / 6, Scalar(255, 0, 0), -1);
        else if (grid[r][c] == 2)
          circle(board, Point(SIZE * r / 3 + SIZE / 6, SIZE * c / 3 + SIZE / 6), SIZE / 6, Scalar(0, 255, 0), -1);
      }

    putText(board, message, Point(SIZE / 2, SIZE / 2), 2, 2, TEXT_CLR);
    imshow("board", board);
  }

 private:
  const Scalar BG_CLR = Scalar(0, 0, 0);
  const Scalar TEXT_CLR = Scalar(255, 255, 255);
  const Scalar LINE_CLR = Scalar(255, 255, 255);
};
```

### tictactoe.hpp

```cpp
#pragma once

#include <iostream>
#include <map>
#include <string>

#include "board.hpp"

static int BOARD_SIZE = 500;
static Board board = Board(BOARD_SIZE);
enum class Status {
  ENDED = -1,
  PROGRESS = 0,
  WIN_1 = 1,
  WIN_2 = 2,
  DRAW = 3,
};

class TicTacToe {
 public:
  TicTacToe(Board board) : board(board) {
    callback = [&](int event, int r, int c) {
      if (event == EVENT_LBUTTONDOWN)
        if (move(r * 3 / board.SIZE, c * 3 / board.SIZE)) {
          updateStatus();
          turn++;
        }
    };
    status2message = {
        {Status::ENDED, "Aborted"},      {Status::PROGRESS, ""}, {Status::WIN_1, "Player 1 won"},
        {Status::WIN_2, "Player 2 won"}, {Status::DRAW, "Draw"},
    };
  }

  bool move(int row, int col) {
    if (board.grid[row][col] != 0) return false;
    board.grid[row][col] = turn % 2 + 1;
    return true;
  }

  void updateStatus() {
    for (int i = 0; i < 3; i++) {
      int row_count = 0, col_count = 0, ld_count = 0, rd_count = 0;
      for (int j = 0; j < 3; j++) {
        if (board.grid[i][j] == (turn % 2 + 1)) row_count++;
        if (board.grid[j][i] == (turn % 2 + 1)) col_count++;
        if (board.grid[j][j] == (turn % 2 + 1)) ld_count++;
        if (board.grid[2 - j][j] == (turn % 2 + 1)) rd_count++;
      }
      if (row_count == 3 || col_count == 3 || ld_count == 3 || rd_count == 3) {
        status = turn % 2 == 0 ? Status::WIN_1 : Status::WIN_2;
        return;
      }
    }

    for (int i = 0; i < 3; i++)
      for (int j = 0; j < 3; j++)
        if (board.grid[i][j] == 0) {
          status = Status::PROGRESS;
          return;
        }

    status = Status::DRAW;
  }

  void start() {
    turn = 0;
    status = Status::PROGRESS;
    while (status == Status::PROGRESS) {
      int key = waitKey(100);
      if (key == 'q') status = Status::ENDED;
      board.draw(status2message[status]);
    }
    waitKey(-1);
  }

 private:
  int turn;
  Status status;
  Board board;
  map<Status, string> status2message;
};
```

## 2048

### CmakeLists.txt

```sh
cmake_minimum_required(VERSION 3.0.0)
project(2048 CXX)

find_package(OpenCV REQUIRED)

add_executable( 2048 2048.cpp )

set(LIBS ${OpenCV_LIBS})
target_link_libraries( 2048 ${LIBS} )
```

### 2048.cpp

```cpp
#include <algorithm>
#include <vector>

#include "board.h"

using namespace std;

enum class Status { GAMEOVER = -1, PROGRESS = 0 };

static int GSIZE = 4, WSIZE = 500;
static Board board = Board(WSIZE, GSIZE);

Status check_game_status() {
  for (int row = 0; row < GSIZE; row++)
    if (find(board.G[row].begin(), board.G[row].end(), 0) != board.G[row].end()) return Status::PROGRESS;
  return Status::GAMEOVER;
}

void addNewNumber() {
  int row, col;
  do {
    row = rand() % GSIZE;
    col = rand() % GSIZE;
  } while (board.G[row][col] != 0);
  board.G[row][col] = 2;
}

void push_left() {
  for (int j = 0; j < GSIZE; j++) {
    vector<int> old_line = board.G[j];
    vector<int> nonempty, new_line;
    copy_if(old_line.begin(), old_line.end(), back_inserter(nonempty), [](int &value) { return value != 0; });

    bool check;
    for (int number : nonempty) {
      if (check || new_line.empty() || *new_line.rbegin() != number) {
        new_line.push_back(number);
        check = false;
      } else {
        *new_line.rbegin() += number;
        check = true;
      }
    }
    new_line.resize(4, 0);
    board.G[j] = new_line;
  }
}

void rotateCW(vector<vector<int>> &mat, int times) {
  for (int i = 0; i < times; i++)
    for (int x = 0; x < GSIZE / 2; x++)
      for (int y = x; y < GSIZE - x - 1; y++) {
        int temp = mat[x][y];
        mat[x][y] = mat[GSIZE - 1 - y][x];
        mat[GSIZE - 1 - y][x] = mat[GSIZE - 1 - x][GSIZE - 1 - y];
        mat[GSIZE - 1 - x][GSIZE - 1 - y] = mat[y][GSIZE - 1 - x];
        mat[y][GSIZE - 1 - x] = temp;
      }
}

int main() {
  addNewNumber();
  while (check_game_status() == Status::PROGRESS) {
    vector<vector<int>> prev_board = board.G;
    char pressed_key = waitKey(50);
    switch (pressed_key) {
      case 'w':
        rotateCW(board.G, 3);
        push_left();
        rotateCW(board.G, 1);
        break;
      case 's':
        rotateCW(board.G, 1);
        push_left();
        rotateCW(board.G, 3);
        break;
      case 'a':
        push_left();
        break;
      case 'd':
        rotateCW(board.G, 2);
        push_left();
        rotateCW(board.G, 2);
        break;
      case 'q':
        return -1;
      default:
        break;
    }

    if (prev_board != board.G) {
      addNewNumber();
    }
    board.draw();
  }
  return 0;
}
```

### board.cpp

```cpp
#include <iostream>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <string>

using namespace std;
using namespace cv;

enum class Status;
const Scalar BG_CLR = Scalar(0, 0, 0);
const Scalar LINE_CLR = Scalar(255, 255, 255);
const Scalar TEXT_CLR = Scalar(255, 255, 255);

class Board {
 public:
  vector<vector<int>> G;

  Board(int WSIZE, int GSIZE) : WSIZE(WSIZE), GSIZE(GSIZE) {
    namedWindow("board");
    G.resize(GSIZE, vector<int>(GSIZE, 0));
    board = Mat::zeros(WSIZE, WSIZE, CV_8UC3);
  }

  void draw() {
    board = Mat::zeros(WSIZE, WSIZE, CV_8UC3);
    for (int gridNum = 1; gridNum < GSIZE; gridNum++) {
      line(board, Point(0, WSIZE * gridNum / GSIZE), Point(WSIZE, WSIZE * gridNum / GSIZE), LINE_CLR, 2);
      line(board, Point(WSIZE * gridNum / GSIZE, 0), Point(WSIZE * gridNum / GSIZE, WSIZE), LINE_CLR, 2);
    }
    for (int row = 0; row < GSIZE; row++) {
      for (int col = 0; col < GSIZE; col++) {
        if (G[row][col] != 0)
          putText(board, to_string(G[row][col]),
                  Point(col * (WSIZE / GSIZE) + 50 - (to_string(G[row][col]).length() - 1) * 12, row * (WSIZE / GSIZE) + 80), 2,
                  2 - 0.2 * to_string(G[row][col]).length(), TEXT_CLR);
      }
    }
    imshow("board", board);
  }

 private:
  Mat board;
  int GSIZE, WSIZE;
};
```
