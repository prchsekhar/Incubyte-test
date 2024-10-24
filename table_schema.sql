-- Table for Customers in India (other country tables will follow similar structure)
CREATE TABLE Table_India (
    customer_name VARCHAR(255),
    customer_id VARCHAR(18),
    open_date DATE,
    last_consulted_date DATE,
    vaccination_id CHAR(5),
    doctor_name VARCHAR(255),
    state CHAR(5),
    country CHAR(5),
    dob DATE,
    is_active CHAR(1),
    age INT,  -- Derived column: age calculated from DOB
    days_since_last_consult INT  -- Derived column: days since last consulted
);
