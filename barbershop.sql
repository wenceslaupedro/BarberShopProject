CREATE DATABASE barbershop;

USE barbershop;

CREATE TABLE barbers (
    barber_id INT AUTO_INCREMENT PRIMARY KEY,
    barber_name VARCHAR(100)
);

CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    barber_id INT,
    client_name VARCHAR(100),
    appointment_date DATE,
    appointment_time TIME,
    haircut_type VARCHAR(50),
    FOREIGN KEY (barber_id) REFERENCES barbers(barber_id)
);

CREATE TABLE haircuts (
    haircut_id INT AUTO_INCREMENT PRIMARY KEY,
    haircut_name VARCHAR(100),
    price DECIMAL(5,2)
);

INSERT INTO barbers (barber_name) VALUES (
('John'),
('Mike'),
('Tadgh')
);

INSERT INTO haircuts (haircut_name, price) VALUES
('Fade', 20),
('Scisors', 25),
('Beard', 15),
('Fade + Beard', 30),
('Scisors + Beard', 35);