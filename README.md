# Campus Item Borrowing Management System
## 1. Project Overview
Designed for campus scenarios, this system implements core functions including item borrowing, return, inventory management, and borrowing record tracking. It follows OOP principles: encapsulation, inheritance, and modularization. An additional min-heap and heap sort algorithm are implemented as the algorithm self-study task.
## 2. Features
### (1). Item Management
- Add items, check item status (available/borrowed)
### (2). User System
- User/Admin roles (Admin inherits from User base class)
### (3). Core Operations
- Borrow item, return item, record operation logs
### (4). Algorithm Module
- Min-heap implementatoin + Heap sort algorithm (self-study content)
### (5). Interface
- Console menu-based interaction, simple and user-friendly
## 3. Flie Structure 
- campus-borrow-system/
- |-- item.py
- |-- user.py
- |-- borrow_system.py
- |-- heap_study.py
- |-- main.py
- |-- README.md
## 4. Technical Hightlights
### (1). Object-Oriented Programming
- Encapsulatoin: Private attributes + public getter methods
- Inheritance: Admin class inherits User class, overrides role judgement method
### (2). Data Structures
- Dictionaries for storing items and users for effficient lookup
- Lists for storing borrowing/return records
### (3). Algorithm Implementation
- Min-heap (insert, heapify up, heapify down, extract min)
- Heap-sort (ascending sorting based on min-heap)
### (4). Modular Design
- Files spit by responsibility, low coupling, easy maintenance and extansion
## 5. Environment Requirements
- Python 3.6 +
- No third-party dependencies; runs with stansard libraries only
## 6. Quick Start
### (1). Clone/Download the Project
```
git clone https://github.com/your-username/campus-borow-system.git
cd campus-borrow-system
```
### (2). Run the Main System
```
python main.py
```
### 
- Built-in test data: Admin A001, Student S001, Items I001 (Power Bank), I002 (Umbrella)
### 
- Operate via menu prompts: view items, borow, return, check records
### (3). Run the Heap Sort Study Module
```
python heap_study.py
```
- Prints original and sorted test array to verify algorithm correctness
## 7. System Operation Guide
- Menu options after running ``` main.py```:
### (1). View all items: 
- Show ID, name, category, and status of items
### (2). Borrow item:
- Enter user ID and item ID to borrow (fails if already borrowed or items does not exist)
### (3). Return item:
- Enter user ID to return (fails if not borrowed)
### (4). View records:
- Show all borrowing and return operation records
### (5). Exit system:
- Terminate the program
## 8. Heap Sort Module Introduction
Contents implemented in heap_study.py:
- MinHeap class: Core min-heap operations (insert, extract_min, heapify_up/down)
- heap_sort function: Heap sort based on min-heap, time complexity O(n log n)
- Test case: [8, 3, 5, 1, 10, 2], outputs sorted result
## 9. Submission Compliance
This project fully matches the COMP 2090SEF report requirements；
- Code structure fully aligns with report design
- Complete comments, standardized variable naming, clear logic
- Satisfies assessment criteria: OOP, inheritance, encapsulation, modularization
