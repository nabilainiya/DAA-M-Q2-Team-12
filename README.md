# Treasure Quest 🗺️

**Treasure Quest** is a Python-based ASCII terminal adventure game that demonstrates the application of graph traversal and shortest-path algorithms through an interactive treasure-hunting experience.

Players explore different maze levels, collect hidden treasures, and find their way to the exit. The game also provides an Algorithm Assistant that visualizes how **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and **Dijkstra's Algorithm** explore the map and determine possible paths.

The project aims to demonstrate how different algorithms solve pathfinding problems, particularly the differences between finding the shortest path in terms of steps and finding the minimum-cost path in a weighted environment.

---

## Table of Contents

- [Features](#features)
- [Algorithms Implemented](#algorithms-implemented)
- [Game Levels](#game-levels)
- [Game Mechanics](#game-mechanics)
- [Controls](#controls)
- [Scoring System](#scoring-system)
- [Installation and Setup](#installation-and-setup)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [Team Members](#team-members)

---

## Features

- **Interactive ASCII Game:** Explore maze environments through a terminal-based interface.
- **Multiple Treasure Collection:** Collect multiple treasures in each level before reaching the exit.
- **Three Pathfinding Algorithms:** Explore the behavior of BFS, DFS, and Dijkstra's Algorithm.
- **Algorithm Visualization:** Observe visited nodes and suggested paths through terminal animations.
- **Weighted Terrain:** Navigate through different terrain types with varying movement costs.
- **Multiple Levels:** Experience three progressively challenging maze environments.
- **Algorithm Comparison:** Compare the number of steps and total movement costs produced by different algorithms.
- **Scoring System:** Earn points by collecting treasures and completing levels.
- **Automated Testing:** Verify algorithm behavior and important game scenarios through unit tests.

---

## Algorithms Implemented

Treasure Quest implements three fundamental graph algorithms to demonstrate different approaches to pathfinding.

### 1. Breadth-First Search (BFS)

BFS explores the graph level by level using a **Queue (First In, First Out)** data structure.

- Finds the path with the fewest number of steps in an unweighted graph.
- Explores neighboring nodes before moving to nodes further away.
- Suitable for finding the minimum-step path when all movements have equal costs.

### 2. Depth-First Search (DFS)

DFS explores as far as possible along one branch before backtracking, using a **Stack (Last In, First Out)** approach.

- Explores paths deeply before considering alternative branches.
- Uses backtracking to continue exploring unexplored areas.
- Can be used to explore the map and locate reachable treasures.
- Does not guarantee the shortest path.

### 3. Dijkstra's Algorithm

Dijkstra's Algorithm finds the minimum-cost path in a weighted graph using a **Priority Queue**.

- Considers the movement cost of each terrain type.
- Prioritizes paths with the lowest accumulated cost.
- Can choose a path with more steps if its total movement cost is lower.
- Suitable for environments where different movements have different costs.

### Algorithm Comparison

| Algorithm | Data Structure | Main Objective | Considers Terrain Cost |
|---|---|---|---|
| BFS | Queue | Find the fewest steps | No |
| DFS | Stack | Explore paths deeply | No |
| Dijkstra | Priority Queue | Find the minimum-cost path | Yes |

**Example:**

In Level 3 (Swamp Crossing), the algorithms demonstrate different pathfinding results when navigating weighted terrain:

| Algorithm | Path Length | Total Cost |
|---|---:|---:|
| BFS | 8 steps | 14 |
| Dijkstra | 12 steps | 12 |

This example illustrates that the path with the fewest steps is not necessarily the path with the lowest total movement cost.

---

## Game Levels

The game consists of three predefined levels with different maze layouts and terrain configurations.

| Level | Name | Description |
|---|---|---|
| 1 | Shallow Cove | An introductory level that introduces players to the basic mechanics of treasure collection and navigation. |
| 2 | Sunken Maze | A more challenging maze that requires players to navigate through a more complex environment. |
| 3 | Swamp Crossing | A weighted environment that demonstrates the differences between minimum-step and minimum-cost pathfinding. |

Each level contains a starting position, multiple treasures, obstacles, and an exit.

---

## Game Mechanics

### Map Representation

The game world is represented as a two-dimensional grid. Each cell represents a specific position in the environment.

The map contains different types of cells, including:

- Walkable terrain
- Obstacles and walls
- Treasure locations
- Player starting position
- Exit location

The grid is used as the basis for graph representation and pathfinding operations.

### Terrain Costs

Different terrain types have different movement costs.

| Terrain | Symbol | Movement Cost |
|---|---|---:|
| Grass | `.` | 1 |
| Sand | `:` | 2 |
| Swamp | `~` | 3 |
| Wall | `#` | Impassable |

These movement costs are particularly important for Dijkstra's Algorithm, which calculates the minimum accumulated cost rather than simply minimizing the number of steps.

### Treasure Collection

- Treasures are collected automatically when the player moves onto their locations.
- All treasures in the current level must be collected before the exit can be accessed.
- The player must reach the exit after collecting all treasures to complete the level.

### Algorithm Assistant

The Algorithm Assistant provides visual guidance for exploring the map.

Players can select one of the available algorithms to observe its exploration process and suggested path.

The algorithm visualization serves as an assistance feature. Players retain control over their movement and are not automatically moved along the suggested path.

---

## Controls

The following keyboard controls are available during gameplay.

| Key | Action |
|---|---|
| `W` / `↑` | Move Up |
| `A` / `←` | Move Left |
| `S` / `↓` | Move Down |
| `D` / `→` | Move Right |
| `1` | Select BFS |
| `2` | Select DFS |
| `3` | Select Dijkstra's Algorithm |
| `T` | Switch Target |
| `P` | Pause Algorithm Animation |
| `C` | Clear or Stop Visualization |
| `R` | Restart Current Level |
| `M` | Return to Main Menu |

---

## Scoring System

The player's score is calculated based on the number of treasures collected and whether the level is completed without restarting.

The scoring formula is:

**Score = (100 × T) + 500 + B**

Where:

- `T` = Number of treasures collected.
- `500` = Base completion points.
- `B` = Bonus points.

The restart bonus is calculated as follows:

| Condition | Bonus |
|---|---:|
| Level completed without restarting | 200 points |
| Level completed after restarting | 0 points |

For example, completing a level with two treasures without restarting gives:

`Score = (100 × 2) + 500 + 200`

`Score = 900 points`

---

## Installation and Setup

### Prerequisites

Before running the project, make sure you have:

- Python 3.8 or later.
- Git (optional, for cloning the repository).
- A terminal or command-line interface.

The project uses Python's standard libraries for its main functionality.

### 1. Clone the Repository

```bash
git clone https://github.com/nabilainiya/DAA-M-Q2-Team-12
```

Navigate to the project directory:

```bash
cd DAA-M-Q2-Team-12
```

### 2. Verify Python Installation

Check whether Python is installed:

```bash
python --version
```

Alternatively, on Windows:

```bash
py --version
```

---

## How to Run

From the project's root directory, execute:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

The main menu will appear in the terminal. Follow the on-screen instructions to start playing.

---

## Project Structure

```text
DAA-M-Q2-Team-12/
│
├── main.py
│
├── tq/
│   ├── __init__.py
│   ├── game.py
│   ├── graph.py
│   ├── maps.py
│   ├── render.py
│   ├── term.py
│   │
│   └── algorithms/
│       ├── __init__.py
│       ├── bfs.py
│       ├── dfs.py
│       └── dijkstra.py
│
├── tests/
│   └── test_algorithms.py
│
└── README.md
```

### Module Description

| File / Directory | Description |
|---|---|
| `main.py` | Main application entry point and game loop. |
| `tq/game.py` | Handles game mechanics, player movement, treasure collection, and scoring. |
| `tq/graph.py` | Provides graph representation and grid-related graph operations. |
| `tq/maps.py` | Defines the predefined game levels and map configurations. |
| `tq/render.py` | Handles map rendering and algorithm visualization in the terminal. |
| `tq/term.py` | Provides terminal utilities and keyboard input handling. |
| `tq/algorithms/bfs.py` | Implements Breadth-First Search. |
| `tq/algorithms/dfs.py` | Implements Depth-First Search. |
| `tq/algorithms/dijkstra.py` | Implements Dijkstra's Algorithm. |
| `tq/algorithms/__init__.py` | Initializes the algorithms package. |
| `tests/test_algorithms.py` | Contains automated tests for algorithms and selected game scenarios. |

---

## Testing

Automated tests are provided to verify the correctness of the implemented algorithms and selected game mechanics.

The test suite covers the following scenarios:

| Test Case | Description |
|---|---|
| `test_bfs_vs_dijkstra_level3` | Compares BFS and Dijkstra's path length and total cost in Level 3. |
| `test_all_targets_reachable_and_dfs_finds_all` | Verifies that all targets are reachable and DFS can locate all remaining treasures. |
| `test_full_playthrough_score` | Verifies successful level completion and the expected scoring calculation. |
| `test_wall_collision` | Ensures that the player cannot move through walls. |

### Running the Tests

Install `pytest` if it is not already installed:

```bash
python -m pip install pytest
```

Run the test suite from the project root directory:

```bash
python -m pytest tests/ -v
```

---

## Technologies Used

- **Programming Language:** Python
- **Interface:** ASCII Terminal
- **Algorithms:** Breadth-First Search (BFS), Depth-First Search (DFS), and Dijkstra's Algorithm
- **Data Structures:** Queue, Stack, Priority Queue, and Graph
- **Testing:** Python automated testing with pytest
- **Version Control:** Git and GitHub

---

## Team Members

This project was developed collaboratively as part of the Design and Analysis of Algorithms (DAA) course.

| Team Member | Main Responsibility |
|---|---|
| Selly Aisyah | User Interface and Terminal Rendering |
| Nabila Ainiya Rahman | Graph Representation and Pathfinding Algorithms |
| Muhammad Hanif Nasrullah | Game Mechanics and Level Design |

---
