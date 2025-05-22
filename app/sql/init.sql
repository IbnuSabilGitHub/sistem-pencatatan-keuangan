CREATE DATABASE IF NOT EXISTS sistem_pencatatan_keuangan;

USE sistem_pencatatan_keuangan;


-- TABLES category icome
CREATE TABLE IF NOT EXISTS category_income (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- TABLES category expense
CREATE TABLE IF NOT EXISTS category_expense (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- TABLES income
CREATE TABLE IF NOT EXISTS income (
    id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    category_id INT NOT NULL,
    description VARCHAR(100) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    date DATE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (category_id) REFERENCES category_income(id)
    
);

-- TABLES expense
CREATE TABLE IF NOT EXISTS expense (
    id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    category_id INT NOT NULL,
    description VARCHAR(100) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    date DATE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (category_id) REFERENCES category_expense(id)
);
