-- Table to store daily punch records
CREATE TABLE punch_records (
    date DATE PRIMARY KEY,
    punch_in_time TIMESTAMP,
    punch_out_time TIMESTAMP
);

-- Table to track the last processed Telegram update
CREATE TABLE telegram_state (
    id INTEGER PRIMARY KEY,
    last_update_id INTEGER
);

-- Initialize telegram_state with a single row
INSERT INTO telegram_state (id, last_update_id) VALUES (1, 0);