-- Seed Data for Testing

-- Insert default users (Passwords are simple hashes for development)
-- Insert default users with sha256 hashed passwords
-- admin / admin123, georgy / georgy123, guest_user / guest123
INSERT INTO users (username, password_hash, role, status) VALUES
('admin', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', 'Admin', 'Active'),
('georgy', 'defed2e22eb3651a9e4b66334c0fafee7994aeb276f2342cecba73e291689606', 'User', 'Active'),
('guest_user', '6b93ccba414ac1d0ae1e77f3fac560c748a6701ed6946735a49d463351518e16', 'Guest', 'Active')
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