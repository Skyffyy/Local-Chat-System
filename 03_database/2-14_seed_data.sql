-- Seed Data for Testing

-- Insert default users (Passwords are simple hashes for development)
INSERT INTO users (username, password_hash, role, status) VALUES
('admin', 'admin_hash_123', 'Admin', 'Active'),
('georgy', 'user_hash_456', 'User', 'Active'),
('guest_user', 'guest_hash_789', 'Guest', 'Active')
ON CONFLICT (username) DO NOTHING;

-- Insert default chat rooms
INSERT INTO rooms (name, description, is_private) VALUES
('general', 'Main chat room for everyone', FALSE),
('dev_room', 'Room for developers to talk about code', FALSE),
('admin_lounge', 'Private room for administrators', TRUE)
ON CONFLICT (name) DO NOTHING;

-- Insert initial welcome messages
INSERT INTO messages (room_id, user_id, message_text) VALUES
(1, 1, 'Welcome to the Local Chat System! System is online.'),
(1, 2, 'Hello everyone! Glad to be here.');