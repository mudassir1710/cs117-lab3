# cs117-lab3
## 1. Assembly Reflections
- **Registers and Instructions:**  
  In Assembly, variables are stored in registers (like `AX`, `BX`, `EAX`), and instructions must explicitly specify each operation. Every step (loading data, performing arithmetic, storing results) must be written out in detail.  

- **Difference from Python:**  
  Coding in Assembly is very low-level and close to the hardware, requiring detailed instructions. In contrast, Python is high-level and abstracts away most of the hardware details, making it much easier and faster to write and understand.

---

## 2. Python Reflections
- **Why Python is easier/faster:**  
  Python is easier because it handles memory management, variable storage, and many operations automatically. It allows developers to focus on problem-solving instead of worrying about hardware-level details.  

- **Helpful Python Features:**  
  - **Variables**: No need to declare data types explicitly.  
  - **Functions**: Encapsulate reusable logic.  
  - **Loops**: Provide simple iteration structures without manual jump instructions.  
  - **Libraries**: Built-in modules simplify complex tasks.

---

## 3. Comparison Table

| Feature            | Assembly Example   | Python Example | Notes |
|--------------------|--------------------|----------------|-------|
| Variable storage   | `MOV AX, 5` (Register EAX) | `x = 5`       | Python automatically allocates memory, Assembly requires registers |
| Printing output    | `INT 21h`          | `print()`      | Python provides a built-in print function, Assembly uses interrupts |
| Arithmetic         | `ADD AX, BX`       | `x + y`        | Python handles operations directly, Assembly requires explicit register usage |
