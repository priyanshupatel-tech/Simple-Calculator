# 🧮 Simple Calculator
 
A beginner-friendly command-line **Calculator** built with Python that performs all basic arithmetic operations with proper input validation and error handling.
 
---
 
## 🚀 Features
 
- ➕ Addition of two numbers
- ➖ Subtraction of two numbers
- ✖️ Multiplication of two numbers
- ➗ Division of two numbers
- ⚠️ Handles **Division by Zero** error gracefully
- ✅ Input validation — only numeric values accepted
- 🔁 Continuous loop — calculate multiple times in one session
- 🚪 Clean exit with Thank You message
---
 
## 🛠️ Technologies Used
 
- **Language:** Python 3
- **Concepts:** Loops, Conditionals, Exception Handling (`try-except`), Input Validation
- **Errors Handled:** `ZeroDivisionError`, `ValueError`
---
 
## 📌 How to Run
 
1. Clone the repository:
   ```bash
   git clone https://github.com/priyanshupatel-tech/Simple-Calculator.git
   cd Simple-Calculator
   ```
 
2. Run the program:
   ```bash
   python calculator.py
   ```
 
3. Choose an operation and enter your numbers!
---
 
## 🖥️ Menu Options
 
```
=================================== Simple Calculator ====================================
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
```
 
---
 
## 🖥️ Sample Output
 
```
Enter your Choice= 1
Enter your first number= 25
Enter your second number= 17
 
-------------------------------------------------------------------------------------
Addition of 25 and 17 = 42
-------------------------------------------------------------------------------------
```
 
```
Enter your Choice= 4
Enter your first number= 10
Enter your second number= 0
 
-------------------------------------------------------------------------------------
Number can't be divided by zero
-------------------------------------------------------------------------------------
```
 
---
 
## 🛡️ Error Handling
 
| Error | Situation | What Happens |
|-------|-----------|--------------|
| `ZeroDivisionError` | Dividing any number by 0 | Friendly error message shown |
| `ValueError` | User enters text instead of number | "Please give only numerical value" message shown |
| Invalid choice | Number outside 1–5 | "Please give Correct Choice Number" message shown |
 
---
 
## 📂 Project Structure
 
```
Simple-Calculator/
│
├── calculator.py    # Main application file
└── README.md
```
 
---
 
## 💡 Learning Outcomes
 
- Implementing arithmetic operations in Python
- Using `try-except` for robust error handling
- Building a loop-based menu-driven CLI app
- Handling multiple exception types (`ZeroDivisionError`, `ValueError`)
- Writing clean, readable conditional logic
---
 
## 👨‍💻 Author
 
**Priyanshu Patel**
- 🔗 [LinkedIn](https://www.linkedin.com/in/priyanshupatel-tech/)
- 💻 [GitHub](https://github.com/priyanshupatel-tech)
