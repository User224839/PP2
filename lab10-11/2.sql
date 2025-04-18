CREATE OR REPLACE PROCEDURE insert_or_update_user(username TEXT, surname TEXT, phone TEXT)
LANGUAGE plpgsql
AS
$$
BEGIN
    -- Check if the user already exists
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = username) THEN
        -- Update phone number if user exists
        UPDATE phonebook
        SET phone = phone
        WHERE username = username;
    ELSE
        -- Insert new user if not exists
        INSERT INTO phonebook (username, surname, phone)
        VALUES (username, surname, phone);
    END IF;
END;
$$;
CALL insert_or_update_user('John Doe', 'Doe', '1234567890');
