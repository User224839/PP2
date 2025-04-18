CREATE OR REPLACE PROCEDURE delete_user(identifier TEXT)
LANGUAGE plpgsql
AS
$$
BEGIN
    -- Check if the identifier is a phone number or username
    IF identifier ~ '^\d{10}$' THEN
        -- Delete by phone number
        DELETE FROM phonebook WHERE phone = identifier;
    ELSE
        -- Delete by username
        DELETE FROM phonebook WHERE username = identifier;
    END IF;
END;
$$;


-- Delete by username
CALL delete_user('John Doe');

-- Delete by phone number
CALL delete_user('1234567890');
