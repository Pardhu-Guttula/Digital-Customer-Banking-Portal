# Epic Title: Email notifications for status updates

CREATE TABLE email_templates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    content TEXT NOT NULL
);

INSERT INTO email_templates (name, content) VALUES ('status_update', 'Your request status has been updated to: {status}');