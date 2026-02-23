# Epic Title: Password Recovery

-- Adding a column to store the password reset token in the users table
ALTER TABLE users
ADD COLUMN reset_token VARCHAR(255);