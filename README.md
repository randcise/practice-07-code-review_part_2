

```md id="readme_final"
# 🛒 CartService Refactoring Project

## 📌 Project Overview

This project demonstrates a complete step-by-step refactoring of a legacy **Shopping Cart Service** using Python and pytest.

The main goal was to transform a "God Object" into a clean, modular, and testable architecture while preserving original behavior through characterization tests.

---

## 🎯 Objectives

- Refactor legacy CartService step by step
- Introduce separation of concerns
- Improve code readability and maintainability
- Add validation and error handling
- Ensure full test coverage with pytest
- Maintain backward compatibility

---

## 🏗️ Project Structure

```

practice-07-code-review_part_2/
│
├── src/
│   ├── cart_service.py
│   ├── discount_calculator.py
│   ├── shipping_calculator.py
│   ├── validator.py
│   └── **init**.py
│
├── original/
│   └── cart_service.py
│
├── tests/
│   ├── characterization/
│   │   └── test_cart_characterization.py
│   │
│   ├── unit/
│   │   ├── test_validator.py
│   │   └── test_async_cart.py
│   │
│   └── **init**.py
│
├── refactoring-journal.md
├── requirements.txt
└── README.md

````

---

## ⚙️ Features

- Add items to cart with validation
- Calculate total price with user-based discounts
- Calculate shipping cost based on quantity
- Safe JSON storage handling (save/load cart)
- Input validation layer to prevent invalid data
- Modular architecture (separated responsibilities)

---

## 🧪 Testing Strategy

This project uses **pytest** and follows two testing approaches:

### 1. Characterization Tests
- Capture existing behavior before refactoring
- Ensure no breaking changes during development

### 2. Unit Tests
- Test individual components (Validator, calculations)
- Validate edge cases and error handling

---

## ▶️ How to Run the Project

### Install dependencies:
```bash
pip install -r requirements.txt
````

### Run tests:

```bash
pytest -v
```

---

## 📊 Test Coverage Goals

* Minimum 80% code coverage
* All critical business logic tested
* Edge cases included (invalid input, empty cart, etc.)

---

## 🧠 Key Refactoring Improvements

* Extracted `DiscountCalculator` from monolithic service
* Extracted `ShippingCalculator` for shipping logic
* Introduced `Validator` for input validation
* Removed duplicated logic
* Replaced magic numbers with constants
* Improved error handling with try/except
* Simplified calculation logic using Python built-ins (`sum`)

---

## 📈 Result

After refactoring:

* Clean modular architecture
* Improved maintainability
* Better testability
* Safer input handling
* Clear separation of responsibilities

---

## 👨‍💻 Author Notes

This project was completed as part of a software engineering practice task focused on:

* legacy code refactoring
* test-driven safety (characterization tests)
* incremental improvements using Git commits

```

