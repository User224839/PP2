CREATE OR REPLACE PROCEDURE insert_multiple_users(users_data TEXT[][])
LANGUAGE plpgsql
AS
$$
DECLARE
    user_record TEXT[];
    invalid_data TEXT := '';
BEGIN
    -- Loop through the array of users_data
    FOREACH user_record IN ARRAY users_data
    LOOP
        -- Validate phone number
        IF user_record[2] ~ '^\d{10}$' THEN
            -- Insert valid user data
            INSERT INTO phonebook (username, surname, phone)
            VALUES (user_record[1], user_record[2], user_record[3]);
        ELSE
            -- Collect invalid data
            invalid_data := invalid_data || 'Invalid data: ' || user_record[1] || ', ' || user_record[2] || ', ' || user_record[3] || '\n';
        END IF;
    END LOOP;

    -- Return invalid data
    RAISE NOTICE '%', invalid_data;
END;
$$;


CALL insert_multiple_users(ARRAY[
    ARRAY['John', 'Doe', '1234567890'],
    ARRAY['Jane', 'Smith', '12345678a9']  -- Invalid phone
]);