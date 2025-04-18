CREATE OR REPLACE FUNCTION get_phonebook_page(limit INT, offset INT)
RETURNS TABLE(username TEXT, surname TEXT, phone TEXT) AS
$$
BEGIN
    RETURN QUERY
    SELECT username, surname, phone
    FROM phonebook
    LIMIT limit OFFSET offset;
END;
$$ LANGUAGE plpgsql;


SELECT * FROM get_phonebook_page(10, 0);  -- Get the first 10 records
