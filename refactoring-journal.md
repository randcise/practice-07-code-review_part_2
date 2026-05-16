# Refactoring Journal - CartService (Shopping Cart Refactoring)

---

## Step 1: Extract DiscountCalculator

### Type: Move Logic / Extract Class

### Reason:
The original CartService contained duplicated discount logic inside `calculate_total`. This made the code harder to maintain and violated the Single Responsibility Principle.

---

### AI assistance:
Yes — AI suggested multiple approaches, including full service decomposition, but I chose a lightweight extraction instead of over-engineering the system.

---

### My decision:
I extracted discount logic into a separate `DiscountCalculator` concept (or module) to centralize business rules.

I avoided excessive splitting into multiple services because:
- The system is small
- Discount rules are simple
- Maintainability is sufficient with minimal abstraction

---

### Tests:
- Characterization tests for discount calculations
- Verification of correct totals for different user types (regular, premium, VIP)
- Edge cases for unknown user types

---

## Step 2: Input Validation Layer

### Type: Add Validation / Improve Robustness

### Reason:
The original implementation allowed invalid data (negative price or quantity), which could lead to incorrect cart state and wrong calculations.

---

### AI assistance:
Yes — AI suggested adding schema validation or strict typing, but I implemented a simple validation layer instead.

---

### My decision:
I added validation directly inside `add_item`:

- Prevent negative prices
- Prevent zero or negative quantities

This keeps the solution simple and practical.

---

### Tests:
- Prevent adding invalid items
- Ensure valid items are added correctly
- Edge case tests for boundary values (0, negative numbers)

---

## Step 3: Safe JSON Storage Handling

### Type: Improve Reliability / Error Handling

### Reason:
JSON serialization and file operations were not protected, which could cause runtime crashes if the file is missing or corrupted.

---

### AI assistance:
Yes — AI suggested async storage and repository abstraction, but I kept it synchronous for simplicity.

---

### My decision:
I added `try/except` blocks to:

- `save_cart`
- `load_cart`

Fallback behavior:
- If loading fails → empty cart is used
- If saving fails → error is ignored safely

---

### Tests:
- Load cart from valid JSON
- Handle missing file scenario
- Handle corrupted JSON safely

---

## Step 4: Remove Magic Numbers & Simplify Discount Logic

### Type: Refactor Constants / Improve Readability

### Reason:
Discount values (0.1, 0.15, 0.25) were hardcoded and duplicated, making business rules hard to update.

---

### AI assistance:
Yes — AI suggested using enums or configuration files, but I chose a simple dictionary-based approach.

---

### My decision:
I replaced magic numbers with a `DISCOUNTS` dictionary:

- centralizes business rules
- improves readability
- makes updates easy

---

### Tests:
- Validate correct discount application for all user types
- Ensure default discount is 0 for unknown users

---

## Step 5: Optimize Shipping Calculation

### Type: Refactor Algorithm / Improve Efficiency

### Reason:
Shipping cost calculation used manual loops, making it verbose and less readable.

---

### AI assistance:
Yes — AI suggested advanced functional patterns, but I only used Python built-in `sum()` for simplicity.

---

### My decision:
Replaced loop-based summation with:

- `sum(item["quantity"] for item in self.items)`

This improved readability and reduced complexity.

---

### Tests:
- Empty cart shipping = 0
- Small cart shipping rules validation
- Large cart free shipping validation

---

## Step 6: Final Cleanup & Structural Fix

### Type: Fix Architecture / Code Structure

### Reason:
During refactoring, method structure needed final cleanup to ensure consistent class design and proper indentation.

---

### AI assistance:
Yes — AI helped identify structural issues in class organization and suggested corrections.

---

### My decision:
I ensured:

- All methods are properly inside `CartService`
- Consistent indentation and structure
- Clean object-oriented design

No further decomposition was introduced to avoid over-engineering.

---

### Tests:
- Full integration tests for CartService workflow
- End-to-end validation of add → calculate → save/load flow
- All 10+ tests passing successfully

---

## Final Result

- Clean and maintainable CartService
- Proper separation of responsibilities (without over-engineering)
- Safe file handling with error protection
- Simplified and readable business logic
- All tests passing (10/10)
- Completed step-by-step refactoring with incremental commits
