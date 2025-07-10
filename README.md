# 🚕 Urban Routes – Taxi Order Automation

This project is part of Sprint 8 of the QA program and aims to automate the complete flow of ordering a taxi in the **Urban Routes** application, using Selenium WebDriver with the Page Object Model (POM) pattern.

---

## 👤 Author

**Full name:** Luis Manco  
---

## 📌 Project Description

The following user steps are automated:

1. Enter pickup and destination addresses.
2. Select the "Comfort" fare.
3. Enter a phone number.
4. Request and capture the confirmation code.
5. Add a bank card.
6. Write a message for the driver.
7. Request a blanket, tissues, and two ice creams 🍦.
8. Confirm the order.
9. Verify that the driver search modal is displayed.
10. (Optional) Verify that the driver information is displayed.

---

## 🛠 Technologies and Tools Used

- Python 3
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Git & GitHub
- Google Chrome + ChromeDriver

---

## 📁 Project Structure

```
📦qa-project-Urban-Routes-en
├── data.py          # Variables containing test data (phone number, addresses, etc.)
├── main.py          # Automation of the taxi order flow
├── README.md        # This file
```

---

## ▶️ How to Run the Tests

### 1. Clone this repository

```bash
git clone https://github.com/youruser/qa-project-Urban-Routes-en.git
cd qa-project-Urban-Routes-en
```

### 2. Install the dependencies

```bash
pip install selenium pytest
```

### 3. Run the tests

```bash
pytest main.py
```

If your tests are inside a folder (for example, `tests/`), the command would be:

```bash
pytest tests/main.py
```

---

## ✅ Additional Notes

- The code intercepts the phone verification code using Chrome’s network logs (CDP).
- Remember to check the IDs or selectors if the page changes.
- It is recommended to use at least 4 types of selectors: `ID`, `ClassName`, `XPath`, `CSS Selector`.

---

## 📬 Contact

If you have questions or suggestions, feel free to contact me via Discord or through GitHub issues.
